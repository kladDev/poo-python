import pymysql.cursors

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='kelly1419',
                                database='banco_poo', 
                                charset='utf8mb4', 
                                cursorclass=pymysql.cursors.DictCursor)
