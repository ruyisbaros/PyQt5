from random import choice


my_words = ['apple', 'banana', 'cherry', 'date',
            'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

# Function to generate a random word


def generate_random_word():
    return choice(my_words)
