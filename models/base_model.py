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
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(kwargs[k])
                if k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
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
        new_dict['__class__'] = type(self).__name__
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
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
