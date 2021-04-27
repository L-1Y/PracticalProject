import pymysql
from bs4 import BeautifulSoup
import requests
import re
 
db = pymysql.connect(host="localhost", user="root", password="123", database="jindong",charset="utf8")#连接数据库(地址,用户名，密码，数据库名)
print("数据库连接成功")
cur = db.cursor()#取游标 
 
def getHTMLText(url):
    kv={'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'}
    try:
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        
        return r.text
    except:
        return "-1"
 
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
    
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    sql = "insert into jindong(number,price,title) VALUES (%s,%s,%s)"
    for i in range(len(ilt)):
        count+=1
        ilt1=ilt[i]
        print(tplt.format(count,ilt1[0],ilt1[1]))
        cur.execute(sql,(count,ilt1[0],ilt1[1]))#执行数据库插入操作
    db.commit()
    print('插入成功')
 
def main():
    goods='衣服'
    depth=3
    start_url='https://search.jd.com/Search?keyword='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&enc=utf-8&page='+str(i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
    
main()
