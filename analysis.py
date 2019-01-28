# -*- coding:utf-8 -*- 
'''
    @Author: Tomas Wu 
    @Date: 2019-01-28 13:52:23 
    @Desc: analysize the data test.txt gotted from a selenium spyder
'''

import sqlalchemy,json
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
Firstly, the data in txt file should be input into a database for 
conveniently analyzing. 
'''
def to_database(filename):
    db=create_engine('mysql://root:123456@localhost/cee?charset=utf8',echo=True)
    base=declarative_base()
    class university(base):
        __tablename__='ESL of CEE'
        id=Column(Integer,primary_key=True)
        colloge=Column(String(64))
        location=Column(String(64))
        branch=Column(String(64))
        batch=Column(String(64))
        year=Column(String(64))
        highest_score=Column(String(64))
        average_score=Column(String(64))
    base.metadata.create_all(db)
    session_class=sessionmaker(bind=db)
    session=session_class()
    
    with open(filename,'r') as f:
        for i in f.readlines():
            msg=json.loads(i)
            col_data=university( \
                colloge=str(msg['colloge']), \
                location=str(msg['location']), \
                branch=str(msg['branch']), \
                batch=str(msg['batch']), \
                year=str(msg['year']), \
                highest_score=str(msg['highest_score']), \
                average_score=str(msg['average_score']), \
            )
            session.add(col_data)
            session.commit()






if __name__=='__main__':
    
    to_database('test1.txt')