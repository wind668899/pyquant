import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def chinese_word_cut(mytext):
    return "/".join(jieba.cut(mytext))

data = pd.read_csv("data.csv", encoding='UTF-8')
#print(data.comment)
data['cut_comment'] = data.comment.apply(chinese_word_cut)
print(data['cut_comment'][0])
X = data['cut_comment']
y = data.star.apply(lambda x: 1 if x > 3 else 0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

# print("================")
# print(y_train)
# print("---------------")
# print(X_train)
# print("================")


# def get_custom_stopwords(stop_words_file):
#     with open(stop_words_file,encoding='UTF-8') as f:
#         stopwords = f.read()
#     stopwords_list = stopwords.split('\n')
#     custom_stopwords_list = [i for i in stopwords_list]
#     return custom_stopwords_list
# stop_words_file = 'end.txt'
# stopwords = get_custom_stopwords(stop_words_file)
# print(stopwords)
stopwords=['reviewbody','reviewbodybrief','nbsp','br','alt', 'class', 'emoji', 'https', 'img', 'm5', 'meituan']



#出现频率，构建矩阵
Vectorizer = CountVectorizer(max_df = 0.8,
                             min_df=1,
                            token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                            stop_words =frozenset(stopwords))

#构建总样本矩阵
test = pd.DataFrame(Vectorizer.fit_transform(X).toarray(), columns=Vectorizer.get_feature_names())
print(test)
print("总样本",test.shape)



#构建训练集矩阵，#保持列数一致
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()


X_train_vect = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(), columns=Vectorizer.get_feature_names())
X_train_vect2=X_train_vect.append(test)
X_train_vect2=X_train_vect2[0:len(X_train_vect)]
X_train_vect2.fillna(0, inplace=True)

print("X_train:",X_train_vect2.shape)
nb.fit(X_train_vect2, y_train)
train_score = nb.score(X_train_vect2, y_train)
# print(nb.predict_log_proba(X_train_vect2))
print(nb.predict(X_train_vect2))
print("X_train得分:",train_score)


#构建测试集矩阵
X_test_vect = pd.DataFrame(Vectorizer.fit_transform(X_test).toarray(), columns=Vectorizer.get_feature_names())
X_test_vect2=X_test_vect.append(test)
X_test_vect2=X_test_vect2[0:len(X_test_vect)]
X_test_vect2.fillna(0, inplace=True)

print("X_test:",X_test_vect2.shape)
print(nb.predict(X_test_vect2))
print(y_test)
test_score = nb.score(X_test_vect2, y_test)

print("X_test得分:",test_score)


# data2 = pd.read_csv("train.csv", encoding='UTF-8')
# #print(data.comment)
# data2['cut_comment'] = data2.comment.apply(chinese_word_cut)
# print(data2['cut_comment'][0])
# X2 = data2['cut_comment']
# y2 = data2.star
#
# X_test_vect2 = pd.DataFrame(Vectorizer.fit_transform(X2).toarray(), columns=Vectorizer.get_feature_names())
# print(X_test_vect2.shape)
# nb.predict_log_proba(X_test_vect2)
