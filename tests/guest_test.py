import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Adam", 40.00)

    def test_guest_name(self):
        self.assertEqual("Adam", self.guest.name)

    def test_guest_wallet(self):
        self.assertEqual(40, self.guest.wallet)
    