#!/bin/python3
"""Base model for air bnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self,  *args, **kwargs):
        """Docstrings"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    elif key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Docstrings"""
        return "[{}]\
({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Docstrings"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Docstring"""
        tmp_dict = self.__dict__.copy()
        tmp_dict["__class__"] = self.__class__.__name__
        tmp_dict['created_at'] = self.created_at.isoformat()
        tmp_dict['updated_at'] = self.updated_at.isoformat()
        return(tmp_dict)
