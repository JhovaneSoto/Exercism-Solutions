"""This module contains a function that returns a personalized 'Two-fer' message."""

def two_fer(name="you"):
    """
    Return a string using the given name.
    
    Args:
        name (str): The name to include in the returned string. Defaults to "you".

    Returns:
        str: A string formatted as "One for <name>, one for me."
    """
    return f"One for {name}, one for me."
