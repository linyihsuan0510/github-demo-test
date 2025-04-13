from main import count_characters, count_words, is_palindrome

def test_count_characters():
    assert count_characters("Hello") == 5

def test_count_words():
    assert count_words("Hello world") == 2

def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True
