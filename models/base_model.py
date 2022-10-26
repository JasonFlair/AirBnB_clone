#!/usr/bin/python3
"""Defines a base model class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    the base model of the console
    """

    def __init__(self, *args, **kwargs):
        """
        the initialiser
        :param id: id of the model
        """
        if kwargs:
            self.__dict__.update((k, v) for k, v in kwargs.items())
        else:
            creation_time = datetime.now()
            update_time = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = creation_time
            self.updated_at = update_time
            models.storage.new(self)

    def to_dict(self):
        """
        to dict function
        :return: dictionary representation
        """
        new_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = datetime.isoformat(value)
            elif key == "updated_at":
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value

        return new_dict
    def save(self):
        """
        update and save time of update
        """
        update_time = datetime.now()
        self.updated_at = update_time
        models.storage.save()

    def __str__(self):
        """
        printable representation returned.
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"