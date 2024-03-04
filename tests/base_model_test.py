# Assuming you have a test framework like unittest set up
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_str_representation(self):
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(instance.__str__(), expected_str)

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(type(instance_dict['created_at']), str)
        self.assertEqual(type(instance_dict['updated_at']), str)

if __name__ == "__main__":
    unittest.main()
