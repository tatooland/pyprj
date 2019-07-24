import pymssql
import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import re
import time
import datetime

def job():
    #设置接口地址
    url = "http://www.xxxx.xx/webservice"
    # 连接数据库
    conn = pymssql.connect(host='127.0.0.1', 
                        user='DESKTOP-2BTBN2L\GuoPei', 
                        password='820526', 
                        database='Card3500',
                        charset='utf8')
    #通过打印判断程序是否连上数据库
    print(conn)
    #进行数据库select操作
    cursor = conn.cursor()
    sql = "select * from table1"
    cursor.execute(sql)
    #执行sql语句后数据会按照row的方式存入cursor中，通过循环可以把数据读出，row指代1条数据，其中的属性可以通过row[0], row[1]来进行具体取值
    for row in cursor:
        print(row)
        #将数据库查询出的数据组装成json格式
        data = {
            'content': row[0]
        }
        #把data先做字符串传唤并通过post的方式发送到接口url上
        r = requests.post(url, data=json.dumps(data))
        #答应接口的返回数据
        print(r.text)
    conn.close()



def main():
    scheduler = BlockingScheduler()
    #1小时执行一次，
    scheduler.add_job(func=job, trigger='cron', hour=1)
    scheduler.start()


main()

