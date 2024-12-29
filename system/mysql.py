import pymysql
def execute(sql,DataBase):
    db = pymysql.connect("localhost", "root", "123456", DataBase, charset='utf8')
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
file=open('C:\\Users\\Administrator\\Desktop\\java\\期权2.txt','r')
file2=open('C:\\Users\\Administrator\\Desktop\\java\\sql.txt','w')
symbol=''
sql='INSERT INTO datad (symbol,date,open,high,low,close,vol,turnover) values'
for str in file.readlines():
    li=str.replace('\n','').split('\t')
    if li[0]!=symbol and symbol!='':
        try:
            execute(sql[0:-1],'option')
            print(sql[0:-1])
            file2.write(sql[0:-1]+'\n')
        except:
            pass
            print(symbol+'\t数据异常')
        symbol = li[0]
        sql = 'INSERT INTO datad (symbol,date,open,high,low,close,vol,turnover) values'
        sql = sql + '("' + symbol + '","' + li[1] + '",' + li[2] + ',' + li[3] + ',' + li[4] + ',' + li[5] + ',' + li[
            6] + ',' + li[7] + '),'
    else:
        symbol=li[0]
        sql=sql+'("'+symbol+'","'+li[1]+'",'+li[2]+','+li[3]+','+li[4]+','+li[5]+','+li[6]+','+li[7]+'),'

#execute(sql[0:-1],'option')
print(sql[0:-1])
file2.write(sql[0:-1]+'\n')
        
        
        
    #print(str.replace('\n','').split('\t'))

#execute(sql,'option')