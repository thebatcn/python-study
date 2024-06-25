# 引入自定义的突变函数库 p51_mutate
import p51_mutate

# 定义一个函数nearly_equal，用于判断两个字符串是否接近相等（即一个字符串是否可以通过单字符突变得到另一个）
def nearly_equal(str1, str2):
    # 使用p51_mutate库中的mutate函数生成str2的所有可能单字符突变的集合
    # 然后检查str1是否在这个突变集合中
    if str1 in p51_mutate.mutate(str2):
        # 如果str1可以通过str2的单字符突变得到，则返回True
        return True
    else:
        # 否则，返回False
        return False

# 测试函数nearly_equal
# 下面的打印语句将测试几个字符串对，并输出它们是否满足“接近相等”的条件
print(nearly_equal('python', 'perl'))  # 示例：检查'python'和'perl'是否可以通过单字符突变相互转换
print(nearly_equal('perl', 'pearl'))   # 示例：检查'perl'和'pearl'的情况
print(nearly_equal('python', 'jython')) # 示例：检查'python'和'jython'的情况
print(nearly_equal('man', 'woman'))     # 示例：检查'man'和'woman'的情况