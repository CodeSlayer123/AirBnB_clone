#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.amenity import Amenity
from models import storage
import pep8


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.a1 = Amenity()
        self.a2 = Amenity()
        my_dict = self.a2.to_dict()
        self.a3 = Amenity(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.a1
        del self.a2
        del self.a3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.a1.id, exists)
        self.assertTrue(self.a2.created_at, exists)
        self.assertTrue(self.a3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_u = "[{}]({}) {}".format\
            (self.a1.__class__.__name__, \
                self.a1.id, self.a1.__dict__)
        self.assertEqual(self.a1.__str__(), print_u)

    def test_save(self):
        """
        Tests save method
        """
        self.a1.save()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        a1_dict = self.a1.to_dict()
        self.assertEqual(a1_dict['__class__'], 'Amenity')
        self.assertEqual(a1_dict['created_at'],
                         self.a1.created_at.isoformat())
        self.assertEqual(a1_dict['updated_at'],
                         self.a1.updated_at.isoformat())
        self.assertEqual(a1_dict['id'], self.a1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.a1, 'NonExistentKey')
        # set attr and test it
        self.a1.Job = "Code Monkey"
        self.assertTrue(self.a1.Job, exists)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)
        self.assertTrue(len(Amenity.__init__.__doc__) >= 1)
        self.assertTrue(len(Amenity.__str__.__doc__) >= 1)
        self.assertTrue(len(Amenity.save.__doc__) >= 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()