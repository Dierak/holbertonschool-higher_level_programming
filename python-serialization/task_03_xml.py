import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to the given filename.
    
    Parameters:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename to save the serialized XML data.
    """
    def _serialize_element(parent, dictionary):
        for key, value in dictionary.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                _serialize_element(child, value)
            else:
                child.text = str(value)
    
    try:
        root = ET.Element("data")
        _serialize_element(root, dictionary)
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print("Dictionary serialized to", filename)
        return True
    except Exception as e:
        print("Error during serialization:", e)
        return False

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename and return a Python dictionary.
    
    Parameters:
        filename (str): The filename from which to read the XML data.
        
    Returns:
        dict: The deserialized Python dictionary.
    """
    def _deserialize_element(element):
        dictionary = {}
        for child in element:
            if list(child):  # If the child has children, it's a nested dictionary
                dictionary[child.tag] = _deserialize_element(child)
            else:
                dictionary[child.tag] = child.text
        return dictionary
    
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = _deserialize_element(root)
        
        # Convert values to appropriate data types
        def _convert_value(value):
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    if value.lower() == 'true':
                        return True
                    elif value.lower() == 'false':
                        return False
                    else:
                        return value
        
        def _convert_dictionary(d):
            for key, value in d.items():
                if isinstance(value, dict):
                    _convert_dictionary(value)
                else:
                    d[key] = _convert_value(value)
        
        _convert_dictionary(dictionary)
        
        return dictionary
    except ET.ParseError as e:
        print("Error during XML parsing:", e)
        return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print("Error during deserialization:", e)
        return None
