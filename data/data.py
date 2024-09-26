# data for chatbot

greetings = [
    {"pattern": r"hey|hi|hello", "response": "Hi there! I'm Holly Germ, your holiday expert! What's your name? 😊"},
    {"pattern": r"how are you", "response": "I'm doing great, thanks for asking! And you? 😊"},
    {"pattern": r"(.*)morning|(.*)afternoon|(.*)evening", "response": "Thank you, How can I assist you today? 😊"},
    {"pattern": r"what is your name|tell me your name|who are you", "response": "I'm Holly Germ, your friendly holiday expert! How can I assist you today? 😊"},
    {"pattern": r"what do you do|what's your purpose", "response": "I provide information about Philippine holidays! Feel free to ask me anything! 🎉"},
    {"pattern": r"tell me about yourself|describe yourself", "response": "I'm Holly Germ, passionate about Philippine holidays. What's your favorite holiday? 🌟"},
]


data = {

    r"(.*)when(.*)new year(.*)|what(.*)new year(.*)": {
        "definition": "New Year's Day celebrates the first day of the Gregorian calendar year.",
        "date": [
            "It was celebrated on January 1.",
            "The first day of the year was January 1."
        ]
    },
    r"(.*)when(.*)maundy thursday(.*)|what(.*)maundy thursday(.*)": {
        "definition": "Maundy Thursday commemorates the Last Supper of Jesus Christ with the Apostles.",
        "date": [
            "It was celebrated on March 28.",
            "You could find it on March 28."
        ]
    },
    r"(.*)when(.*)good friday(.*)|what(.*)good friday(.*)": {
        "definition": "Good Friday observes the crucifixion and death of Jesus Christ.",
        "date": [
            "It was celebrated on March 29.",
            "You could mark your calendar for March 29."
        ]
    },
    r"(.*)when(.*)araw ng kagitingan(.*)|what(.*)araw ng kagitingan(.*)": {
        "definition": "Araw ng Kagitingan honors the bravery of Filipino and American soldiers during World War II.",
        "date": [
            "It was celebrated on April 9.",
            "The date for this holiday was April 9."
        ]
    },
    r"(.*)when(.*)labor day(.*)|what(.*)labor day(.*)": {
        "definition": "Labor Day celebrates the contributions of workers and the labor movement.",
        "date": [
            "It was celebrated on May 1.",
            "You could mark your calendar for May 1."
        ]
    },
    r"(.*)when(.*)independence day(.*)|what(.*)independence day(.*)": {
        "definition": "Independence Day marks the declaration of Philippine independence from Spanish rule in 1898.",
        "date": [
            "It was celebrated on June 12.",
            "The holiday fell on June 12."
        ]
    },
    r"(.*)when(.*)national heroes day(.*)|what(.*)national heroes day(.*)": {
        "definition": "National Heroes Day honors the national heroes of the Philippines.",
        "date": [
            "It was celebrated on August 26.",
            "You could observe it on August 26."
        ]
    },
    r"(.*)when(.*)bonifacio day(.*)|what(.*)bonifacio day(.*)": {
        "definition": "Bonifacio Day commemorates the birth of Andrés Bonifacio, a Filipino revolutionary leader.",
        "date": [
            "It was celebrated on November 30.",
            "This day was observed on November 30."
        ]
    },
    r"(.*)when(.*)christmas day(.*)|what(.*)christmas day(.*)": {
        "definition": "Christmas Day celebrates the birth of Jesus Christ.",
        "date": [
            "It was celebrated on December 25.",
            "The date for this celebration was December 25."
        ]
    },
    r"(.*)when(.*)rizal day(.*)|what(.*)rizal day(.*)": {
        "definition": "Rizal Day honors the life and works of José Rizal, a national hero of the Philippines.",
        "date": [
            "It was celebrated on December 30.",
            "You could observe it on December 30."
        ]
    },
    r"(.*)when(.*)ninoy aquino day(.*)|what(.*)ninoy aquino day(.*)": {
        "definition": "Ninoy Aquino Day commemorates the assassination of Benigno “Ninoy” Aquino Jr., a Filipino senator and opposition leader.",
        "date": [
            "It was celebrated on August 21.",
            "The holiday was on August 21."
        ]
    },
    r"(.*)when(.*)all saints' day(.*)|what(.*)all saints' day(.*)": {
        "definition": "All Saints' Day honors all saints, known and unknown, in Christian tradition.",
        "date": [
            "It was celebrated on November 1.",
            "You could find it on November 1."
        ]
    },
    r"(.*)when(.*)the feast of the immaculate conception(.*)|what(.*)the feast of the immaculate conception(.*)": {
        "definition": "The Feast of the Immaculate Conception celebrates the belief in the Immaculate Conception of the Virgin Mary.",
        "date": [
            "It was celebrated on December 8.",
            "You could mark December 8 for this holiday."
        ]
    },
    r"(.*)when(.*)the last day of the year(.*)|what(.*)the last day of the year(.*)": {
        "definition": "The last day of the year marks the final day of the Gregorian calendar year.",
        "date": [
            "It was celebrated on December 31.",
            "The last day of the year was December 31."
        ]
    },
    r"(.*)when(.*)the chinese new year(.*)|what(.*)the chinese new year(.*)": {
        "definition": "The Chinese New Year celebrates the beginning of the lunar new year, observed by Chinese communities worldwide.",
        "date": [
            "It was celebrated on February 10.",
            "The lunar new year fell on February 10."
        ]
    },
    r"(.*)when(.*)black saturday(.*)|what(.*)black saturday(.*)": {
        "definition": "Black Saturday observes the day Jesus Christ lay in the tomb after his crucifixion.",
        "date": [
            "It was celebrated on March 30.",
            "This holiday was on March 30."
        ]
    },
    r"(.*)when(.*)all souls' day(.*)|what(.*)all souls' day(.*)": {
        "definition": "All Souls' Day commemorates all the faithful departed, particularly but not exclusively one’s relatives.",
        "date": [
            "It was celebrated on November 2.",
            "You could observe it on November 2."
        ]
    },
    r"(.*)when(.*)christmas eve(.*)|what(.*)christmas eve(.*)": {
        "definition": "Christmas Eve is the evening or entire day before Christmas Day, celebrating the birth of Jesus Christ.",
        "date": [
            "It was celebrated on December 24.",
            "You could mark December 24 for this celebration."
        ]
    },
}
