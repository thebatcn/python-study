#计算输入的字符串中，每一种字符的个数。fad

def count_char(string):
    char_dict ={}

    for char in string:
        #The function count_char is using the keys() method unnecessarily, which slows down the program.
        #  Instead, we can use in to check for the key's existence in the dictionary.
        # if char not in char_dict.keys():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def main():
    string = input("输入字符串，统计字符个数： ")
    print(count_char(string))

if __name__ == "__main__":
    main()