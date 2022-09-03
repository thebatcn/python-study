from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import time

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
        '(KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
        #加入请求头

def get_info(url):#定义获取信息的函数 
        wb_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        ranks = soup.select('span.pc_temp_num')
        titles = soup.select('div.pc_temp_songlist>ul>li>a')
        times =soup.select('span.pc_temp_tips_r>span')

        for rank,title,time in zip(ranks,titles,times):
                data = {'rank':rank.get_text().strip(),
                        'singer':title.get_text().strip().split('-')[1],
                        'song':title.get_text().split('-')[0].strip(),
                        'time':time.get_text().strip()}
                         #通过split获取歌手和歌曲信息

                # print('rank: ',rank.get_text().strip(),"singer: ",title.get_text().strip().split('-')[1],'song: ',title.get_text().split('-')[0],
                #         'time: ',time.get_text().strip())

                print(data)     #获取爬虫信息并安字典格式打印

if __name__== '__main__':
        urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)] #构造多页URL

        for url in urls:
                get_info(url) #循环调用 get_info(url)函数
                time.sleep(1) #睡眠1秒

# print(type(headers))
# print('\n',headers)
# print(headers['User-Agent'])