
def recognize_intent(text):
    """
    This function is designed to recognize the intent of a given text.
    It checks for specific keywords in the input text and returns a corresponding intent.

    Parameters:
    text (str): The input text to be analyzed.

    Returns:
    str: The recognized intent. It can be one of the following:
         - "get_time": If the input text contains the keyword "time".
         - "shutdown_system": If the input text contains the keyword "shutdown".
         - "unknown": If the input text does not contain any of the specified keywords.
    """
    if "time" in text:
        return "get_time"
    elif "shutdown" in text:
        return "shutdown_system"
    else:
        return "unknown"
