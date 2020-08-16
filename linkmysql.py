import pymysql

class MysqlHelp():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='zhuce', charset='utf8')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def insert(self,sql):
        self.cur.execute(sql)
        self.conn.commit()

    def serch_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        words = '  '.join(str(x) for x in result)
        return words

    def serch_all(self):
        self.cur.execute('select sfzh from new_students')
        result = self.cur.fetchall()
        return result

    def serch_list(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def table_list(self,sql):
        self.cur.execute(sql)
        result =self.cur.fetchone()
        return result

