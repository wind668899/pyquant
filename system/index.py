

def getData(symbol):
    f="D:\\期权数据\\input\\"+symbol+".txt"
    data={}
    for i in open(f,"r").readlines():
        if i!="数据来源:通达信\n":
            j=i.replace("\n","").split("\t")

        data[j[0]]=j[1:]
    return data



if __name__ == '__main__':

    index1=getData('510050')
    index2=getData('SPY')
    begin=""
    now=""
    for i in index1:
        if i in index2:
            if begin == "":
                begin = i
                pass
            else:
                now=i
                #print(float(index1[now][3])/float(index1[begin][3])-1.0)
                #print(str(i) + "\t" + str(index1[now][3]) + "\t" + str(index2[now][3]))
                print(str(i) + "\t" + str(index1[now][0]) + "\t" + str(index1[now][1])+"\t"+str(index1[now][2]) + "\t" + str(index1[now][3]))
                #print(str(i)+"\t"+str(float(index1[now][3])/float(index1[begin][3])-1.0)+"\t"+str(float(index2[now][3])/float(index2[begin][3])-1.0))
                begin=now

