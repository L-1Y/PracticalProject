def printGoodsList(ilt):
    
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    sql = "insert into jindong(number,price,title) VALUES (%s,%s,%s)"
    for i in range(len(ilt)):
        count+=1
        ilt1=ilt[i]
        print(format(count,ilt1[0],ilt1[1]))
        cur.execute(sql,(count,ilt1[0],ilt1[1]))#执行数据库插入操作
    db.commit()
    print('插入成功')