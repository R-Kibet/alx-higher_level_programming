#!/usr/bin/python3
""" class Student """


class Student:
    """ class """
    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary descritption """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces Student instance '''
        for attr in json:
            self.__dict__[attr] = json[attr]
