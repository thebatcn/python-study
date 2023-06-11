# 输入2个数字和运算符，计算并返回结果

def Addition(a, b):
    result = a + b
    print("结果等于：{}".format(result))
    return result


def Subtraction(a, b):
    result = a - b
    print("结果等于：{}".format(result))
    return result


def Multiplication(a, b):
    result = a * b
    print("结果等于：{}".format(result))
    return result


def Division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为零")
    print("结果等于：{}".format(result))
    return result


def main():
    print("*"*60)
    print("*"+("输入两个数字进行运算".center(48)+"*"))
    print("*"+" "*58+"*")
    print("*"+"首先分别输入运算的2个数字".center(46)+"*")
    print("*"+"然后输入运算符".center(51)+"*")
    print("*"*60)

    try:
        first_num = float(input("请输入第一个数字： "))
        operators = input("请输入运算符号： ")
        second_num = float(input("请输入第二个数字： "))
    except:
        print("输入错误。")
        return None

    match operators:
        case "+":
            Addition(first_num, second_num)
        case "-":
            Subtraction(first_num, second_num)
        case "*":
            Multiplication(first_num, second_num)
        case "/":
            Division(first_num, second_num)
        case _:
            print("输入的运算符不支持。")


if __name__ == "__main__":
    main()
