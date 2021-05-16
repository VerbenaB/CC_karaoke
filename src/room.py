class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def admit_guest(self, guest):
        self.guests.append(guest)

    def checkout_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
        