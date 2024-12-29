import pandas as pd
import csv
import numpy as np
import stopwords as stopwords
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('data.csv',encoding='utf-8')
data.head()
data['star'].unique()

# def make_label(star):
#     if star > 3:
#         return 1
#     else:
#         return 0
# data['setiment'] = data.star.apply(make_label)
# data.head()


from snownlp import SnowNLP
# text1 = '这个一般般！'
# text2 = '这个太棒了！'
# s1 = SnowNLP(text1)
# s2 = SnowNLP(text2)
#
# print(s1.sentiments,s2.sentiments)

# def snow_result(comment):
#     s = SnowNLP(comment)
#     if s.sentiments >= 0.5:
#         return 1
#     else:
#         return 0
# data['snlp_result'] = data.comment.apply(snow_result)
# print(data)
#
# counts = 0
# for i in range(len(data)):
#     if data.iloc[i,2] == data.iloc[i,3]:
#         counts+=1
# print(counts/len(data))

import jieba
def chinese_word_cut(mytext):
    return "/".join(jieba.cut(mytext))
data['cut_comment'] = data.comment.apply(chinese_word_cut)
data.head()

#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=22)
# X = data['cut_comment']
# y = data.sentiment



X = data['cut_comment']
print(type(data))
print(type(X))
y = data.sentiment

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19113122)


Vectorizer = CountVectorizer(max_df = 0.8,
                            min_df = 3,
                            token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                            stop_words =frozenset(stopwords) )


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

X_train_vect = Vectorizer.fit_transform(X_train)
nb.fit(X_train_vect, y_train)
train_score = nb.score(X_train_vect, y_train)
print(train_score)


test = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(),
columns=Vectorizer.get_feature_names())
test.head()


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

X_train_vect = Vectorizer.fit_transform(X_train)
nb.fit(X_train_vect, y_train)
train_score = nb.score(X_train_vect, y_train)
print(train_score)





