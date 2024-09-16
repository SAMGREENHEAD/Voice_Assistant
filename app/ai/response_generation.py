
def generate_response(intent):
    """
    This function generates a response based on the given intent.

    Parameters:
    intent (str): The intent of the user's request. It can be one of the following:
        - "get_time": Indicates the user wants to know the current time.
        - "shutdown_system": Indicates the user wants to shut down the system.

    Returns:
    str: The response generated based on the given intent.
        - If the intent is "get_time", the response will be "The time is ...".
        - If the intent is "shutdown_system", the response will be "Shutting down...".
        - If the intent is neither "get_time" nor "shutdown_system", the response will be "I didn't understand that.".
    """
    if intent == "get_time":
        return "The time is ..."
    elif intent == "shutdown_system":
        return "Shutting down..."
    else:
        return "I didn't understand that."
