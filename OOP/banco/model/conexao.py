import pymysql.cursors

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='banco_poo', 
                                charset='utf8mb4', 
                                cursorclass=pymysql.cursors.DictCursor)
