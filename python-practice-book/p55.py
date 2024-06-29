# #未编写完成
# def anagrams(words):
#     """To find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat, 'ate' and 'tea' are anagrams."""
#     result = []
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if sorted(words[i]) == sorted(words[j]):
#                 if not result:
#                     result.append([words[i], words[j]])
#                 else:
#                     found = False
#                     for group in result:
#                         if words[i] in group:
#                             group.append(words[j])
#                             found = True
#                             break
#                     if not found:
#                         result.append([words[i], words[j]])
#     return result

# 示例：
words_list = ['eat', 'ate', 'done', 'tea', 'soup', 'node','heart', 'earth', 'hater', 'rathe','have','glove']
# words_list = ['eat', 'ate', 'have','glove']
word_dict = {}
# print(anagrams(words_list))
def anagrams(word_list):
    result_no = []
    result_have=[]
    new_list =[''.join(sorted(w)) for w in words_list]
    # print(new_list)
    """ 版本1
    # for w in words_list:
    #     sort_w ="".join(sorted(w))
    #     word_dict.setdefault(sort_w, []).append(w)
    #     if  sort_w in new_list and new_list.count(sort_w) > 1:
    #         result_have.append(w)
    #     else:
    #         result_no.append(w)
    # return result_no, result_have"""
    for w in words_list:
        sort_w ="".join(sorted(w))
        word_dict.setdefault(sort_w, []).append(w)
    return word_dict.values()
#目前实现分辨单词是否anagrams，并且输出的功能。
#改进版，实现用字典储存结果，根据单词长度分别储存
#最终版，字典储存，能根据构成字母类型一致的，储存在一组。长度可以作为排行依据。
# print(words_list)
print(anagrams(words_list))
"""for w in words:  word_dict"""