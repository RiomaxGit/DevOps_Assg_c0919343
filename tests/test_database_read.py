import unittest
from pymongo import MongoClient


class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("Mongo DB string")  # Used for local testing. Removed it.

    def test_ping(self):
        """Test MongoDB connection using ping."""
        try:
            self.client.admin.command('ping')
            connected = True
        except Exception:
            connected = False
        self.assertTrue(connected)

if __name__ == "__main__":
    unittest.main()
