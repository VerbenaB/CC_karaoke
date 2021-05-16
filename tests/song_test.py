import unittest
from src.song import Song 

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Malo", "Spanish pop")

    def test_song_name(self):
        self.assertEqual("Malo", self.song.name)
    
    def test_song_genre(self):
        self.assertEqual("Spanish pop", self.song.genre)

    def test_song_duration(self):
        self.assertEqual(3.47, self.song._duration)
