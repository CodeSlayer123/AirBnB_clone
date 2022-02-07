#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.user import User
from models import storage
import pep8


class TestUsers(unittest.TestCase):
    """
    Test cases for Users
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.u1 = User()
        self.u2 = User()
        my_dict = self.u2.to_dict()
        self.u3 = User(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.u1
        del self.u2
        del self.u3
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.u1.id, exists)
        self.assertTrue(self.u2.created_at, exists)
        self.assertTrue(self.u3.updated_at, exists)
        self.assertEqual(self.u1.password, "")
        self.assertEqual(self.u2.email, "")
        self.assertEqual(self.u3.first_name, "")
        self.assertEqual(self.u3.last_name, "")


    def test_str(self):
        """
        Tests __str__ method
        """
        print_u = "[{}]({}) {}".format\
            (self.u1.__class__.__name__, \
                self.u1.id, self.u1.__dict__)
        self.assertEqual(self.u1.__str__(), print_u)

    def test_save(self):
        """
        Tests save method
        """
        self.u1.save()
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        u1_dict = self.u1.to_dict()
        self.assertEqual(u1_dict['__class__'], 'User')
        self.assertEqual(u1_dict['created_at'],
                         self.u1.created_at.isoformat())
        self.assertEqual(u1_dict['updated_at'],
                         self.u1.updated_at.isoformat())
        self.assertEqual(u1_dict['id'], self.u1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.u1, 'NonExistentKey')
        # set attr and test it
        self.u1.Job = "Code Monkey"
        self.assertTrue(self.u1.Job, exists)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        self.assertTrue(len(User.__doc__) >= 1)
        self.assertTrue(len(User.__init__.__doc__) >= 1)
        self.assertTrue(len(User.__str__.__doc__) >= 1)
        self.assertTrue(len(User.save.__doc__) >= 1)
        self.assertTrue(len(User.to_dict.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()