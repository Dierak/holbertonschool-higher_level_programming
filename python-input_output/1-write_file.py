#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Parameters:
    filename (str): The name of the file to write to. Defaults to an empty string.
    text (str): The text to write to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    # Open the file in write mode with UTF-8 encoding using the with statement
    with open(filename, "w", encoding="utf-8") as file:
        # Write the provided text to the file
        file.write(text)
    
    # Return the number of characters written
    return len(text)
