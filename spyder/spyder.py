# -*- coding : utf-8 -*- 
'''
@Author: Tomas Wu
Date: 2019-01-29 22:31:26
@Desc: this is a spyder for fetching the data of entrance score line for college entrance examination. 
'''
# import urllib,re

# the goal web:
# http://college.gaokao.com/schpoint/a16/p1

# def getHTML(url):
#     f=urllib.request.urlopen(url)
#     print(f.read().decode('gbk'))
# It is sad that the urlopen can't deal with  the ajax.

from selenium import webdriver
import re,time,json

def getContent(url,m=0,*args, **kwargs):
    opt=webdriver.FirefoxOptions()
    opt.headless=True  # headless mode.
    prf=webdriver.FirefoxProfile()
    # prf.set_preference('permissions.default.image',2) #not loading image.
    # It is very weird that browser can't stop connection with the server if not loading images.
    browser=webdriver.Firefox(options=opt,firefox_profile=prf)
    browser.implicitly_wait(30)
    browser.get(url)
    # the parameter m means getting the college info (m=0) or scores info (m=1). 
    if m==0:
        content=browser.find_element_by_class_name('scores_List').get_attribute('outerHTML')
    elif m==1:
        content=browser.find_element_by_id('pointbyarea').get_attribute('outerHTML')
    browser.quit()
    return content


def parseContent(content,m=0,*args, **kwargs):
    result=[]
    if m==0:
        r=r'<dl>.*?</dl>'
        total_data=re.findall(r,content,re.DOTALL)
        for i in total_data:
            college=re.findall(r'k\">.{,20}?</a',i)[0][3:-3]  #get the college name.
            data=re.findall(r'li>.*?</li',i)
            recruit_location=data[0][8:-4]
            recruit_batch=data[1][8:-4]
            candidate_branch=data[2][8:-4]
            score_url=re.findall(r'http:.*?\"',data[3])[0][:-1]
            result.append([college,recruit_location,recruit_batch,candidate_branch,score_url])
    elif m==1:
        total_data=re.findall(r'<tr.*?</tr',content,re.DOTALL)[1:]
        for i in total_data:
            data=[i[1:-1] for i in re.findall(r'>.{1,15}?<',i)]
            data_json=json.dumps({'年份':data[0],'最低':data[1],'最高':data[2],'平均':data[3], \
                                    '录取人数':data[4],'录取批次':data[5]})
            result.append(data_json)
    return result


# test url:'http://college.gaokao.com/school/tinfo/34/result/16/2/'
        


if __name__=="__main__":
    
    # c=getContent(r'http://college.gaokao.com/school/tinfo/34/result/16/2/',1)
    with open('test_score.txt','r',encoding='utf-8') as f:
        c=f.read()
    
    cach=(parseContent(c,1))
    with open('data_saved.txt','w',encoding='utf-8') as f:
        for i in cach:
            f.write(str(i)+'\n')