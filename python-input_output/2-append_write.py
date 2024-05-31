#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a text 
file (UTF8)and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8) and returns the number of 
    characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    # Open the file in append mode with UTF-8 encoding using the with statement
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)

    # Return the number of characters written
    return num_chars
