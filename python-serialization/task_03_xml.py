#!/usr/bin/python3
"""XML serialization and deserialization module"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to an XML file"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)

    with open(filename, "wb") as f:
        tree.write(f)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a dictionary"""

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        result[child.tag] = child.text

    return result
