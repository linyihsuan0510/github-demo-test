def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def is_palindrome(text):
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]
