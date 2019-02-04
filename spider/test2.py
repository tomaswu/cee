import spider
import re,json

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
        # print(total_data)
        for i in total_data:
            data=[i[1:-1] for i in re.findall(r'>.{1,15}?<',i)]
            print(data)
            
        keys=['年份','最低','最高','平均','录取人数','录取批次']
        ye={}
        for i in range(len(keys)):
            try:
                ye[keys[i]]=data[i]
            except:
                ye[keys[i]]='------'
            
            data_json=json.dumps(ye)
            result.append(data_json)
    return result


url='http://college.gaokao.com/school/tinfo/138/result/16/2/'

y=spider.getContent(url,m=1)

y=parseContent(y,m=1)

print(y)