#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.review import Review
from models import storage
import pep8


class TestReview(unittest.TestCase):
    """
    Test cases for Review
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.r1 = Review()
        self.r2 = Review()
        my_dict = self.r2.to_dict()
        self.r3 = Review(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.r1
        del self.r2
        del self.r3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.r1.id, exists)
        self.assertTrue(self.r2.created_at, exists)
        self.assertTrue(self.r3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_r = "[{}]({}) {}".format\
            (self.r1.__class__.__name__, \
                self.r1.id, self.r1.__dict__)
        self.assertEqual(self.r1.__str__(), print_r)

    def test_save(self):
        """
        Tests save method
        """
        self.r1.save()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        s1_dict = self.r1.to_dict()
        self.assertEqual(s1_dict['__class__'], 'Review')
        self.assertEqual(s1_dict['created_at'],
                         self.r1.created_at.isoformat())
        self.assertEqual(s1_dict['updated_at'],
                         self.r1.updated_at.isoformat())
        self.assertEqual(s1_dict['id'], self.r1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.r1, 'NonExistentKey')
        # set attr and test it
        self.r1.Job = "Code Monkey"
        self.assertTrue(self.r1.Job, exists)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(Review.__doc__) >= 1)
        self.assertTrue(len(Review.__init__.__doc__) >= 1)
        self.assertTrue(len(Review.__str__.__doc__) >= 1)
        self.assertTrue(len(Review.save.__doc__) >= 1)
        self.assertTrue(len(Review.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()