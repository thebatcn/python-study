'''
测试xpath语法
//li['ul[@class="red"]'/text() 为什么是[]空列表
'''

from cgitb import html
from unittest import result
from lxml import etree

text ='''
    <html>

<head>
    <meta charset="utf-8">
    <title>flower</title>
</head>

<body>
    <h1>我的第一个HTML页面</h1>
    <p>我的第一个段落。</p>

    <div>
        <ul>
            <li price = 37>'TEST Red'
              <h1>red flowers</h1>
            </li>
            <li price = 32>'YELLOW'
                <h2>yellow flowers item</h2>
            </li>
            <li class='white'>'WHITE'
              <h3>white flowers</h3>
            </li>
            <li class='black'>'BLACK'
                <h4>black flowers</h4>
            </li>
            <li class='blue'>'BLUE'
                <h5>blue flowers</h5>
            </li>
            <li class="item-0"><a href="link1.html">第一个</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
        </ul>
        <uk>
            <li class='red'>' Red in uK'
                <h1>red flowers</h1>
               
            </li>
            <li class='yellow'>'YELLOW in uK'
                <h2>yellow flowers item</h2>
            </li>
            <li class='white'>'WHITE in uK'
              
                <h3>white flowers</h3>
            </li>
            <li class='black'>'BLACK in uK'
                <h4>black flowers</h4>
            </li>
            <li class='blue'>'BLUE in uK'
                <h5>blue flowers</h5>
            </li>
        </uk>
    </div>

</body>

</html>
    '''
html =etree.HTML(text,etree.HTMLParser())
result =etree.tostring(html)

#r_path = html.xpath('//*/text()') #找属性时，必须要先指定在哪个节点？
#r1_path = html.xpath('../text()')

r1 = html.xpath('//li[@class="item-0"]/a/text()') # 第一个
r2 = html.xpath('//a[@href="link1.html"/../@class') # item-0
#r3 = html.xpath('//@href="link1.html"/partent::*/@class')  # item-0

print('r1: {}\n'.format(r1))

#print(r1_path)

