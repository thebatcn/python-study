#time.sleep()运行卡死
from cgitb import html
import imp
from time import sleep
from turtle import title
import requests
from lxml import etree
import xlwt
import time

all_info_list = []

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'}

def get_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//*[@id="book-img-text"]/ul/li')
    print('infos\n',infos)
   
    for info in infos:
        title = info.xpath('div[2]/h2/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        stytle_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        stytle_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        stytle = stytle_1 + '-' + stytle_2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        word = info.xpath('div[2]/p[3]/span/span/text()')[0].strip('万字')
        info_list =[title,author,stytle,complete,introduce,word]
        all_info_list.append(info_list)

        # time.sleep(1)
        
        # print(type(info_list))
        # print(info_list)

        # print(all_info_list)
if __name__ == '__main__':
    urls = ["https://www.qidian.com/all/page{}/".format(str(i)) for i in range(1,6)]

    # urls = ['https://www.qidian.com/all/page1','https://www.qidian.com/all/page2',
    #         'https://www.qidian.com/all/page3','https://www.qidian.com/all/page4',
    #         'https://www.qidian.com/all/page5'
    #         ]

    for url in urls:
        get_info(url)

    header = ['Title','Author','Stytle','Complete','Introduce','Word']
    
    book = xlwt.Workbook(encoding='utf-8')#创建工作簿
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i,j,data)
            j += 1
        i += 1
    book.save("xiaoshuo.xls")