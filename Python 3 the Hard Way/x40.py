class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#    def count_letters(self, lyrics, character):
#        return lyrics.count(character)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

my_song = Song(["What does the billboard say?",
                "Come and play! Come and play!",
                "Forget about the moment!"])

a1 = Song("Freedom")

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


#QUESTION: Classa length hesaplama methodu nasil ekleriz?