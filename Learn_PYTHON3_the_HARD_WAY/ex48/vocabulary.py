directions = ['north', 'west', 'south', 'east', 'down', 'up', 'right', 'left']
wordtuple = []

stuff = input('> ').split()

for word in stuff:
    if word in directions:
        wordtuple.append(('direction', word))

print(wordtuple)
