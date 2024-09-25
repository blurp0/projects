from flask import Flask, render_template, request, jsonify
import nltk
from nltk.stem import PorterStemmer
import random
from data.data import data  # Ensure that 'data' contains your patterns and definitions
import json

app = Flask(__name__)

# Initialize the stemmer
stemmer = PorterStemmer()

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]

def get_response(user_input):
    print("User input:", user_input)
    # Check if the input matches any holiday pattern
    for pattern, info in data.items():
        print("Checking pattern:", pattern)
        if nltk.re.match(pattern, user_input.lower()):
            print("Pattern matched!")
            # Only set 'name' if it hasn't been set (to avoid overwriting during follow-ups)
            if 'name' not in info:
                info['name'] = user_input.split()[-2] + " " + user_input.split()[-1]

            # Return the definition or date as needed
            if "what" in user_input.lower():
                return (f"{info['definition']}<br>Would you like to know the date? (yes/no)", "definition", pattern, info)
            elif "when" in user_input.lower():
                date_response = random.choice(info['date'])
                return (f"{date_response}<br>Would you like to know the definition? (yes/no)", "date", pattern, info)
            else:
                return ("I'm sorry, I didn't understand that. Please ask what or when.", None, None, {})

    print("No pattern matched. Returning default response.")
    return ("I'm sorry, I didn't understand that. Please ask about a holiday.", None, None, {})


def follow_up_response(user_input, context, pattern, info):
    print(f"Follow-up context: {context}, info: {info}")  # Debugging info
    if "yes" in user_input.lower():
        if context == "date":
            response = f"Great! {info['definition']}<br>Pick another holiday or tell me which holiday you want to know."
        elif context == "definition":
            date_response = random.choice(info['date'])
            response = f"Great! {date_response}<br>Pick another holiday or tell me which holiday you want to know."
        
        # Reset context and pattern to allow new input
        context = None
        pattern = None
        info = {}
        
        return response, context, pattern, info  # Return updated values

    elif "no" in user_input.lower():
        return "Okay! Pick another holiday or tell me which holiday you want to know.", context, pattern, info  # Maintain state
    return "I'm sorry, I didn't understand that. Please answer with yes or no.", context, pattern, info  # Maintain state

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
