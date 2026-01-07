import unittest
import requests

BASE_URL = "http://localhost:8000"

class TestAPIs(unittest.TestCase):
    def test_list_servers(self):
        response = requests.get(f"{BASE_URL}/servers")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
