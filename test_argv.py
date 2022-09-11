"""用法：在终端输入 python test_argv.py 参数1 参数2 ..."""

import sys

print("There are {}argv in list.".format(len(sys.argv)))
print("There are {}".format(str(sys.argv)))

