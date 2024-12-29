import pymysql
import tushare as ts
import sys
from multiprocessing import Pool
import datetime
#import tdxData
from pytdx.reader import TdxExHqDailyBarReader as a
from pytdx.reader import TdxDailyBarReader as b

reader1 = a()
reader2 = b()


def getSymbols(sql):
    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "123456", "stocks", charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stocks", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    results = cursor.fetchall()
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()

        # print(type(symbols))
    # 关闭数据库连接
    db.close()
    return results


def getClose(sql):
    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "123456", "stocks2", charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stocks", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        close = results[0][0]
    except:
        return None
    # 关闭数据库连接
    db.close()
    return close


def getLastDataD(sql):
    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "123456", "stocks2", charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stocks", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        print(sql)
        # print(type(results))
        # LastDate = results[0][0]
    except:
        print('except:' + sql)
        return None
        raise

    # 关闭数据库连接
    db.close()
    return results


def saveData(sqls):
    #db = pymysql.connect("localhost", "root", "123456", "stocks2", charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stocks", charset="utf8")
    for sql in sqls:
        try:
            cursor = db.cursor()
            # print('=================')
            cursor.execute(sql)
            print('插入数据：' + sql)
            db.commit()

        except:
            print('except：' + sql)
            raise
        finally:
            pass
    db.close()


def execute(sql):
    #db = pymysql.connect("localhost", "root", "123456", "stocks2", charset='utf8')
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stocks", charset="utf8")
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print('更新数据：' + sql)
    except:
        print('except:' + sql)
        raise
    finally:
        pass
    db.close()


def updateStockMessage():
    new = ts.get_stock_basics()
    symbols =dict(getSymbols('SELECT symbol,name FROM STOCKMESSAGE'))
    print(symbols)
    newsymbol = {}
    for symbol, rows in new.iterrows():
        print(rows.index)
        print(rows.get('name'))
        newsymbol[symbol] = rows.get('name')
    addSqls = []

    # print(newsymbol.difference(symbols))
    for symbol in newsymbol:
        # print(new.loc[symbol].values[0:-1])
        if  symbol not in symbols:
            addsql = 'INSERT INTO stockmessage(symbol,name,area,industry,equity,outstandingCapital,type) values("' + symbol
            addsql = addsql + '","' + new.loc[symbol].values[0] + '","' + str(new.loc[symbol].values[2]) + '","' + str(new.loc[symbol].values[1]) + '",' + str(new.loc[symbol].values[5]) + ',' + str(new.loc[symbol].values[4]) + ',1);'
            addSqls.append(addsql)
        elif symbols.get(symbol) != newsymbol[symbol]:
            updateSql = 'UPDATE stockmessage SET name="' + newsymbol[symbol] + '" WHERE symbol="' + symbol + '"'
            execute(updateSql)
    saveData(addSqls)


def updateDataD(symbol):
    # new = ts.get_stock_basics()
    LD = getLastDataD('SELECT MAX(date) FROM timeseries')
    LastDate = LD[0]
    stockLastDataD = getLastDataD(
        'SELECT date,close FROM DataD where symbol="' + symbol + '" order by date desc limit 1')
    print(LastDate)
    print(stockLastDataD[0])
    if stockLastDataD is None:
        dataD = ts.get_h_data(symbol)
    elif stockLastDataD[0] > LastDate:
        LastDate = stockLastDataD[0]
        dataD = ts.get_h_data(symbol, start=str(LastDate))
    else:
        dataD = ts.get_h_data(symbol, start=str(LastDate))
    date = dataD.index[0].to_pydatetime()
    # print('===')
    # print(type(date))
    # date = datetime.datetime.strptime(da, "%Y-%m-%d")
    if date == LastDate:
        return
    values = []
    for i in range(len(dataD)):
        da = str(dataD.iloc[[i]].index.values[0]).split('T')[0]
        date = datetime.datetime.strptime(da, "%Y-%m-%d")
        if date == LastDate:
            pass
        if date > LastDate:
            if i < len(dataD) - 1:
                # print(date, end='\t')
                # print(dataD.iloc[i]['open'], end='\t')
                # print(dataD.iloc[i]['close'] / dataD.iloc[i + 1]['close'] - 1)
                o = dataD.iloc[i]['open']
                h = dataD.iloc[i]['high']
                l = dataD.iloc[i]['low']
                c = dataD.iloc[i]['close']
                vol = dataD.iloc[i]['volume']
                amount = dataD.iloc[i]['amount']
                change = c / dataD.iloc[i + 1]['close'] - 1
                value = (symbol, da, o, h, l, c, vol, amount, change)
                values.append(value)
            else:
                close = stockLastDataD[1]
                o = dataD.iloc[i]['open']
                h = dataD.iloc[i]['high']
                l = dataD.iloc[i]['low']
                c = dataD.iloc[i]['close']
                vol = dataD.iloc[i]['volume']
                amount = dataD.iloc[i]['amount']
                if close is None:
                    change = 0
                else:
                    change = c / close - 1
                value = (symbol, da, o, h, l, c, vol, amount, change)
                values.append(value)
        else:
            pass
    sql = 'INSERT INTO DataD(symbol,date,open,high,low,close,vol,turnover,cchange) values'
    for value in values:
        sql = sql + '("%s","%s",%f,%f,%f,%f,%d,%f,%f),' % (value)
    sql = sql[0:-1]
    execute(sql)

