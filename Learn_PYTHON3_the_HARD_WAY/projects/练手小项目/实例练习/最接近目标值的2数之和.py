# nums = [1, 3, 5, 7, 2, 4, 9, 8, 11, -8]
# odd = []
# even = []

# 判断数字是不是奇数
# for num in nums:
#     if num & 1:     
#         (odd.append(num))
#     else:
#         (even.append(num))
# print(odd)
# print(even)

# odd1 = [i for i in nums if i % 2 != 0]
# print(odd1)

# 问题描述
# 给出一个数组，在数组中找到2个数，使得它们的和最接近但不超过目标值，返回它们的和。
# ．问题示例
# 输入target = 15，array = [1，3，5，11，7]，输出14，11+3 = 14。输入target = 16和array = [1，3，5，11，7]，输出16，11+5 = 16。


# 递归求数组和
def sum_list(List):
    if not List:
        return 0
    return (List[0] + sum_list(List[1::]))

# 演示每一项数字与后面数字相加
# for i in range(len(array)-1):
#     print(sum_list(array[i::]))


# print(sum_list(nums))

array = [1, 3, 5, 7, 11, 6, 8]
targe = 15
every_sum = {}
for i in range(len(array)-1):  # 可以用于非递归求数组和
    n = i + 1
    while n < len(array):
        a_sum = (array[i] + array[n])
        difference = targe - a_sum
        if difference >= 0:
            every_sum[str(array[i]) + "+" + str(array[n])] = difference
        n += 1
    # every_sum.append("/n")

print(every_sum)

sorted_dict = dict(sorted(every_sum.items(), key=lambda x: x[1]))
print(sorted_dict)

n = 0
for k in sorted_dict.keys():
    print(k)
    if n >= 1:
        break
    n += 1

# 用双指针解

def find_closest_sum(nums, target):
    nums.sort()  # 对数组进行排序
    left = 0
    right = len(nums) - 1
    closest_sum = float('-inf')  # 初始化最接近目标值的和为负无穷大

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum <= target:
            closest_sum = max(closest_sum, curr_sum)
            left += 1
        else:
            right -= 1

    return closest_sum

# 示例
nums = [4, 8, 7, 1, 3]
target = 6
result = find_closest_sum(nums, target)
print(result)  # 输出：5
