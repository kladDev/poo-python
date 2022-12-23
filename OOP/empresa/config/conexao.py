import pymysql.cursors

def conectar():
    connection = pymysql.connect(host='localhost', 
                                    user='root', 
                                    password='kelly1419',                          
                                    database='prova03',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    return connection
