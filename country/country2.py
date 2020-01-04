#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://www.runoob.com/python/python-mysql.html
import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()
执行以上脚本输出结果如下：

Database version : 5.0.45






# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)

# # 关闭数据库连接
# db.close()


# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# # 关闭数据库连接
# db.close()
# 以上例子也可以写成如下形式：

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES (%s, %s, %s, %s, %s )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭数据库连接
# db.close()
# 实例：
# 以下代码使用变量向SQL语句中传递参数:

# ..................................
# user_id = "test123"
# password = "password"

# con.execute('insert into Login values(%s, %s)' % \
#              (user_id, password))
# ..................................
# 数据库查询操作
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall():接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# 实例：
# 查询EMPLOYEE表中salary（工资）字段大于1000的所有数据：

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # 打印结果
#       print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income )
# except:
#    print "Error: unable to fecth data"

# # 关闭数据库连接
# db.close()
# 以上脚本执行结果如下：

# fname=Mac, lname=Mohan, age=20, sex=M, income=2000
# 数据库更新操作
# 更新操作用于更新数据表的的数据，以下实例将 EMPLOYEE 表中的 SEX 字段为 'M' 的 AGE 字段递增 1：

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭数据库连接
# db.close()
# 删除操作
# 删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭连接
# db.close()
# 执行事务
# 事务机制可以确保数据一致性。

# 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
# Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。

# 实例：
# # SQL删除记录语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 向数据库提交
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

# commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。