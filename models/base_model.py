#!/usr/bin/env python3

import uuid
import datetime

class BaseModel():
    """base model parent class for all other classes
       used in project
    """

    def __init__(self):
        """init method for base class used in instantiation
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """custom str method for str and print
        """
        builder = "["
        builder += str(self.__class__.__name__) + '] ('
        builder += str(self.id) + ') ' + str(self.__dict__)
        return builder

    def save(self):
        """save method used for updating class so updated_at changes
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns the dictionary of our instance
        """
        temp_d = self.__dict__
        temp_d['__class__'] = self.__class__.__name__
        temp_d['created_at'] = self.created_at.isoformat()
        temp_d['updated_at'] = self.updated_at.isoformat()
        return temp_d
