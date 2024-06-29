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
word_dict = {}
# print(anagrams(words_list))
result_no = []
new_list =[''.join(sorted(w)) for w in words_list]
print(new_list)

for w in words_list:
    if sorted(w) in new_list:
        continue
    else:
        result_no.append(w)
        words_list.remove(w)

print(words_list)
print(result_no)
"""for w in words:  word_dict"""