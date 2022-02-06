#!/usr/bin/python3
"""
Tests for File Storage
"""
from genericpath import exists
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
        self.s1 = State()
        self.s2 = State()
        my_dict = self.s2.to_dict()
        self.s3 = State(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.s1
        del self.s2
        del self.s3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.s1.id, exists)
        self.assertTrue(self.s2.created_at, exists)
        self.assertTrue(self.s3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_u = "[{}]({}) {}".format\
            (self.s1.__class__.__name__, \
                self.s1.id, self.s1.__dict__)
        self.assertEqual(self.s1.__str__(), print_u)

    def test_save(self):
        """
        Tests save method
        """
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        s1_dict = self.s1.to_dict()
        self.assertEqual(s1_dict['__class__'], 'State')
        self.assertEqual(s1_dict['created_at'],
                         self.s1.created_at.isoformat())
        self.assertEqual(s1_dict['updated_at'],
                         self.s1.updated_at.isoformat())
        self.assertEqual(s1_dict['id'], self.s1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.s1, 'NonExistentKey')
        # set attr and test it
        self.s1.Job = "Code Monkey"
        self.assertTrue(self.s1.Job, exists)

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(State.__doc__) >= 1)
        self.assertTrue(len(State.__init__.__doc__) >= 1)
        self.assertTrue(len(State.__str__.__doc__) >= 1)
        self.assertTrue(len(State.save.__doc__) >= 1)
        self.assertTrue(len(State.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()