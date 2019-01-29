# -*- coding:utf-8 -*- 
'''
    @Author: Tomas Wu 
    @Date: 2019-01-27 22:10:20 
    @Desc: study of sqlalchemy
'''

# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Integer,String,Column
# from sqlalchemy.orm import sessionmaker

# if __name__=="__main__":
#     # create a connection
#     engine=sqlalchemy.create_engine("mysql+mysqldb://root:123456@localhost/cee", \
#                                     encoding="utf-8",echo=True)
    
#     # create a base class of ORM
#     base=declarative_base()
#     class user(base):
#         __tablename__ = "users" # set table name
#         id = Column(Integer,primary_key=True)
#         name = Column(String(32))
#         password = Column(String(64))
    
#     base.metadata.create_all(engine)

#     Session_class=sessionmaker(bind=engine)

#     Session=Session_class()

#     user_obj = user(name='Tom',password="654321mot") # add data to the user_obj, it can be exeuted any times.

#     Session.add(user_obj) # add the user_obj to the Session class for providing to database

#     Session.commit() # submit the data in Sessoin class to the table



# list sort test

import numpy as np

a=np.array([['1', 'b', '5'],
            ['3', 'c', '3'],
            ['5', 'a', '4'],
            ['4', 'd', '1'],
            ['2', 'f', '2']])

print(a)

# b=np.sort(a,axis=0)
# c=np.msort(a)
d=a[np.lexsort(a.T[0,None])].T 

print(d)