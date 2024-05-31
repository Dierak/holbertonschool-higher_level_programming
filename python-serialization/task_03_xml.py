#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to the given filename.

    Parameters:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename to save the serialized XML data.
    """
    root = ET.Element("data")

    # Iterate through the dictionary items and add them as child elements to the root
    for key, value in dictionary.items():
        # Create a new child element for each key-value pair
        child = ET.Element(key)
        child.text = str(value)  # Convert value to string before setting as text
        root.append(child)

    # Write the XML tree to the provided filename
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename and return a Python dictionary.

    Parameters:
        filename (str): The filename from which to read the XML data.

    Returns:
        dict: The deserialized Python dictionary.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct the dictionary from XML elements
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    # Convert values to appropriate data types
    for key, value in dictionary.items():
        # Try converting to integer
        try:
            dictionary[key] = int(value)
        except ValueError:
            # If conversion to integer fails, retain the value as string
            pass

    return dictionary
