import json
import os
import requests
import time
import random
def readFile(f,status,resultFile):
    print(resultFile)
    result=open(resultFile,'a',encoding='utf-8')
    with open(f, 'r',encoding='utf-8') as file:
        d= json.load(file)
        datas=d['answer']['components'][0]['data']['datas']
        for i in datas:
            if status==False:
                for j in i:
                    print(j,end='\t')
                    result.write(j+"\t")
                print()
                result.write('\t'+f+"\n")
                for j in i:
                    print(i[j],end='\t')
                    result.write(str(i[j]) + "\t")
                print()
                result.write('\t'+f+"\n")
                status=True
            else:
                for j in i:
                    print(i[j],end='\t')
                    result.write(str(i[j]) + "\t")
                print()
                result.write('\t'+f+"\n")


def list_text_files(root_dir):
    text_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".txt"):
                text_files.append(os.path.join(dirpath, file))
    return text_files


def post_data(query,page,perpage):
    url = 'http://www.iwencai.com/gateway/urp/v7/landing/getDataList?'
    query='query='+query+'&page='+str(page)+'&perpage='+str(perpage)
    formData=query+'&comp_id=6836372&uuid=24087&condition=%5B%7B%22dateText%22%3A%222024%E5%B9%B4%22%2C%22ci%22%3Afalse%2C%22indexName%22%3A%22%E4%B8%9A%E7%BB%A9%E5%BF%AB%E6%8A%A5%E6%8A%AB%E9%9C%B2%E6%97%A5%22%2C%22indexProperties%22%3A%5B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241231%22%5D%2C%22dateUnit%22%3A%22%E5%B9%B4%22%2C%22source%22%3A%22new_parser%22%2C%22type%22%3A%22index%22%2C%22indexPropertiesMap%22%3A%7B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241231%22%7D%2C%22reportType%22%3A%22QUARTER%22%2C%22score%22%3A0%2C%22node_type%22%3A%22index%22%2C%22dateType%22%3A%22%E6%8A%A5%E5%91%8A%E6%9C%9F%22%2C%22chunkedResult%22%3A%222024%E5%B9%B4%E4%B8%9A%E7%BB%A9%E5%BF%AB%E6%8A%A5%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22uiText%22%3A%222024%E5%B9%B4%E7%9A%84%E4%B8%9A%E7%BB%A9%E5%BF%AB%E6%8A%A5%E6%8A%AB%E9%9C%B2%E6%97%A5%22%2C%22valueType%22%3A%22_%E6%97%A5%E6%9C%9F%22%2C%22sonSize%22%3A0%7D%5D'
    header = {}
    header["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    # header["cookie"] ='other_uid=Ths_iwencai_Xuangu_979ni0zxoxgv0q4ltb8yk85syziqox3f; ta_random_userid=s1g5km1nie; cid=9ecb78a23cbb4def812fbf7f209cee911731126290; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=MiUpIuzpSY6ei1S%2FwyiN2rIKFAntkuqzBI%2FDCNn9Js90Xt30D%2BuynpQg3o1qHLN3Hi80LrSsTFH9a%2B6rtRvqGg%3D%3D; u_did=D141F1A723994A9A9D502A52C1076DE9; u_ttype=WEB; user=MDrB9bvUb2c6Ok5vbmU6NTAwOjQ5MjczODAxMDo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDo6Ojo0ODI3MzgwMTA6MTczMTkzNzMzMDo6OjE1NTQyNTUzMDA6NjA0ODAwOjA6MTNmYjI2MDc0ZDVlMTQ1NGM2NDU1NDUxYTgzNmY3MWE3OmRlZmF1bHRfNDox; userid=482738010; u_name=%C1%F5%BB%D4og; escapename=%25u5218%25u8f89og; ticket=17aac6f6eb6ad270621fc430f8219892; user_status=0; utk=81bac676ab2e41e63c5c3efd4678e918; v=A5-tShrvBG2s8ABxdrLy_UcTLvgsBPOiDVj3mjHsO86VwLFmOdSD9h0oh-1C'
    #
    # #header[ "authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    # header['referer']='http://www.iwencai.com/unifiedwap/result?w=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C11%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C%E5%B8%82%E5%80%BC&querytype=stock&addSign=1731937339235'
    # header["host"]='www.iwencai.com'
    # header['origin']='http://www.iwencai.com'
    # header['content-type']='application/x-www-form-urlencoded'

    header['via'] = '1.1 cachewc8.10jqka.com.cn (squid/3.5.20), 1.1 cachehw188 (squid/3.5.20)'
#     data={
#     "source": "Ths_iwencai_Xuangu",
#     "version": "2.0",
#     "query_area": "",
#     "block_list": "",
#     "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
#     "question": "北交所，股东减持时间，10月份涨幅，11月份涨幅，市值",
#     "perpage": "200",
#     "page": 1,
#     "secondary_intent": "stock",
#     "log_info": "{\"input_type\":\"typewrite\"}",
#     "rsh": "482738010"
# }
    response = requests.post(url+formData,headers=header)

    #print(response.json())
    d=response.json()

    file="C:\\Users\\wind\\Desktop\\py\\ifind\\"+query+'.txt'
    result = open(file, 'w', encoding='utf-8')
    json.dump(d, result)
    #result.writelines(str(d))
    result.close()
    print(d)
    return d

def json_To_Excel():
    root_dir='C:\\Users\\wind\\Desktop\\py\\ifind\\'
    files=list_text_files(root_dir)
    status=False
    resultFile='C:\\Users\\wind\\Desktop\\py\\result.csv'
    f=open(resultFile,'w',encoding='utf-8')
    for i in files:
        if status==False:
            readFile(i,False,resultFile)
            status=True
        else:
            readFile(i, True,resultFile)

def queryIFind(query):
    page=1
    perpage=100
    d=post_data(query,page,perpage)
    k=d['answer']['components'][0]['data']['meta']['extra']['row_count']
    for i in range(13,int(k/100+2)):
        t=random.randint(5,20)
        time.sleep(t)
        post_data(query, i, perpage)


#批量查询
def plcx():
    #查询词列表
    file = 'C:\\Users\\wind\\Desktop\\py\\2.txt'
    f=open(file,'r',encoding='utf-8')
    for i in f.readlines():
        query=i.replace("\n",'')
        print(query)
        t=random.randint(0, 2)
        time.sleep(t)
        queryIFind(query)

    json_To_Excel()

if __name__ == '__main__':


    #
    query='2024年业绩快报'
    queryIFind(query)
    json_To_Excel()




