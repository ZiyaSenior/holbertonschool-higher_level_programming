#!/usr/bin/python3
"""Student class module with filtered JSON output"""


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
            filtered_dict = {}
            for key in attrs:
                if key in obj_dict:
                    filtered_dict[key] = obj_dict[key]
            return filtered_dict

        return obj_dict
