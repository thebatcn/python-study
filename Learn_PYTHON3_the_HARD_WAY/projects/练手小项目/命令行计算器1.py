# #准备用eval()函数实现
# import string
# arithmetic_operator = "+, -, *, /, ., (, ) "
# digits = string.digits
# def Cal(strs):
#     for str in strs:
#         if str not in (arithmetic_operator + digits):
#             print("输入的不是正确的算式。")
#             return None
#     try:
#         print(eval(strs))
#     except SyntaxError:
#         print('请输入合格的算式。')
#         return None

# def main():
#     formula = input("输入一个算式进行计算： ")
#     Cal(formula)

# if __name__ == "__main__":
#     main()

# 下面是chatgpt修改版

# import string

# # Define valid arithmetic operators
# arithmetic_operators = "+-*/()"

# # Define valid digits
# digits = string.digits

# # Check if input string is a valid arithmetic expression
# def Cal(strs):
#     for char in strs:
#         if char not in (arithmetic_operators + digits):
#             print("输入的不是正确的算式。")
#             return False
#     try:
#         print(eval(strs))
#     except SyntaxError:
#         print('请输入合格的算式。')
#         return False
#     return True

# def main():
#     # Prompt user for input
#     formula = input("输入一个算式进行计算： ")
    
#     # Check if input is a valid arithmetic expression
#     if Cal(formula):
#         print("计算结束。")

# if __name__ == "__main__":
#     main()

def calculate_equation(equation):
    valid_operators = ["+", "-", "*", "/", ".", "(", ")"]
    for char in equation:
        if char not in valid_operators and not char.isdigit():
            print("Invalid equation. Please enter a correct equation.")
            return None
    try:
        result = eval(equation)
        print(result)
    except:
        print("Invalid equation. Please enter a correct equation.")
        return None

def main():
    equation = input("Enter an equation to calculate: ")
    calculate_equation(equation)

if __name__ == "__main__":
    main()
