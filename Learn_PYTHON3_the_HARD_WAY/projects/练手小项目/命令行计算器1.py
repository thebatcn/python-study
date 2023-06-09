#准备用eval()函数实现
import string
arithmetic_operator = "+, -, *, /, ., (, ) "
digits = string.digits
def Cal(strs):
    for str in strs:
        if str not in (arithmetic_operator + digits):
            print("输入的不是正确的算式。")
            return None
    try:
        print(eval(strs))
    except SyntaxError:
        print('请输入合格的算式。')
        return None

def main():
    formula = input("输入一个算式进行计算： ")
    Cal(formula)

if __name__ == "__main__":
    main()