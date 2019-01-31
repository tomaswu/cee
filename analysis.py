# -*- coding:utf-8 -*- 
'''
    @Author: Tomas Wu 
    @Date: 2019-01-28 13:52:23 
    @Desc: analysis the data test.txt gotten from a selenium spyder.
'''

import sqlalchemy,json
from sqlalchemy import create_engine,Column,Integer,String,text  #text can help query data by regular expression.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
Firstly, the data in txt file should be input into a database for 
conveniently analyzing. 
'''
def to_database(filename):
    db=create_engine('mysql+mysqldb://root:123456@localhost/cee?charset=utf8',echo=False)  #echo = True means print the sql code.
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
        n=0
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
            n=n+1
            if n==500:
                session.commit()
                n=0
    session.commit()
    session.close()



def get_score(colloge_name):
    db=create_engine('mysql+mysqldb://root:123456@localhost/cee?charset=utf8',echo=False)
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
    Session=sessionmaker(bind=db)
    session=Session()
    # ret = session.query(university).filter(university.colloge.contains(colloge_name)).all() #contains is common.
    ret = session.query(university).filter(university.colloge==colloge_name).all()
    return ret


if __name__=='__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    # [to_database('test{}.txt'.format(i)) for i in range(1,5) ]
    
    ret=get_score('西南科技大学')
    for i in ret:
        print(i.colloge,i.branch,i.year,i.average_score)
    
    # for analysizing, the data should be shown by figure.
    plt.figure()
    x,y=[],[]
    for i in ret:
        x.append(float(i.year))
        y.append(float(i.average_score))  
    a=np.array([x,y])
    b=a.T[np.lexsort(a[0,None])].T   #sort the data along x.
    plt.plot(b[0],b[1],marker='o')
    plt.show()

    