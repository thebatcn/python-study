import re
from base64 import decode
from dataclasses import replace
from pprint import PrettyPrinter
from unittest import result

import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
          }
res = requests.get('http://www.doupoxs.com/doupocangqiong/1.html',headers=headers)

res.encoding = 'utf-8'
results = etree.HTML(res.text)

a = results.xpath('//a/text()')
href = results.xpath('//a[@href="/doupocangqiong/1.html"]/text()')
print(href)

with open('d:/dddd.txt','a+',encoding='utf-8') as fp:
    for h in href:
        fp.write(h+'\n') 
 

print(href)
""" selector = etree.HTML(res.text)
print(type(selector)) """
"""
x_paths = ['//*[@id="s-top-left"]/a[{}]/text()'.format(str(i)) for i in range(1,8)]
rrs = []

for x_path in x_paths:
    rr = selector.xpath(x_path)
    print(rr)
    rrs.append(rr)
print('\n\n',rrs)


 """
#etree.tostring()