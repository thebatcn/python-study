#未编写完成
def anagrams(words):
    """To find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat, 'ate' and 'tea' are anagrams."""
    result = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                if not result:
                    result.append([words[i], words[j]])
                else:
                    found = False
                    for group in result:
                        if words[i] in group:
                            group.append(words[j])
                            found = True
                            break
                    if not found:
                        result.append([words[i], words[j]])
    return result

# 示例：
words_list = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
print(anagrams(words_list))