#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://www.runoob.com/python3/python3-mysql.html
import pymysql
 
db = pymysql.connect("localhost", "root", "root", "laravel_production_base")
 
cursor = db.cursor()
 
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print ("Database version : %s " % data)

sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
	VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
	# VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
	# ('Mac', 'Mohan', 20, 'M', 2000)
try:
	cursor.execute(sql)
	db.commit()
except:
   db.rollback()

db.close()




 
# user_id = "test123"
# password = "password"

# con.execute('insert into Login values( %s,  %s)' % \
#              (user_id, password))
 
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    cursor.execute(sql)
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]

#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")


# fname=Mac, lname=Mohan, age=20, sex=M, income=2000

# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    cursor.execute(sql)
#    db.commit()
# except:
#    db.rollback()
 

# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    cursor.execute(sql)
#    db.commit()
# except:
#    db.rollback()

# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
#  Python MySQL - mysql-connector 驱动Python3 网络编程 


# 操作数据库与操作文件类似，在读取修改开始和结束时都需要进行连接（打开），断开（关闭）等固定操作，文件读写时可以使用 with （上下文管理器）来简化操作，数据库当然也是可以的：

# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

# from pymysql import connect

# class DB():
#     def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
#     # 建立连接
#         self.conn = connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
#     # 创建游标，操作设置为字典类型
#         self.cur = self.conn.cursor(cursor = cursors.DictCursor)
 
#     def __enter__(self):
#     # 返回游标
#         return self.cur
 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#     # 提交数据库并执行
#         self.conn.commit()
#     # 关闭游标
#         self.cur.close()
#     # 关闭数据库连接
#         self.conn.close()
# sh-winter
#    sh-winter

# import pymysql

# class DB():
#     def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
#         # 建立连接 
#         self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
#         # 创建游标，操作设置为字典类型        
#         self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

#     def __enter__(self):
#         # 返回游标        
#         return self.cur

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 提交数据库并执行        
#         self.conn.commit()
#         # 关闭游标        
#         self.cur.close()
#         # 关闭数据库连接        
#         self.conn.close()


# if __name__ == '__main__':
#     with DB(host='192.168.68.129',user='root',passwd='zhumoran',db='text3') as db:
#         db.execute('select * from course')
#         print(db)
#         for i in db:
#             print(i)