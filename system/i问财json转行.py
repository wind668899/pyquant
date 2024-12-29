import json
import os
import requests
def readFile(file,status,resultFile):
    print(resultFile)
    result=open(resultFile,'a',encoding='utf-8')
    with open(file, 'r',encoding='utf-8') as file:
        d= json.load(file)
        datas=d['answer']['components'][0]['data']['datas']
        for i in datas:
            if status==False:
                for j in i:
                    print(j,end='\t')
                    result.write(j+"\t")
                print()
                result.write("\n")
                for j in i:
                    print(i[j],end='\t')
                    result.write(str(i[j]) + "\t")
                print()
                result.write("\n")
                status=True
            else:
                for j in i:
                    print(i[j],end='\t')
                    result.write(str(i[j]) + "\t")
                print()
                result.write("\n")


def list_text_files(root_dir):
    text_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".txt"):
                text_files.append(os.path.join(dirpath, file))
    return text_files


def post_data():
    url = 'http://www.iwencai.com/gateway/urp/v7/landing/getDataList?'
    formDate='query=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C11%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C%E5%B8%82%E5%80%BC&urp_sort_way=desc&urp_sort_index=%E5%8F%98%E5%8A%A8%E6%95%B0%E9%87%8F%E5%8D%A0%E6%B5%81%E9%80%9A%E8%82%A1%E6%AF%94%5B20240518-20241119%5D&page=1&perpage=100&addheaderindexes=&condition=%5B%7B%22score%22%3A0.0%2C%22chunkedResult%22%3A%22%E5%8C%97%E4%BA%A4%E6%89%80_%26_%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4_%26_10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85_%26_11%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85_%26_%E5%B8%82%E5%80%BC%22%2C%22opName%22%3A%22and%22%2C%22opProperty%22%3A%22%22%2C%22sonSize%22%3A7%2C%22relatedSize%22%3A%220%22%2C%22logid%22%3A%2202af642076961a383001746cfeb5e275%22%2C%22source%22%3A%22text2sql%22%7D%2C%7B%22dateText%22%3A%22%22%2C%22indexName%22%3A%22%E8%82%A1%E7%A5%A8%E5%B8%82%E5%9C%BA%E7%B1%BB%E5%9E%8B%22%2C%22indexProperties%22%3A%5B%22%E5%8C%85%E5%90%AB%E5%8C%97%E8%AF%81a%E8%82%A1%22%5D%2C%22ci%22%3Atrue%2C%22source%22%3A%22text2sql%22%2C%22type%22%3A%22index%22%2C%22indexPropertiesMap%22%3A%7B%22%E5%8C%85%E5%90%AB%22%3A%22%E5%8C%97%E8%AF%81a%E8%82%A1%22%7D%2C%22reportType%22%3A%22null%22%2C%22ciChunk%22%3A%22%E5%8C%97%E4%BA%A4%E6%89%80%22%2C%22createBy%22%3A%22preCache%22%2C%22uiText%22%3A%22%E8%82%A1%E7%A5%A8%E5%B8%82%E5%9C%BA%E7%B1%BB%E5%9E%8B%E5%8C%85%E5%90%AB%E5%8C%97%E4%BA%A4%E6%89%80%22%2C%22valueType%22%3A%22_%E8%82%A1%E7%A5%A8%E5%B8%82%E5%9C%BA%E7%B1%BB%E5%9E%8B%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22dateList%22%3A%5B%5D%2C%22order%22%3A0%7D%2C%7B%22ciChunk%22%3A%22%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%22%2C%22createBy%22%3A%22cache%22%2C%22opName%22%3A%22and%22%2C%22opProperty%22%3A%22%22%2C%22ci%22%3Afalse%2C%22uiText%22%3A%22%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%8F%98%E5%8A%A8%E8%82%A1%E6%95%B0%E6%98%8E%E7%BB%86%E5%B0%8F%E4%BA%8E0%E5%B9%B6%E4%B8%94%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%A2%9E%E5%87%8F%E6%8C%81%E5%8F%98%E5%8A%A8%E6%97%A5%E6%9C%9F%22%2C%22sonSize%22%3A2%2C%22opPropertyMap%22%3A%7B%7D%2C%22source%22%3A%22text2sql%22%2C%22order%22%3A0%7D%2C%7B%22dateText%22%3A%22%22%2C%22indexName%22%3A%22%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%8F%98%E5%8A%A8%E8%82%A1%E6%95%B0%E6%98%8E%E7%BB%86%22%2C%22indexProperties%22%3A%5B%22%3C0%22%2C%22nodate%201%22%2C%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020240518%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241119%22%5D%2C%22ci%22%3Afalse%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22type%22%3A%22index%22%2C%22isDateRange%22%3Atrue%2C%22indexPropertiesMap%22%3A%7B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220240518%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241119%22%2C%22%3C%22%3A%220%22%2C%22nodate%22%3A%221%22%7D%2C%22parentOpName%22%3A%22and%22%2C%22reportType%22%3A%22NATURAL_DAILY%22%2C%22ciChunk%22%3A%22%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%22%2C%22createBy%22%3A%22cache%22%2C%22dateType%22%3A%22%2B%E5%8C%BA%E9%97%B4%22%2C%22isExtend%22%3Afalse%2C%22uiText%22%3A%22%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%8F%98%E5%8A%A8%E8%82%A1%E6%95%B0%E6%98%8E%E7%BB%86%E5%B0%8F%E4%BA%8E0%22%2C%22valueType%22%3A%22_%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%28%E8%82%A1%29%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22parentOpOrder%22%3A0%2C%22order%22%3A1%7D%2C%7B%22dateText%22%3A%22%22%2C%22indexName%22%3A%22%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%A2%9E%E5%87%8F%E6%8C%81%E5%8F%98%E5%8A%A8%E6%97%A5%E6%9C%9F%22%2C%22indexProperties%22%3A%5B%22nodate%201%22%2C%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020240518%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241119%22%5D%2C%22ci%22%3Afalse%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22type%22%3A%22index%22%2C%22isDateRange%22%3Atrue%2C%22indexPropertiesMap%22%3A%7B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220240518%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241119%22%2C%22nodate%22%3A%221%22%7D%2C%22parentOpName%22%3A%22and%22%2C%22reportType%22%3A%22NATURAL_DAILY%22%2C%22ciChunk%22%3A%22%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%22%2C%22createBy%22%3A%22cache%22%2C%22dateType%22%3A%22%2B%E5%8C%BA%E9%97%B4%22%2C%22isExtend%22%3Afalse%2C%22uiText%22%3A%22%E5%A4%A7%E8%82%A1%E4%B8%9C%E5%A2%9E%E5%87%8F%E6%8C%81%E5%8F%98%E5%8A%A8%E6%97%A5%E6%9C%9F%22%2C%22valueType%22%3A%22%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22parentOpOrder%22%3A0%2C%22order%22%3A2%7D%2C%7B%22dateText%22%3A%2210%E6%9C%88%E4%BB%BD%22%2C%22indexName%22%3A%22%E5%8C%BA%E9%97%B4%E6%B6%A8%E8%B7%8C%E5%B9%85%3A%E5%89%8D%E5%A4%8D%E6%9D%83%22%2C%22indexProperties%22%3A%5B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241008%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241031%22%5D%2C%22ci%22%3Atrue%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22source%22%3A%22text2sql%22%2C%22type%22%3A%22index%22%2C%22isDateRange%22%3Atrue%2C%22indexPropertiesMap%22%3A%7B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241008%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241031%22%7D%2C%22reportType%22%3A%22TRADE_DAILY%22%2C%22ciChunk%22%3A%2210%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%22%2C%22createBy%22%3A%22ner_con%22%2C%22dateType%22%3A%22%2B%E5%8C%BA%E9%97%B4%22%2C%22isExtend%22%3Afalse%2C%22uiText%22%3A%2210%E6%9C%88%E4%BB%BD%E7%9A%84%E6%B6%A8%E8%B7%8C%E5%B9%85%22%2C%22valueType%22%3A%22_%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%28%25%29%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22order%22%3A0%7D%2C%7B%22dateText%22%3A%2211%E6%9C%88%E4%BB%BD%22%2C%22indexName%22%3A%22%E5%8C%BA%E9%97%B4%E6%B6%A8%E8%B7%8C%E5%B9%85%3A%E5%89%8D%E5%A4%8D%E6%9D%83%22%2C%22indexProperties%22%3A%5B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241101%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241118%22%5D%2C%22ci%22%3Atrue%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22source%22%3A%22text2sql%22%2C%22type%22%3A%22index%22%2C%22isDateRange%22%3Atrue%2C%22indexPropertiesMap%22%3A%7B%22%E8%B5%B7%E5%A7%8B%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241101%22%2C%22%E6%88%AA%E6%AD%A2%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241118%22%7D%2C%22reportType%22%3A%22TRADE_DAILY%22%2C%22ciChunk%22%3A%2211%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%22%2C%22createBy%22%3A%22ner_con%22%2C%22dateType%22%3A%22%2B%E5%8C%BA%E9%97%B4%22%2C%22isExtend%22%3Afalse%2C%22uiText%22%3A%2211%E6%9C%88%E4%BB%BD%E7%9A%84%E6%B6%A8%E8%B7%8C%E5%B9%85%22%2C%22valueType%22%3A%22_%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%28%25%29%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22order%22%3A0%7D%2C%7B%22dateText%22%3A%22%22%2C%22indexName%22%3A%22%E6%80%BB%E5%B8%82%E5%80%BC%22%2C%22indexProperties%22%3A%5B%22nodate%201%22%2C%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020241118%22%5D%2C%22ci%22%3Atrue%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22source%22%3A%22text2sql%22%2C%22type%22%3A%22index%22%2C%22indexPropertiesMap%22%3A%7B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220241118%22%2C%22nodate%22%3A%221%22%7D%2C%22reportType%22%3A%22TRADE_DAILY%22%2C%22ciChunk%22%3A%22%E5%B8%82%E5%80%BC%22%2C%22createBy%22%3A%22preCache%22%2C%22dateType%22%3A%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%2C%22isExtend%22%3Afalse%2C%22uiText%22%3A%22%E6%80%BB%E5%B8%82%E5%80%BC%22%2C%22valueType%22%3A%22_%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%28%E5%85%83%7C%E6%B8%AF%E5%85%83%7C%E7%BE%8E%E5%85%83%7C%E8%8B%B1%E9%95%91%29%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22sonSize%22%3A0%2C%22dateList%22%3A%5B%5D%2C%22order%22%3A0%7D%5D&codelist=&indexnamelimit=&logid=02af642076961a383001746cfeb5e275&ret=json_all&sessionid=02af642076961a383001746cfeb5e275&source=Ths_iwencai_Xuangu&date_range%5B0%5D=20240518&date_range%5B1%5D=20241119&iwc_token=0ac952a717319373404546732&urp_use_sort=1&user_id=482738010&uuids%5B0%5D=24087&query_type=stock&comp_id=6836372&business_cat=soniu&uuid=24087'
    header = {}
    header["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    header["cookie"] ='other_uid=Ths_iwencai_Xuangu_979ni0zxoxgv0q4ltb8yk85syziqox3f; ta_random_userid=s1g5km1nie; cid=9ecb78a23cbb4def812fbf7f209cee911731126290; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=MiUpIuzpSY6ei1S%2FwyiN2rIKFAntkuqzBI%2FDCNn9Js90Xt30D%2BuynpQg3o1qHLN3Hi80LrSsTFH9a%2B6rtRvqGg%3D%3D; u_did=D141F1A723994A9A9D502A52C1076DE9; u_ttype=WEB; user=MDrB9bvUb2c6Ok5vbmU6NTAwOjQ5MjczODAxMDo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDo6Ojo0ODI3MzgwMTA6MTczMTkzNzMzMDo6OjE1NTQyNTUzMDA6NjA0ODAwOjA6MTNmYjI2MDc0ZDVlMTQ1NGM2NDU1NDUxYTgzNmY3MWE3OmRlZmF1bHRfNDox; userid=482738010; u_name=%C1%F5%BB%D4og; escapename=%25u5218%25u8f89og; ticket=17aac6f6eb6ad270621fc430f8219892; user_status=0; utk=81bac676ab2e41e63c5c3efd4678e918; v=A5-tShrvBG2s8ABxdrLy_UcTLvgsBPOiDVj3mjHsO86VwLFmOdSD9h0oh-1C'

    #header[ "authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMwMzQxNDEwM0BxcS5jb20iLCJ1c2VyX2lkIjoxMTU5LCJpYXQiOjE3MzExMzU3ODQsImV4cCI6MTczMTMwODU4NH0.JaeG8JW_AR67YoyjOH4KWJYJLbSnZ6d6EdqSq8528RU"
    header['referer']='http://www.iwencai.com/unifiedwap/result?w=%E5%8C%97%E4%BA%A4%E6%89%80%EF%BC%8C%E8%82%A1%E4%B8%9C%E5%87%8F%E6%8C%81%E6%97%B6%E9%97%B4%EF%BC%8C10%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C11%E6%9C%88%E4%BB%BD%E6%B6%A8%E5%B9%85%EF%BC%8C%E5%B8%82%E5%80%BC&querytype=stock&addSign=1731937339235'
    header["host"]='www.iwencai.com'
    header['origin']='http://www.iwencai.com'
    # header['content-type']='application/x-www-form-urlencoded'
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
    response = requests.post(url+formDate,headers=header)

    #print(response.json())
    d=response.json()
    print(d)



if __name__ == '__main__':

    root_dir='C:\\Users\\wind\\Desktop\\北证\\文本\\'
    files=list_text_files(root_dir)
    status=False
    resultFile='C:\\Users\\wind\\Desktop\\北证\\result.csv'
    f=open(resultFile,'w',encoding='utf-8')
    for i in files:
        if status==False:
            readFile(i,False,resultFile)
            status=True
        else:
            readFile(i, True,resultFile)

    #post_data()



