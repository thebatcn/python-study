import xlwt
import webbrowser

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')

sheet.write(0,0,'Python')
sheet.write(1,1,'love')
book.save('Testxls.xls')

htmls = ['https://www.qidian.com/all/page{}/'.format(str(i)) for i in range(1,6)]

print(type(htmls))

print(htmls)

open_html = webbrowser.open(htmls[4])