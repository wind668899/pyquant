import json
import os
import datetime
from multiprocessing import Pool

#
#
#生成分钟线
def jsontickBar(file):
    fp = open('d:\\pyData\\' + file, 'r')
    symbol = file[3:9]
    path = 'd:\\Data\\tickBar\\' + symbol + '\\'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    date = ''
    js = {}
    for str in fp.readlines():
        if '/' in str:
            # print(str.split('\t')[7])
            list = str.replace('\n', '').split('\t')
            # print(list)
            date2 = date
            date = list[0].replace('/', '')
            key = list[1]
            list.pop(0)
            list.pop(0)
            if date2 != '' and date2 == date:
                js[key] = list
            elif date2 != '':
                pa = 'd:\\Data\\tickBar\\' + symbol + '\\' + date2.replace('/', '') + '.txt'
                print(pa)
                f = open(pa, 'w')
                # print(js)
                jso = json.dumps(js)
                f.write(jso)
                js = {}

def tickBar(file):
    fp = open('d:\\pyData\\' + file, 'r')
    symbol = file[3:9].split('.')[0]
    path = 'd:\\Data\\tickBar\\' + symbol + '\\'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    date = ''
    date2=''
    data=''
    list=[]
    pa=''
    for str in fp.readlines():
        if '/' in str:
            # print(str.split('\t')[7])
            list =str.split('\t')
            # print(list)
            date2 = date
            date = list[0].replace('/', '')
            list.pop(0)

            if date2=='':
                data=data+'\t'.join(list)
            elif date2 != '' and date2 == date:
                data = data + '\t'.join(list)
            elif date2 != '':
                pa = 'd:\\Data\\tickBar\\' + symbol + '\\' + date2.replace('/', '') + '.txt'
                isExists = os.path.exists(pa)
                if isExists:
                    continue
                print(pa)
                f = open(pa, 'w')
                f.write(data)
                f.close()
                data='\t'.join(list)
    if date2!='':
        pa = 'd:\\Data\\tickBar\\' + symbol + '\\' + date2.replace('/', '') + '.txt'
        isExists = os.path.exists(pa)
        if not isExists:
            print(pa)
            f = open(pa, 'w')
            f.write(data)
            f.close()

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    stocks = []
    for allDir in pathDir:
        stocks.append(allDir)
    pool = Pool(50)  # 可以同时跑50个进程
    pool.map(tickBar, stocks)
    pool.close()
    pool.join()


def main():
    start = datetime.datetime.now()
    eachFile('D:\\pyData\\')
    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    main()
