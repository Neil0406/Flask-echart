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

def wei():
    connect_mysql()
    df = pd.read_sql('SELECT * FROM 緯育', con = connect) #使用connect指定的Mysql獲取資料
    data = df.to_dict('recode')


    for i in data:
        if i['price'] != '免費' and i['price'] != None:
            i['price'] = int(i['price'].replace('NT$','').replace(',',''))
        else:
            i['price'] = 0

    d = {}
    for i in data:
        d[i['category']] = ''

    title_num = []   #每種類課程總和 [45, 74, 10, 12, 45, 5, 25]
    for j in d:
        t = []
        for i in data:
            count = 0
            if i['category'] == j:
                count += 1
                t.append(count)
        title_num.append(sum(t))
                
    title = []     #課程分類              ['網站前端', '網站後端', '物聯網 IOT', '手機應用', '數據分析', '遊戲開發', '微軟應用']
    price = []     #每個種類課程的"價格"總和 [109686, 281049, 21090, 35899, 211530, 15860, 151690]
    free = []      #免費課程的數量          [7, 13, 4, 1, 11, 0, 0]

    for k in d :
        title.append(k)
        p = []
        f = []
        count = 0
        for i in data:
            if i['category'] == k and i['price'] != 0:
                p.append(i['price'])
            if i['category'] == k and i['price'] == 0:
                count =+ 1
                f.append(count)
        price.append(sum(p))
        free.append(sum(f))

    #price / (title_num - free)  計算平均 （扣掉免費課程的平均）

    avg = []   # [2886, 4607, 3515, 3264, 6221, 3172, 6068]
    for i in range(len(title)):
        p = price[i] / (title_num[i] - free[i])
        avg.append(int(f'{p:.0f}'))
    mylist = zip(title, avg)
    return title, avg, mylist

