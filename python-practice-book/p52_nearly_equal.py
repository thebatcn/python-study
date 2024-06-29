# # 引入自定义的突变函数库 p51_mutate
# import p51_mutate

# # 定义一个函数nearly_equal，用于判断两个字符串是否接近相等（即一个字符串是否可以通过单字符突变得到另一个）
# def nearly_equal(str1, str2):
#     # 使用p51_mutate库中的mutate函数生成str2的所有可能单字符突变的集合
#     # 然后检查str1是否在这个突变集合中
#     if str1 in p51_mutate.mutate(str2):
#         # 如果str1可以通过str2的单字符突变得到，则返回True
#         return True
#     else:
#         # 否则，返回False
#         return False

# # 测试函数nearly_equal
# # 下面的打印语句将测试几个字符串对，并输出它们是否满足“接近相等”的条件
# print(nearly_equal('python', 'perl'))  # 示例：检查'python'和'perl'是否可以通过单字符突变相互转换
# print(nearly_equal('perl', 'pearl'))   # 示例：检查'perl'和'pearl'的情况
# print(nearly_equal('python', 'jython')) # 示例：检查'python'和'jython'的情况
# print(nearly_equal('man', 'woman'))     # 示例：检查'man'和'woman'的情况


def nearly_equal(s1, s2):   #根据AI结果修改。
    if abs(len(s1) - len(s2)) > 1:  # 字符长度相差大于2，肯定满足。
        return False

    diff = 0
    # spacing = 0
    if len(s1) == len(s2):  # 字符长度一样的情况，逐个比较，差异大于，不满足。
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return True
    short_length = min(len(s1), len(s2))
    short_str, long_str = (s2, s1) if len(s1) > len(s2) else (s1, s2)

    for i in range(
        short_length
    ):  # 字符相差一位的，先分辩出字符长短，根据短字符来比较。比较找到不同点，长字符后移动一位，然后继续比较。差异大于1不满足，否则满足条件。
        if short_str[i] != long_str[i + diff]:
            diff += 1
            # spacing += 1
        if diff > 1:
            return False
    return True


print(nearly_equal("python", "perl"))  # False
print(nearly_equal("perl", "pearl"))  # True
print(nearly_equal("python", "jython"))  # True
print(nearly_equal("main", "man"))  # False
