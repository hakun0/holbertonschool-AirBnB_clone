import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel  # Import the BaseModel class from your actual module        


class TestBaseModel(unittest.TestCase):

    @patch('models.base_model.datetime')
    def test_init(self, mock_datetime):
        mock_now = datetime(2023, 10, 31, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        base_model = BaseModel()

        self.assertIsNotNone(base_model.id)
        self.assertEqual(base_model.created_at, mock_now)
        self.assertEqual(base_model.updated_at, mock_now)

    def test_save(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()

        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertTrue('__class__' in base_model_dict)
        self.assertTrue('created_at' in base_model_dict)
        self.assertTrue('updated_at' in base_model_dict)

    def test_str(self):
        base_model = BaseModel()
        obj_str = str(base_model)

        self.assertTrue(base_model.__class__.__name__ in obj_str)
        self.assertTrue(base_model.id in obj_str)

if __name__ == '__main__':
    unittest.main()
