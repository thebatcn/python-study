#re hs方法
#match search  fullmatch  findall finditer  sub  spilt

#match fullmatch 从字符串首字符检测，匹配返回结果，不匹配返回NONE。字符串第二个起能匹配都返回NONE。fullmatch是完全匹配意思，模式和字符串一样返回结果，不一样返回NONE。

#search 可以从字符串任意位置匹配，匹配返回结果，不匹配返回NONE。只匹配找的一个返回。

#findall 返回匹配的所有值，返回列表。空匹配也返回列表。

#finditer 返回所有非重复匹配，返回一个迭代器。空匹配包含在结果。

#sub(模式，替换的，检测的字符串) 参数:题换的可以是字符，也可以是函数。函数的情况有参数(名字任意)，参数是matchobj，及前面模式匹配的结果。

#split(pattern, string, maxsplit=0, flags=0)用 pattern 分开 string 。
#如果在 pattern 中捕获到括号，那么所有的组里的文字也会包含在列表里。如果 maxsplit 非零，
#最多进行 maxsplit 次分隔， 剩下的字符全部返回到列表的最后一个元素。
#re.split(r'(\W+)', 'Words, words, words.')
#**(\w+)pattern 中捕获到括号**？
#如果分隔符里有捕获组合，并且匹配到字符串的开始，那么结果将会以一个空字符串开始。对于结尾也是一样

#
#>>> re.split(r'(\W+)', '...words, words...')
#['', '...', 'words', ', ', 'words', '...', '']



import re

m = re.findall(r'-{1,2}','hh----jj-k')

print(type(m))
print(m)

def fct(mobj):
    if mobj.group(0) == '-':return '~'
    else:
        return '-'


s = re.sub(r'-{1,2}',fct,'hh----jj-k')
print(s)
