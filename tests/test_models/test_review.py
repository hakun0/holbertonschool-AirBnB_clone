#!/usr/bin/python3

import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up an instance of Review for testing"""
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after tests"""
        del cls.rev1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        # Check the code style using pep8
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """Check if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Check if Review has a docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """Check if Review has the required attributes"""
        self.assertTrue('id' in self.rev1.__dict__)
        self.assertTrue('created_at' in self.rev1.__dict__)
        self.assertTrue('updated_at' in self.rev1.__dict__)
        self.assertTrue('place_id' in self.rev1.__dict__)
        self.assertTrue('text' in self.rev1.__dict__)
        self.assertTrue('user_id' in self.rev1.__dict__)

    def test_attributes_are_strings(self):
        """Check if attributes with string values are of type str"""
        self.assertEqual(type(self.rev1.text), str)
        self.assertEqual(type(self.rev1.place_id), str)
        self.assertEqual(type(self.rev1.user_id), str)

    def test_save(self):
        """Test the save method"""
        self.rev1.save()
        self.assertNotEqual(self.rev1.created_at, self.rev1.updated_at)

    def test_to_dict(self):
        """Check if to_dict method is present in the instance"""
        self.assertEqual('to_dict' in dir(self.rev1), True)

if __name__ == "__main__":
    unittest.main()
