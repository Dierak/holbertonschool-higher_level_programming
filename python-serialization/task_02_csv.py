#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and write the JSON data to data.json.
    
    Parameters:
        csv_filename (str): The filename of the CSV file.
        
    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
