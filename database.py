import pymysql

class Mysql:
    def __int__(self,conn,cur,sql):
        self.conn = conn
        self.cur = cur
        self.sql = sql

    def connDB():
        conn = pymysql.connect(host='localhost',user='root',passwd='897570',db='study',charset='utf8')
        cur = conn.cursor()
        return conn,cur
    connDB = staticmethod(connDB)

    def exeUpdate(conn,cur,sql):
        sta = cur.execute(sql)
        conn.commit()
        return sta

    def exeQuery(cur,sql):
        cur.execute(sql)
        result = cur.fetchone()
        return result

    def exeSearch(cur):
        cur.execute('select id from xungen')

    def connClose(conn,cur):
        cur.close()
        conn.close()
