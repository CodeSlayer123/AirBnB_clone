#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.city import City
from models import storage
import pep8


class TestCity(unittest.TestCase):
    """
    Test cases for City
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.c1 = City()
        self.c2 = City()
        my_dict = self.c2.to_dict()
        self.c3 = City(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.c1
        del self.c2
        del self.c3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.c1.id, exists)
        self.assertTrue(self.c2.created_at, exists)
        self.assertTrue(self.c3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_u = "[{}]({}) {}".format\
            (self.c1.__class__.__name__, \
                self.c1.id, self.c1.__dict__)
        self.assertEqual(self.c1.__str__(), print_u)

    def test_save(self):
        """
        Tests save method
        """
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        c1_dict = self.c1.to_dict()
        self.assertEqual(c1_dict['__class__'], 'City')
        self.assertEqual(c1_dict['created_at'],
                         self.c1.created_at.isoformat())
        self.assertEqual(c1_dict['updated_at'],
                         self.c1.updated_at.isoformat())
        self.assertEqual(c1_dict['id'], self.c1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.c1, 'NonExistentKey')
        # set attr and test it
        self.c1.Job = "Code Monkey"
        self.assertTrue(self.c1.Job, exists)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(City.__doc__) >= 1)
        self.assertTrue(len(City.__init__.__doc__) >= 1)
        self.assertTrue(len(City.__str__.__doc__) >= 1)
        self.assertTrue(len(City.save.__doc__) >= 1)
        self.assertTrue(len(City.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()