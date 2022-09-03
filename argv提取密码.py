import sys,pyperclip

PASSWORD={'Email':'lyz23451','thebat':'10059299lzy','EC':'Liuyang@0906','CD':'10059299@Lzy'}

if len(sys.argv) < 2:
    print('正确的使用方法：PYTHON.exe 111.py 账户名称')
    sys.exit()

else:
    account_name = sys.argv[1]
    if account_name in PASSWORD:
        keys = PASSWORD[account_name]
        pyperclip.copy(keys)
print('账户名：{}'.format(account_name),'密码： {}'.format(keys))

