
import os
def shutdown():
    """
    This function is used to initiate a shutdown of the system.

    Parameters:
    None

    Returns:
    str: A message indicating that the system is shutting down.
    """
    os.system("shutdown /s /t 1")
    return "Shutting down the system."

