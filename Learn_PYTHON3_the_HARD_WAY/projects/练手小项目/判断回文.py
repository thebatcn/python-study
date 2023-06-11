#偶数不是
#奇数。判断第一个和最后一个，第二个和倒数第二个。。。依次判断，都相等是回文。

def ispalindrome(s):
    s = s.lower()
    if len(s)%2 == 0:
        return False
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
    

def main():
    string = input("输入一个字符串： ")
    print(ispalindrome(string))

if __name__ == "__main__":
    main()

