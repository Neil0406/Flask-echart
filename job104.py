import pymysql
import pandas as pd
from random import choice

MYSQL_HOST = 'localhost'
MYSQL_DB = 'neildb'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

def connect_mysql():  #連線資料庫
    global connect, cursor
    connect = pymysql.connect(host = MYSQL_HOST, db = MYSQL_DB, user = MYSQL_USER, password = MYSQL_PASS,
            charset = 'utf8', use_unicode = True)
    cursor = connect.cursor()

def job104():
    connect_mysql()
    df = pd.read_sql('SELECT * FROM job104', con = connect) #使用connect指定的Mysql獲取資料
    data = df.to_dict('recode')       #總共數量約18xx工作


    result = []               #result 有資料的總比數約9xx筆
    for i in data:
        if i['工具'] != None:
            p = i['工具'].split('/')
            result.append(p)
    r = []
    for j in range(len(result)):
        for i in result[j]:
            r.append(i)

    r2 = []    #關鍵字全部出現的list 約48xx
    for i in r:
        r2.append(i.replace(' ',''))

    r3 = []    #全部分類（不包含重複出現）
    for i in r2:
        if i not in r3:
            r3.append(i)

    list1 = ['hadoop', 'Linux', 'MySQL', 'HTML', 'CSS', 'Django', 'AJAX', 'PHP', 'JavaScript', 'jQuery', 'Java', 'Github', 'SQL', 'Git', 'Tableau', 'Hive'] #自定義關鍵字

    num = {}  #最後計算結果

    for i in list1:
        num[i] = 0
    for i in num:
        for j in r2:
            if j == i:
                num[i] = num[i] + 1

    r1 = []    #與list1 對應總數
    for i in num:
        r1.append(num[i])
 
   
    
    return list1, r1






 