from pytdx.reader import TdxExHqDailyBarReader
import pymysql
from pytdx.hq import TdxHq_API
from pytdx.reader import TdxExHqDailyBarReader as a
from pytdx.reader import TdxDailyBarReader as b

reader1 = a()
reader2 = b()

def getSymbols(sql,DataBase):
    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "123456", DataBase, charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database=DataBase, charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    results = cursor.fetchall()
    symbols = []
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    for data in results:
        # print(type(data))
        # print(data)
        symbols.append(data[0])
        # print(type(symbols))
    # 关闭数据库连接
    db.close()
    return symbols
def getLastDate(sql,DataBase):
    #db = pymysql.connect("localhost", "root", "123456", DataBase, charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database=DataBase, charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    results = cursor.fetchall()
    symbols = {}
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    for data in results:
        # print(type(data))
        # print(data)
        symbols[data[0]] = data[1]
        # print(type(symbols))
    # 关闭数据库连接
    db.close()
    return symbols

def execute(sql,DataBase):
    #db = pymysql.connect("localhost", "root", "123456", DataBase, charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database=DataBase, charset="utf8")
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print('跟新数据：' + sql)
    except:
        print('except:' + sql)
        raise
    finally:
        pass
    db.close()

def updateData(DataBase):
    stockMessages=getSymbols('SELECT* FROM stockmessage',DataBase)
    lastDate=getLastDate('SELECT symbol,max(date) FROM datad GROUP BY symbol',DataBase)
    print(stockMessages)
    values = []
    for symbol in stockMessages:
        try:
            df=None
            if len(symbol) == 8:
                file = 'D:/new_tdx/vipdoc/ds/lday/8#' + symbol + '.day'
                df = reader1.get_df(file)
            elif symbol.find('I') != -1:
                file = 'D:/new_tdx/vipdoc/ds/lday/47#' + symbol + '.day'
                df = reader1.get_df(file)
            elif symbol[0] == '6' or symbol[0] == '5' or symbol[0] == '9':
                file = 'D:/new_tdx/vipdoc/sh/lday/sh' + symbol + '.day'
                df = reader2.get_df(file)
            elif symbol[0] == '0' or symbol[0] == '3':
                file = 'D:/new_tdx/vipdoc/sz/lday/sz' + symbol + '.day'
                df = reader2.get_df(file)
        except:
            print('数据异常'+symbol + '不存在')
            continue
        #print(df)
        try:
            if  symbol in lastDate:
                date = str(lastDate[symbol]).split(' ')[0]
                #for i in range(len(df)):
                 #   j = len(df) - i - 1
                 #   index = str(df.iloc[[j]].index.values[0]).split('T')[0]
                    # print(index)
                 #   if index == date:
                        # print('true')
                 #      break
                newDatas = df[df.index>date]
            else:
                #j=0
                #newDatas=df.tail(len(df)-j-1)
                newDatas=df
            for i in range(len(newDatas)):
                # print(date, end='\t')
                # print(dataD.iloc[i]['open'], end='\t')
                # print(dataD.iloc[i]['close'] / dataD.iloc[i + 1]['close'] - 1)
                da = str(newDatas.iloc[[i]].index.values[0]).split('T')[0]
                o = newDatas.iloc[i]['open']
                h = newDatas.iloc[i]['high']
                l = newDatas.iloc[i]['low']
                c = newDatas.iloc[i]['close']
                vol = newDatas.iloc[i]['volume']
                amount = newDatas.iloc[i]['amount']
                value = (symbol, da, o, h, l, c, vol, amount)
                values.append(value)
        except:
            print(symbol+'数据不存在')
    sql = 'INSERT INTO DataD(symbol,date,open,high,low,close,vol,turnover) values'

    if len(values)>0:
        for value in values:
            sql = sql + '("%s","%s",%f,%f,%f,%f,%d,%f),' % (value)
        sql = sql[0:-1]
    #print(sql)
        execute(sql,DataBase)





def main():
    updateData('option')


if __name__ == '__main__':
    main()

