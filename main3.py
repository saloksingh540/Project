import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks for asking!", "I'm good, how about you?",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using Python and NLTK.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "Goodbye!",]
    ],
]

def simple_chatbot():
    print("Hi, I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    simple_chatbot()
