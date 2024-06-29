import os

def word_frequency(words):
    """Returns frequency of each word given a list of
    words
    >>> word frequency(['a','b','a'])
    {'a':2,'b': 1)
    """

    frequency = {}

    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


# print(word_frequency('abcda'))


def read_words(filename):
    return open(filename).read().split()
    
def filetype(filename):
    """分别文件类型"""
	basename,extension = os.path.splitext(filename)
	
	file_type = {'.c':'c program file','.py':'python file','.txt':'text file'}
	
	return file_type.get(extension.lower())


def main(filename):
    print(filetype(filename))
    frequency = word_frequency(read_words(filename))
    sort_frequency = dict(sorted(frequency.items(), key=lambda item: item[1],reverse=True))
    for word, count in sort_frequency.items():
        print(word, count)
    # print(sort_frequency)
    # print(type(sort_frequency))


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
