import pymysql
def create():
    conn = pymysql.connect(host='localhost', user='root', password='jaikeerthi07a')
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS royal_bikes;")
    conn.commit()
    conn.close()
if __name__ == '__main__':
    create()
