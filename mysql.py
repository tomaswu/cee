# -*- coding:utf-8 -*-
# Author: Tomas

import MySQLdb

db=MySQLdb.connect('localhost','root','wt7090334','test',charset='utf8')

cursor=db.cursor()

sql="INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES (%s, %s, %s, %s, %s )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

cursor.execute(sql)

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print("Error: unable to fecth data")

db.close()