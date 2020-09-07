import pymysql
import pandas as pd

MYSQL_HOST = 'localhost'
MYSQL_DB = 'neildb'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

def connect_mysql():  #連線資料庫
    global connect, cursor
    connect = pymysql.connect(host = MYSQL_HOST, db = MYSQL_DB, user = MYSQL_USER, password = MYSQL_PASS,
            charset = 'utf8', use_unicode = True)
    cursor = connect.cursor()

def six():
    connect_mysql()
    df = pd.read_sql('SELECT * FROM 六角學院', con = connect) #使用connect指定的Mysql獲取資料
    data = df.to_dict('recode')

    class_name = []  #課程名稱
    price = []      #價格
    price_dis = []   #折扣後
    people = []     #參與人數

    for i in data:
        #課程名稱
        d = i['title'].replace('\n', '').replace('限時優惠','')
        d2 = d.split()
        w = ''
        i['title'] =  w.join(d2)
        class_name.append(i['title'])
        #價格
        p = int(i['price'].replace('原價：',''))
        price.append(p)
        #折扣後
        dis = i['price_dis'].replace('折扣：NT$ ','')
        dis2 = int(dis.replace(',',''))
        price_dis.append(dis2)
        #參與人數    因為有空值所以捕0
        try:
            people.append(int(i['peoples'].replace('人參與', '')))    
        except:
            people.append(0)
    return class_name, price, people

    

