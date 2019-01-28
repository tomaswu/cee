# -*- coding:utf-8 -*- 
# Author: Tomas Wu
import json
def getnumber(log_name):
    with open(log_name,'r') as f1:
        log=[]
        for i in f1.readlines():
            if i[-3]=='=':
                log.append(i[-2:-1])
            elif i[-4]=='=':
                log.append(i[-3:-1])
            elif i[-5]=='=':
                log.append(i[-4:-1])
    return [int(i) for i in log]

if __name__=='__main__':
    log1=getnumber('log1.txt')
    log2=getnumber('log2.txt')
    log3=getnumber('log3.txt')
    log4=getnumber('log4.txt')
    log=[]
    log.extend(log1)
    log.extend(log2)
    log.extend(log3)
    log.extend(log4)
    log.sort()
    
    for i in range(1,702):
        if i!=log[i-1]:
            print('less {}'.format(i))
    # with open('result.txt','w') as f:
    #     f1=open('test1.txt','r')
    #     f2=open('test2.txt','r')
    #     f3=open('test3.txt','r')
    #     f4=open('test4.txt','r')
    #     for i in range(176):
    #         if i <=len(f1.readlines):
    #             f.write(f1.readline(i))
    #         if i <=len(f2.readlines):
    #             f.write(f1.readline(i))
    #         if i <=len(f1.readlines):
    #             f.write(f1.readline(i))
    #         if i <=len(f1.readlines):
    #             f.write(f1.readline(i))

    with open('test1.txt','rb') as f:
        for i in f.readlines():
            # print(i.decode('utf8'))
            print(json.loads(i))

