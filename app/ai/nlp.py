import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
def clean_text(text):
    """
    This function takes a string of text as input and performs several cleaning operations.
    It removes any non-alphanumeric characters and converts the text to lowercase.

    Parameters:
    text (str): The input text to be cleaned.

    Returns:
    str: The cleaned text with only alphanumeric characters and converted to lowercase.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
