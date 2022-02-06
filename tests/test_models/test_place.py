#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.place import Place
from models import storage
import pep8


class TestPlace(unittest.TestCase):
    """
    Test cases for Place
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.p1 = Place()
        self.p2 = Place()
        my_dict = self.p2.to_dict()
        self.p3 = Place(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.p1
        del self.p2
        del self.p3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.p1.id, exists)
        self.assertTrue(self.p2.created_at, exists)
        self.assertTrue(self.p3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_u = "[{}]({}) {}".format\
            (self.p1.__class__.__name__, \
                self.p1.id, self.p1.__dict__)
        self.assertEqual(self.p1.__str__(), print_u)

    def test_save(self):
        """
        Tests save method
        """
        self.p1.save()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        p1_dict = self.p1.to_dict()
        self.assertEqual(p1_dict['__class__'], 'Place')
        self.assertEqual(p1_dict['created_at'],
                         self.p1.created_at.isoformat())
        self.assertEqual(p1_dict['updated_at'],
                         self.p1.updated_at.isoformat())
        self.assertEqual(p1_dict['id'], self.p1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.p1, 'NonExistentKey')
        # set attr and test it
        self.p1.Job = "Code Monkey"
        self.assertTrue(self.p1.Job, exists)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(Place.__doc__) >= 1)
        self.assertTrue(len(Place.__init__.__doc__) >= 1)
        self.assertTrue(len(Place.__str__.__doc__) >= 1)
        self.assertTrue(len(Place.save.__doc__) >= 1)
        self.assertTrue(len(Place.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()