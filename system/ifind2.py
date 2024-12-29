import requests        #导入requests包
from urllib.request import Request
from urllib.request import urlopen

import json
def get_data(word=None):
    url ='https://pro.gogudata.com/api/specialModule/findById?id=115'
    header={}
    header["User-Agent"]='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    header["cookie"]="Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    #header["authorization"]="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
   #header['referer']='http://www.iwencai.com/unifiedwap/result?w=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E6%9C%80%E8%BF%913%E4%B8%AA%E6%9C%88%E8%B0%83%E7%A0%94%E6%AC%A1%E6%95%B0%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85&querytype=stock'
    # header["host"]='www.iwencai.com'
    # header['origin']='http://www.iwencai.com'
    # header['content-type']='application/x-www-form-urlencoded'
    response = requests.get(url,headers=header)

def post_data(resultFile):
    url = 'http://www.iwencai.com/customized/chart/get-robot-data'
    header = {}
    header["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    header["cookie"] ='other_uid=Ths_iwencai_Xuangu_979ni0zxoxgv0q4ltb8yk85syziqox3f; ta_random_userid=s1g5km1nie; cid=9ecb78a23cbb4def812fbf7f209cee911731126290; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=MiUpIuzpSY6ei1S%2FwyiN2rIKFAntkuqzBI%2FDCNn9Js90Xt30D%2BuynpQg3o1qHLN3Hi80LrSsTFH9a%2B6rtRvqGg%3D%3D; u_did=D141F1A723994A9A9D502A52C1076DE9; u_ttype=WEB; user=MDrB9bvUb2c6Ok5vbmU6NTAwOjQ5MjczODAxMDo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDo6Ojo0ODI3MzgwMTA6MTczMTkzNzMzMDo6OjE1NTQyNTUzMDA6NjA0ODAwOjA6MTNmYjI2MDc0ZDVlMTQ1NGM2NDU1NDUxYTgzNmY3MWE3OmRlZmF1bHRfNDox; userid=482738010; u_name=%C1%F5%BB%D4og; escapename=%25u5218%25u8f89og; ticket=17aac6f6eb6ad270621fc430f8219892; user_status=0; utk=81bac676ab2e41e63c5c3efd4678e918; v=AxYkVUv8bdqeLVl-9NTragZQZ8cdt1pvrPuOVYB_AvmUQ7j56EeqAXyL3nxT'
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
    "question": "北交所，股东减持时间，10月份涨幅，11月份涨幅，市值",
    "perpage": "200",
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
    post_data('C:\\Users\\wind\\Desktop\\北证\\result2.txt')