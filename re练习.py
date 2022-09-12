#re正则表达式   \Z表示文本末尾  $行末尾 
#多行模式  ^ $每行首 末尾都匹配，\Z任然只匹配文本末尾
#使用非贪婪的限定符 *? 、 +? 、 ?? 或 {m,n}? ，匹配为尽可能 少 的文字


import re

cmpl = re.compile(r'love(?='you')'.flags=I)
re.match(r,str,re.IGNORECASE,re.MULTILINE)p 
str.replace()
re.sub()