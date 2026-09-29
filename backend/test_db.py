import pymysql

passwords = ["jaikeerthi07a", "JAIKEERTHI07A", "jaikeerthi@07a", "Jaikeerthi@07a", "Jaikeerthi@07A", "root", "password", "admin"]
users = ["root", "jaikeerthi", "Jaikeerthi"]

with open("results.txt", "w", encoding="utf-8") as f:
    for u in users:
        for pwd in passwords:
            try:
                conn = pymysql.connect(host='localhost', user=u, password=pwd)
                f.write(f"SUCCESS with user: {u}, password: {pwd}\n")
                with conn.cursor() as cursor:
                    cursor.execute("SHOW DATABASES;")
                    dbs = [row[0] for row in cursor.fetchall()]
                    f.write(f"Databases: {dbs}\n")
                conn.close()
                break
            except Exception as e:
                pass
