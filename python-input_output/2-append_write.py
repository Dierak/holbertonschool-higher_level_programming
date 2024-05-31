#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_lines(filename="", nb_lines=0):
    """Print a given number of lines from a UTF8 text file to stdout.

    This function reads and prints a specified number of lines from a text file.
    If the number of lines specified is less than or equal to 0, the entire file is printed.
    If the number of lines specified exceeds the total number of lines in the file,
    the entire file is printed.

    Args:
        filename (str): The name of the file to read from. Defaults to an empty string.
        nb_lines (int): The number of lines to read from the file. Defaults to 0.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs during file reading.
    """
    with open(filename, encoding="utf-8") as f:
        # If nb_lines is less than or equal to 0, print the entire file
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        # Count the total number of lines in the file
        lines = 0
        for line in f:
            lines += 1
        f.seek(0)  # Reset the file pointer to the beginning of the file

        # If nb_lines is greater than or equal to the total number of lines, print the entire file
        if nb_lines >= lines:
            print(f.read(), end="")
            return

        # Print the specified number of lines
        else:
            n = 0
            while n < nb_lines:
                print(f.readline(), end="")
                n += 1
