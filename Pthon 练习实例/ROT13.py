"""
    (ord(char) - base + offset) % 26 以循环，或者按26为进制
    可以把问题分解，起点+循环（进制），base + (X % 26)
"""


def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
                offset = 13
            else:
                base = ord('A')
                offset = 13
            rotated = (ord(char) - base + offset) % 26 + base
            result += chr(rotated)
        else:
            result += char
    return result


# 示例用法
message = "Hello, World!"
encrypted_message = rot13(message)
decrypted_message = rot13(encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

#---------------------------------------------------------#
class Lesson1_1:
  @staticmethod
  def decimalToBinary(decimalSource):
    # 使用内置函数bin()将十进制数转换成二进制字符串
    return bin(decimalSource)[2:]

  @staticmethod
  def binaryToDecimal(binarySource):
    # 使用内置函数int()将二进制字符串转换成十进制数
    return int(binarySource, 2)
# 十进制转换成二进制
print(Lesson1_1.decimalToBinary(10))  # output: 1010

# 二进制转换成十进制
print(Lesson1_1.binaryToDecimal("1010"))  # output: 10

#---------------------------------------------------------#