def updateTDXDataD(symbol):
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
        elif symbol[0] == '8' or symbol[0] == '9' or symbol[0] == '4':
            file = 'D:/new_tdx/vipdoc/bj/lday/bj' + symbol + '.day'
            print("AAA"+file)
            df = reader2.get_df(file)
        else:
            file=''
    except:
        print(symbol+'不存在')
        return
    print(file)
    stockLastDataD = getLastDataD(
        'SELECT date,close FROM DataD where symbol="' + symbol + '" order by date desc limit 1')

    #print(stockLastDataD[0])
    if stockLastDataD is None:
        dataD = df
        #dataD =None
    else:
        dataD = df[df.index > stockLastDataD[0]]
    if dataD is None:
        return
    #date = dataD.index[0].to_pydatetime()
    # print('===')
    # print(date)
    # print(type(date))
    # date = datetime.datetime.strptime(da, "%Y-%m-%d")

    values = []
    for i in range(len(dataD)):
        # da = str(dataD.iloc[[i]].index.values[0]).split('T')[0]
        date = dataD.index[i].to_pydatetime()
        if i == 0:
            o = dataD.iloc[i]['open']
            h = dataD.iloc[i]['high']
            l = dataD.iloc[i]['low']
            c = dataD.iloc[i]['close']
            vol = dataD.iloc[i]['volume']
            amount = dataD.iloc[i]['amount']
            if stockLastDataD is None:
                change=0;
            else:
                change = c / stockLastDataD[1] - 1
            value = (symbol, date, o, h, l, c, vol, amount, change)
            values.append(value)
        else:
            # print(date, end='\t')
            # print(dataD.iloc[i]['open'], end='\t')
            # print(dataD.iloc[i]['close'] / dataD.iloc[i + 1]['close'] - 1)
            o = dataD.iloc[i]['open']
            h = dataD.iloc[i]['high']
            l = dataD.iloc[i]['low']
            c = dataD.iloc[i]['close']
            vol = dataD.iloc[i]['volume']
            amount = dataD.iloc[i]['amount']
            change = c / dataD.iloc[i - 1]['close'] - 1
            value = (symbol, date, o, h, l, c, vol, amount, change)
            values.append(value)
    sql = 'INSERT INTO DataD(symbol,date,open,high,low,close,vol,turnover,cchange) values'
    #print(sql)
    if len(values)>0:
        for value in values:
            sql = sql + '("%s","%s",%f,%f,%f,%f,%d,%f,%f),' % (value)
        sql = sql[0:-1]
        print(sql)
        execute(sql)
        
def updateTDXDataD2(symbol):
    try:
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
        print(symbol+'不存在')
        return
    print(file)
    stockLastDataD = getLastDataD(
        'SELECT date,close FROM DataD where symbol="' + symbol + '" order by date desc limit 1')

    #print(stockLastDataD[0])
    if stockLastDataD is None:
        dataD = df
    else:
        dataD = df[df.index > stockLastDataD[0]]
        if dataD is None:
            return
        #date = dataD.index[0].to_pydatetime()
        # print('===')
        # print(date)
        # print(type(date))
        # date = datetime.datetime.strptime(da, "%Y-%m-%d")

        values = []
        for i in range(len(dataD)):
            # da = str(dataD.iloc[[i]bue].index.values[0]).split('T')[0]
            date = dataD.index[i].to_pydatetime()
            if i == 0:
                o = dataD.iloc[i]['open']
                h = dataD.iloc[i]['high']
                l = dataD.iloc[i]['low']
                c = dataD.iloc[i]['close']
                vol = dataD.iloc[i]['volume']
                amount = dataD.iloc[i]['amount']
                change = c / stockLastDataD[1] - 1
                value = (symbol, date, o, h, l, c, vol, amount, change)
                values.append(value)
            else:
                # print(date, end='\t')
                # print(dataD.iloc[i]['open'], end='\t')
                # print(dataD.iloc[i]['close'] / dataD.iloc[i + 1]['close'] - 1)
                o = dataD.iloc[i]['open']
                h = dataD.iloc[i]['high']
                l = dataD.iloc[i]['low']
                c = dataD.iloc[i]['close']
                vol = dataD.iloc[i]['volume']
                amount = dataD.iloc[i]['amount']
                change = c / dataD.iloc[i - 1]['close'] - 1
                value = (symbol, date, o, h, l, c, vol, amount, change)
                values.append(value)
        sql = 'INSERT INTO DataD(symbol,date,open,high,low,close,vol,turnover,cchange) values'
        if len(values)>0:
            for value in values:
                sql = sql + '("%s","%s",%f,%f,%f,%f,%d,%f,%f),' % (value)
            sql = sql[0:-1]
            print(sql)
            execute(sql)


# saveDataD('INSERT INTO DataD(symbol,date,open,high,low,close,vol,turnover,cchange) values(%s,%s,%f,%f,%f,%f,%d,%f,%f)',values)


def main():
    startTime = datetime.datetime.now()
    # pool = Pool(20)  # 可以同时跑20个进程
    # pool.map(updateTDXDataD, stocks)
    # pool.close()
    # pool.join()
    #updateStockMessage()
    #stocks = list(ts.get_stock_basics().index)
    stocks=[]
    # print(stocks)
    # updateDataD('300222')
    stockMessages = getSymbols('SELECT symbol FROM stockmessage')
    for i in stockMessages:
        #print(i)
        #updateTDXDataD(i[0])
        stocks.append(i[0])
    pool = Pool(20)  # 可以同时跑20个进程
    pool.map(updateTDXDataD, stocks)
    pool.close()
    pool.join()
    #print(stocks)

    # tdxData.updataData('stocks2')
    #updateTDXDataD('300223')
    endTime = datetime.datetime.now()
    print("time :", endTime - startTime)


if __name__ == '__main__':
    main()
