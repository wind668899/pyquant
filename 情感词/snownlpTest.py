from snownlp import SnowNLP
text1 = '大基金：提前终止减持'
text2 = '11家银行已官宣下调存款利率 最大降幅25个基点！'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)

print(s1.sentiments,s2.sentiments)
