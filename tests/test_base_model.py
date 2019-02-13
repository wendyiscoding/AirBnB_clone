#!/usr/bin/env python3


import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class for testing base models
    """
    def setUp(self):
        self.temp_b = BaseModel()

    def tearDown(self):
        self.temp_b = None

    def test_basic_attribute_set(self):
        self.temp_b.name = "bennett"
        self.temp_b.xyz = 400
        self.assertEqual(self.temp_b.name, "bennett")
        self.assertEqual(self.temp_b.xyz, 400)

    def test_string_return(self):
        """tests the string method to make sure it returns
            the proper string
        """
        my_str = str(self.temp_b)
        id_test = "[BaseModel] ({})".format(self.temp_b.id)
        boolean = id_test in my_str
        self.assertEqual(True, boolean)
        boolean = "updated_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "created_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in my_str
        self.assertEqual(True, boolean)

    def test_to_dict(self):
        """tests the to_dict method to make sure properly working
        """
        my_dict = self.temp_b.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.temp_b.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.temp_b.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.temp_b.__class__.__name__)
        self.assertEqual(my_dict['id'], self.temp_b.id)
        
