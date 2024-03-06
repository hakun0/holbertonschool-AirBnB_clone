#!/usr/bin/python3
""" first class base """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ class Basemodel """

    def __init__(self, *args, **kwargs):
        """ Constructor for BaseModel """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            """if kwargs is empty"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """ to save the updated d.time """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Return a dictionary representation of the instance.
            returns:
            dict: A dictionary containing instance attributes
            and a __class__ key.
            Converts created_at and updated_at
            to string objects in ISO format.
        """
        class_name = self.__class__.__name__
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = class_name

        """ to convert """
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.created_at.isoformat()
        return instance_dict

    def __str__(self):
        """ Return a string representation of the instance """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id,
                self.__dict__
        )
