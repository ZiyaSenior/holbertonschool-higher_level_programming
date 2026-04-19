#!/usr/bin/python3
"""Student class with serialization and deserialization"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of Student"""
        obj_dict = self.__dict__

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: obj_dict[k] for k in attrs if k in obj_dict}

        return obj_dict

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
