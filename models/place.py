#!/usr/bin/python3
"""place module
"""


import datetime
import uuid
from models.base_model import BaseModel


class Place(BaseModel):
    """place model inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """init method for place class used in instantiation
        """
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
