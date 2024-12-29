# import nltk
# nltk.download('stopwords')
# # 导入停用词库
# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('english'))
# # 打印停用词列表
# print(stop_words)


def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list
stop_words_file = 'end.txt'
stopwords = get_custom_stopwords(stop_words_file)


from sklearn.feature_extraction.text import CountVectorizer

Vectorizer = CountVectorizer(max_df = 0.8,
                            min_df = 3,
                            token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                            stop_words =frozenset(stopwords) )
