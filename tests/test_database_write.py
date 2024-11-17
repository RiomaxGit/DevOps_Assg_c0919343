import unittest
from pymongo import MongoClient

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("Mongo DB string")  # Used for local testing. Have removed it
        self.db = self.client.shop_db
        self.collection = self.db.products

    def test_insert_document(self):
        """Test inserting a document into MongoDB and verifying it."""
        test_document = {"name": "Test Product", "tag": "Test Tag", "price": 1.99}
        result = self.collection.insert_one(test_document)
        self.assertIsNotNone(result.inserted_id)
        found_document = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(found_document)
        self.assertEqual(found_document['name'], "Test Product")

if __name__ == "__main__":
    unittest.main()
