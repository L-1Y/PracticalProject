import pymysql
from bs4 import BeautifulSoup
import requests
import re
 
db = pymysql.connect(host="localhost", user="root", password="123", database="jindong",charset="utf8")#连接数据库(地址,用户名，密码，数据库名)
print("数据库连接成功")
cur = db.cursor()#取游标 
 
def getHTMLText(url):
    pass
 
def parsePage(ilt,html):
    try:
        soup=BeautifulSoup(html,'html.parser')
        plt=soup.find_all('div',attrs={'class':'p-price'})#提取所有class为p-price的标签

        tlt=soup.find_all('div',attrs={'class':'p-name p-name-type-2'})
        title=re.findall(r'<em>.*</em>',str(tlt))#需要提取的数据在em标签中，因此用此标签定位
        price=re.findall(r'<i>\d*\.\d*</i>',str(plt))#需要提取的数据在i标签中，因此用此标签定位

        for i in range(len(title)):
            price[i]=re.sub(r'<[^>]+>',"",str(price[i]),re.S)#清除标签
            title[i]=re.sub(r'<[^>]+>',"",str(title[i]),re.S)#清除标签
            ilt.append([price[i],title[i]])
    except:
        print("")
        
def printGoodsList(ilt):
    
    pass
 
def main():
    pass
    
main()