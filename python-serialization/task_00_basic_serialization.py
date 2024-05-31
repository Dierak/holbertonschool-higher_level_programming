#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize data to JSON format and save it to the specified file.
    
    Parameters:
        data (dict): A Python Dictionary with data to be serialized.
        filename (str): The filename of the output JSON file. If the output file already exists,
                        it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from the specified file.
    
    Parameters:
        filename (str): The filename of the input JSON file.
        
    Returns:
        dict: A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
