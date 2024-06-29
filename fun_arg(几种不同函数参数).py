def function(p1, /, p_k, arg_k1, *, arg_k2):
    """def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
  -----------    ----------     ----------
    |             |                  |
    |        Positional or keyword   |
    |                                - Keyword only
     -- Positional only
/ 和 * 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。关键字形参也叫作命名形参。
"""
    print(p1)
    # for v in p_k:
    # 	print(v,end = ' ')
    print(p_k)
    print(arg_k1)
    print(arg_k2)


function(134, 'a', arg_k1="abcdefg", arg_k2='[[[[]]]]')


def foo(p1, *p2, p_k):
    """*args形参后的任何形式参数只能是仅限关键字参数，即只能用作关键字参数，不能用作位置参数。"""
    print(p1)
    print(p2)
    print(p_k)


foo(234, 'a', 'b', p_k='234ab')