# -*- coding : utf-8 -*- 
'''
@Author: Tomas Wu
Date: 2019-01-29 22:31:26
@Desc: this is a spyder for fetching the data of entrance score line for colloge entrance examination. 
'''
# import urllib,re

# the goal web:
# http://college.gaokao.com/schpoint/a16/

# def getHTML(url):
#     f=urllib.request.urlopen(url)
#     print(f.read().decode('gbk'))
# It is sad that the urlopen cant deal with  the ajax.

from selenium import webdriver
import re,time

def getContent(url):
    opt=webdriver.FirefoxOptions()
    opt.headless=True  # headless mode.
    prf=webdriver.FirefoxProfile()
    # prf.set_preference('permissions.default.image',2) #not loading image.
    # It is very weird that broswer cant stop connection with server if not loading image.
    broswer=webdriver.Firefox(options=opt,firefox_profile=prf)
    broswer.implicitly_wait(30)
    broswer.get(url)
    content=broswer.find_element_by_class_name('scores_List').get_attribute('outerHTML')
    broswer.quit()
    return content

def parseContent(content):
    result=[]
    r=r'<dl>.*?</dl>'
    data=re.findall(r,content,re.DOTALL)
    for i in data:
        colloge=re.findall(r'k\">.{,20}?</a',i)[0][3:-3]  #get the colloge name.
        
        data=re.findall(r'li>.*?</li',i)
        recruit_location=data[0][8:-4]
        recruit_batch=data[1][8:-4]
        candidate_branch=data[2][8:-4]
        score_url=re.findall(r'http:.*?\"',data[3])[0][:-1]
        result.append([colloge,recruit_location,recruit_batch,candidate_branch,score_url])
    return result
        


if __name__=="__main__":
    
    # c=getContent(r'http://college.gaokao.com/schpoint/a16/')
    with open('test.txt','r',encoding='utf-8') as t:
        c=t.read()
    # print(c)
    parseContent(c)