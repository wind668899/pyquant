f=open("C:\\Users\\wind\\Desktop\\期权\\2.txt","r",encoding='UTF-8')
f2=open("C:\\Users\\wind\\Desktop\\期权\\result.txt","w",encoding='UTF-8')
data={}
k=f.readline().replace("\n", "").replace(".SH","").split('\t')
f
for i in f.readlines():
    j = i.replace("\n", "").replace(".SH","").replace(",","").replace(" ","").split('\t')
    if j[0] not in data:
        data[j[0]]={}
        data[j[0]][j[2]]=j[3:]
    else:
        data[j[0]][j[2]] = j[3:]
for i in data:
    for j in range(len(k)-3):
        if float(data[i]['开盘价'][j])<0.0001 and float(data[i]['最高价'][j])<0.0001 and float(data[i]['最低价'][j])<0.0001 and float(data[i]['收盘价'][j])<0.0001 and float(data[i]['成交额'][j])<0.0001 and float(data[i]['成交量'][j])<0.0001:
            pass
        else:
            print(i+"\t"+k[j+3]+"\t"+data[i]['开盘价'][j]+"\t"+data[i]['最高价'][j]+"\t"+data[i]['最低价'][j]+"\t"+data[i]['收盘价'][j]+"\t"+str(int(round(float(data[i]['成交量'][j])*10000,0)))+"\t"+str(int(round(float(data[i]['成交额'][j])*10000,0)))+"\n")
            f2.write(i+"\t"+k[j+3]+"\t"+data[i]['开盘价'][j]+"\t"+data[i]['最高价'][j]+"\t"+data[i]['最低价'][j]+"\t"+data[i]['收盘价'][j]+"\t"+str(int(round(float(data[i]['成交量'][j])*10000,0)))+"\t"+str(int(round(float(data[i]['成交额'][j])*10000,0)))+"\n")
