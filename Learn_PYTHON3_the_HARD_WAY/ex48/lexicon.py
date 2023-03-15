directions = ['north', 'west', 'south', 'east',
              'down', 'up', 'right', 'left', 'back']
verb = ['go', 'stop', 'kill', 'eat']
modifiers = ['the', 'in', 'of', 'from', 'at', 'it']
noun = ['door', 'bear', 'princess', 'cabinet']
nums = [num for num in range(0, 101)]  # 0-100的数字
vocabulary = [directions, verb, modifiers, noun, nums]
# stuff = input('> ').split()
# 转换其中的数字字符类型为int


class Lexicon():

    def __init__(self, stuff) -> None:
        self.stuff = stuff.strip().split()
        

    def scan(self):
        self.wordtuple = []
        self.words = []
        for a in self.stuff:
            try:
                self.words.append(int(a))
            except ValueError:
                self.words.append(a)
        # print('stuff: ', stuff)
        # print('words: ', words)
        for word in self.words:  # 多if 条件判断，应该加continue.
            if word in directions:
                self.wordtuple.append(('direction', word))
                continue
            if word in verb:
                self.wordtuple.append(('verb', word))
                continue
            if word in modifiers:
                self.wordtuple.append(('modifiers', word))
                continue
            if word in noun:
                self.wordtuple.append(('noun', word))
                continue
            if word in nums:
                self.wordtuple.append(('nums', word))
                continue
            else:
                self.wordtuple.append(('errors', word))
                continue
        # print(self.wordtuple)
        return self.wordtuple


# def lexicon_scan(stuff):
#     stuff = stuff.strip().split()
#     for a in stuff:
#         try:
#             words.append(int(a))
#         except ValueError:
#             words.append(a)
#     # print('stuff: ', stuff)
#     # print('words: ', words)
#     for word in words:  # 多if 条件判断，应该加continue.
#         if word in directions:
#             wordtuple.append(('direction', word))
#             continue
#         if word in verb:
#             wordtuple.append(('verb', word))
#             continue
#         if word in modifiers:
#             wordtuple.append(('modifiers', word))
#             continue
#         if word in noun:
#             wordtuple.append(('noun', word))
#             continue
#         if word in nums:
#             wordtuple.append(('nums', word))
#             continue
#         else:
#             wordtuple.append(('errors', word))
#             continue
#     return wordtuple


# a = lexicon_scan(' I GO 8 it')
# print(a)

# a = Lexicon('go into the door')
# print(a.scan())
