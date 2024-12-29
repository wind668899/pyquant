import pandas as pd
import numpy as np
from pandas import DataFrame, Series

data = pd.read_csv("data.csv", encoding='UTF-8')


def make_label(df):
    df["sentiment"] = df["star"].apply(lambda x: 1 if x > 3 else 0)

make_label(data)
X = data[["comment"]]
y = data.sentiment

print(type(X))
print(type(y))

import jieba
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))

X["cuted_comment"] = X.comment.apply(chinese_word_cut)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print(X_train.shape)





def get_custom_stopword(stop_word_file):
    with open(stop_word_file,encoding='UTF-8') as f:
        stop_word = f.read()
        stop_word_list = stop_word.split("/n")
        custom_stopword = [i for i in stop_word_list]
    return custom_stopword

custom_stopwordstopwords = get_custom_stopword("end.txt")


from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
term_matrix = DataFrame(vect.fit_transform(X_train.cuted_comment).toarray(), columns=vect.get_feature_names())


print(term_matrix)
# term_matrix.shape



from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

from sklearn.pipeline import make_pipeline
pipe = make_pipeline(vect, nb)

from sklearn.model_selection import cross_val_score
k=cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy').mean()
print(k)



