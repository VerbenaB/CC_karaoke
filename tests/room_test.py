import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Blue room", 4)
        self.guest_1 = Guest("Adam", 40.00)
        self.guest_2 = Guest("Bekah", 50.00)
        self.guest_3 = Guest("Matthew", 60.00)
        self.song_1 = Song("Malo", "Spanish pop")
        self.song_2 = Song("Era", "Dream pop")
        self.song_3 = Song("Djadja", "Electronic")

    def test_room_name(self):
        self.assertEqual("Blue room", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)

    def test_room_admit_guest(self):
        self.room_1.admit_guest(self.guest_1)
        self.assertEqual([self.guest_1], self.room_1.guests)

    def test_room_checkout_guest(self):
        self.room_1.admit_guest(self.guest_1)
        self.room_1.admit_guest(self.guest_2)
        self.room_1.admit_guest(self.guest_3)
        self.room_1.checkout_guest(self.guest_2)
        self.assertEqual([self.guest_1, self.guest_3], self.room_1.guests)

    def test_room_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual([self.song_1], self.room_1.songs)

        

    