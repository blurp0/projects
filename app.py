# app.py (chatbot main python file)
import re
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.stem import PorterStemmer
import random
from data.data import data, greetings  # Import greetings patterns from data
import json

app = Flask(__name__)

# Initialize the stemmer
stemmer = PorterStemmer()

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]

def get_response(user_input):
    print("Handling new input")
    print("User input:", user_input)

    # Check for goodbye inputs
    if re.search(r"\b(bye|goodbye)\b", user_input.lower()):
        print("Goodbye pattern matched!")
        return "Goodbye! Have a great day! 👋", "goodbye", None, {}

    # Check for greetings first using imported patterns
    for item in greetings:
        pattern = item["pattern"]
        if re.search(pattern, user_input.lower()):
            print("Greeting pattern matched!")
            return item["response"], "greeting", None, {}

    # If no greetings matched, check holiday patterns
    for pattern, info in data.items():
        print("Checking pattern:", pattern)
        if re.match(pattern, user_input.lower()):
            print("Pattern matched!")
            if "what" in user_input.lower():
                return f"{info['definition']}<br>Would you like to know the date? (yes/no)", "definition", pattern, info
            elif "when" in user_input.lower():
                date_response = random.choice(info['date']) if info['date'] else "I don't have the date for that."
                return f"{date_response}<br>Would you like to know the definition? (yes/no)", "date", pattern, info

    # Default response if no patterns matched
    print("No pattern matched. Returning default response.")
    return "I'm sorry, I didn't understand that. Please ask about a holiday.", None, None, {}

def follow_up_response(user_input, context, pattern, info):
    print(f"Follow-up context: {context}, info: {info}")
    if "yes" in user_input.lower():
        if context == "date":
            response = f"Glad you're interested! Here's more about it: {info['definition']}<br>Feel free to ask about another holiday!"
        elif context == "definition":
            date_response = random.choice(info['date'])
            response = f"Got it! {date_response}.<br>Anything else you’re curious about?"

        # Reset context
        context = None
        pattern = None
        info = {}

        return response, context, pattern, info
    
    elif "no" in user_input.lower():
        return "Okay, no problem! Let me know if you'd like to hear about another holiday.", context, pattern, info
    
    return "Hmm, I didn’t quite get that. Can you answer with yes or no?", context, pattern, info


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Safely load context, info, and pattern
        context = request.form.get("context")  # Keep as string
        info = json.loads(request.form.get("info", "{}")) if request.form.get("info") else {}
        pattern = request.form.get("pattern")  # Keep as string

        user_input = request.form["msg"]

        # Your chatbot logic here
        response, context, pattern, info = process_user_input(user_input, context, info, pattern)  # Ensure all arguments are provided

        # Send back the updated context, info, and pattern along with the response
        return jsonify({
            "response": response,
            "context": context,
            "info": info,
            "pattern": pattern
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Sorry, something went wrong!"}), 500

def process_user_input(user_input, context, info, pattern):
    # Check if we are in a follow-up conversation
    if context in ["date", "definition"] and info:
        print("Handling follow-up response")
        return follow_up_response(user_input, context, pattern, info)
    
    # Otherwise, this is the first time we're processing user input
    print("Handling new input")
    response, new_context, new_pattern, new_info = get_response(user_input)
    
    # Update context, pattern, and info
    context = new_context
    pattern = new_pattern
    info = new_info

    return response, context, pattern, info  # Return all values

if __name__ == "__main__":
    app.run(debug=True)
