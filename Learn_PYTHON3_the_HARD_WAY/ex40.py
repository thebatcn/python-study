
# dict style
mystuff = {"apple":"I AM APPLES!"}
print(mystuff['apple'])


import mystuff

# moudle style
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = mystuff.Mystuff()
thing.apple()
print(thing.tangering)

class Song():

    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right the re"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()