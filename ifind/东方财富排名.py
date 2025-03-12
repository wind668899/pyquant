import requests        #导入requests包
from urllib.request import Request
from urllib.request import urlopen

import json
def get_data(word=None):
    url ='https://guba.eastmoney.com/rank/stock?code=600126&from='
    header={}
    header["User-Agent"]='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    header["cookie"]="Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    header["authorization"]="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
   #header['referer']='http://www.iwencai.com/unifiedwap/result?w=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E6%9C%80%E8%BF%913%E4%B8%AA%E6%9C%88%E8%B0%83%E7%A0%94%E6%AC%A1%E6%95%B0%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85&querytype=stock'
    # header["host"]='www.iwencai.com'
    # header['origin']='http://www.iwencai.com'
    # header['content-type']='application/x-www-form-urlencoded'
    response = requests.get(url,headers=header)
    print(response.text)

def post_data(resultFile):
    url = 'http://www.iwencai.com/customized/chart/get-robot-data'
    header = {}
    header["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    header["cookie"] = "Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    #header[ "authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    # header['referer']='http://www.iwencai.com/unifiedwap/result?w=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E6%9C%80%E8%BF%913%E4%B8%AA%E6%9C%88%E8%B0%83%E7%A0%94%E6%AC%A1%E6%95%B0%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85&querytype=stock'
    header["host"]='www.iwencai.com'
    header['origin']='http://www.iwencai.com'
    # header['content-type']='application/x-www-form-urlencoded'
    data={
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
    "question": "北交所，10月份涨跌幅",
    "perpage": "100",
    "page": 1,
    "secondary_intent": "stock",
    "log_info": "{\"input_type\":\"typewrite\"}",
    "rsh": "482738010"
}
    response = requests.post(url,json=data,headers=header)

    #print(response.json())
    d=response.json()
    datas=d['data']['answer'][0]['txt'][0]['content']['components'][0]['data']['datas']
    result=open(resultFile,'w',encoding='utf-8')
    status=False
    for i in datas:
        if status == False:
            for j in i:
                print(j, end='\t')
                result.write(j + "\t")
            print()
            result.write("\n")
            for j in i:
                print(i[j], end='\t')
                result.write(str(i[j]) + "\t")
            print()
            result.write("\n")
            status = True
        else:
            for j in i:
                print(i[j], end='\t')
                result.write(str(i[j]) + "\t")
            print()
            result.write("\n")

if __name__=='__main__':
    #post_data('C:\\Users\\wind\\Desktop\\北证\\result.txt')
    get_data("920099")