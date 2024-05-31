#!/usr/bin/python3
"""
Description:
    This module defines a custom Python class named CustomObject.
    The CustomObject class represents an object with attributes like
    name, age, and is_student.

Classes:
    CustomObject: Represents an object with attributes.
    Provides methods for display, serialization, and deserialization.
"""


import pickle
class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with provided attributes.
        
        Parameters:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Whether the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the attributes of the object.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)
    
    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to the provided filename using pickle.
        
        Parameters:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except pickle.PickleError as e:
            print("Error occurred while serializing the object:", e)
    
    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from the provided filename using pickle.
        
        Parameters:
            filename (str): The filename from which to load the serialized object.
        
        Returns:
            CustomObject or None: An instance of CustomObject if successfully loaded, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except pickle.PickleError as e:
            print("Error occurred while deserializing the object:", e)
            return None
