import re

text = 'Ronald Heathmore: 892.345.3428 436 Finley Avenue'

print(text)

poem = '12345，22358。guijj,hiiim.'
print(re.split('[,.，。]',poem))

print(re.split(r'(:*\s)' ,text,3))#()分组，分隔符返回在结果列表中
print(re.split(':? ' ,text,4))#不加？或者*，后面空白识别不了
#(?:....不捕获不显示....内容，....代表模式)