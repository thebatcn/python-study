from unittest import result
from lxml import etree

def test():

    text='''
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">第一个</a></li>
            <li class="item-1"><a href="link2.html">second item</a><b>添加进去的块B</b></li>
        </ul>
    </div>
    ''' 
    html=etree.HTML(text,etree.HTMLParser())
    result=html.xpath('//a[@href="link2.html"]/../@class')
    result1=html.xpath('//a[@href="link2.html"]/parent::*/@class')
    result3 = html.xpath('//a/@href') #返回属性的值

    print(result)
    print(result1)
    print(result3)

def test1():

    text1='''
    <div>
        <ul>
            <li class="aaa item-0"><a href="link1.html">第一个</a></li>
            <li class="bbb item-1"><a href="link2.html">second item</a></li>
        </ul>
    </div>
    '''
    html=etree.HTML(text1,etree.HTMLParser())
    result0=html.xpath('//li[@class="aaa"]/a/text()')  #属性名要写全
    result1=html.xpath('//li[@class="aaa item-0"]/a/text()')
    result2=html.xpath('//li[contains(@class,"aaa")]/a/text()') #属性名可以不写全

    print("result0:{} \n result0:{} \n result1:{}\n".format(result0,result1,result2))
   

def test2():
    text2='''
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">第一个</a></li>
            <li class="item-1"><a href="link2.html">second item</a><b>添加进去的块B</b></li>
        </ul>
    </div>
    ''' 
    html=etree.HTML(text2,etree.HTMLParser())

    result1 = html.xpath('//li[@class="item-1"]') #返回节点 <a href="link2.html">second item</a> 是一个list类型
    result2 = html.xpath('//li[@class="item-1"]//text()') #返回后代节点的所有text

    print('result1:{} \n result2:{}\n'.format(result1,result2))
 
def test3():        #多属性匹配
    text3='''
        <div>
            <ul>
                <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
                <li class="aaa" name="fore"><a href="link2.html">second item</a></li>
            </ul>
        </div>
        '''

    html=etree.HTML(text3,etree.HTMLParser())
    result=html.xpath('//li[@class="aaa" and @name="fore"]/a/text()')
    result1=html.xpath('//li[contains(@class,"aaa") and @name="fore"]/a/text()')

def test3():        #lxml 按序选择
    text1='''
    <div>
        <ul>
            <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
            <li class="aaa" name="item"><a href="link1.html">第二个</a></li>
            <li class="aaa" name="item"><a href="link1.html">第三个</a></li>
            <li class="aaa" name="item"><a href="link1.html">第四个</a></li> 
        </ul>
    </div>
    '''

    html=etree.HTML(text1,etree.HTMLParser())

    result=html.xpath('//li[contains(@class,"aaa")]/a/text()') #获取所有li节点下a节点的内容
    result1=html.xpath('//li[1][contains(@class,"aaa")]/a/text()') #获取第一个
    result2=html.xpath('//li[last()][contains(@class,"aaa")]/a/text()') #获取最后一个
    result3=html.xpath('//li[position()>2 and position()<4][contains(@class,"aaa")]/a/text()') #获取第三个
    result4=html.xpath('//li[last()-2][contains(@class,"aaa")]/a/text()') #获取倒数第三个


    print(result)
    print(result1)
    print(result2)
    print(result3)
    print(result4)



if __name__=='__main__':
    # print("现在是TEST,测试返回父节点的属性，使用了2种方法。\n")
    # test()
    # print("现在是TEST1，测试确定属性值，返回子节点text值。两种方法。\n")
    # test1()
    # print("现在是TEST2,测试返回后代节点所有text值\n")
    # test2()
    print('''
        有时候，我们在选择的时候某些属性可能同时匹配多个节点，
        但我们只想要其中的某个节点，如第二个节点或者最后一个
        节点，这时可以利用中括号引入索引的方法获取特定次序的节点\n''')
    test3()

    

