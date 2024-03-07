#!/usr/bin/python3
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the 'all' method of FileStorage"""
        # Verify that the 'all' method returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the 'new' method of FileStorage"""
        key = self.base_model.__class__.__name__ + "." + self.base_model.id
        # Add an object to the storage and check if it exists in the storage
        self.storage.new(self.base_model)
        self.assertEqual(self.storage.all()[key], self.base_model)

    def test_save_and_reload(self):
        """Test the 'save' and 'reload' methods of FileStorage"""
        key = self.base_model.__class__.__name__ + "." + self.base_model.id
        # Add an object to the storage, save it to a file, and reload it
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        
        new_storage = FileStorage()
        new_storage.reload()
        # Check if the reloaded object is the same as the original object
        self.assertTrue(key in new_storage.all())
        reloaded_model = new_storage.all()[key]
        self.assertEqual(reloaded_model.to_dict(), self.base_model.to_dict())

if __name__ == '__main__':
    unittest.main()
