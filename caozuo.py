import linkmysql

class ChuLi():
    def __init__(self):
        #super(linkmysql,self).__init__()
        self.mysql = linkmysql.MysqlHelp()

    def zhuce (self , str):
        sql = "update new_students set zt = '注册' where sfzh='"+ str +"'"
        self.mysql.insert(sql)

    def serch_one(self , str):
        sql = "select name,sex,xuebu,zy,bj,zt from new_students where sfzh='"+ str +"'"
        word = self.mysql.serch_one(sql)
        return  word

    def panduan (self , str):
        result = self.mysql.serch_all()
        lst1 = []
        for i in range(len(result)):
            lst1.append(result[i][0])
        for i in lst1:
            if str == i:
                return True
        else:
            return False

    def set_list(self,str):
        sql = "select DISTINCT "+ str +" from new_students;"
        result = self.mysql.serch_list(sql)
        lst1 = []
        for i in range(len(result)):
            lst1.append(result[i][0])
        return lst1

    def serch_table(self , str):
        sql = "select name,sex,xuebu,zy,bj,zt from new_students where sfzh='"+ str +"'"
        word = self.mysql.table_list(sql)
        return  word



