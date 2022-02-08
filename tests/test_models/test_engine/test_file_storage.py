#!/usr/bin/python3
"""
Tests for File Storage



"""
from os.path import exists
import unittest
from models import *
from models import storage
import pep8


class TestFileStorage(unittest.TestCase):
    """
    Test cases for File Storage
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.fs1 = BaseModel()
        self.fs2 = BaseModel()
        self.my_dict = self.fs2.to_dict()
        self.fs3 = BaseModel(**self.my_dict)
        self.objects = storage.all

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.fs1
        del self.fs2
        del self.fs3
        storage.save()

    def test_save(self):
        """
        Tests save method
        """
        self.fs1.save()
        self.assertNotEqual(self.fs1.created_at, self.fs1.updated_at)
        self.assertTrue(exists("file.json"))

    def test_new(self):
        storage.new(self.fs3)

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()