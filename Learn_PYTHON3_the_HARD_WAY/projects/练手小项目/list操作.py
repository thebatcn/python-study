# 实现对一个整数列表的排序、去重和查找最大/最小值的功能

class list_operate:

    def __init__(self, a_list) -> None:
        self.a_list = a_list

    def l_sort(self, key=None):
        self.a_list.sort()
        return self.a_list

    def find_max(self):
        return max(self.a_list)
    
    def find_min(self):
        return min(self.a_list)

    def deduplicate(self):
        return list(set(self.a_list))

ab = ['a', 'b', '3', 'e','a','4','b']
a1 = list_operate(ab)
print(a1.l_sort())
print(a1.find_max())
print(a1.deduplicate())