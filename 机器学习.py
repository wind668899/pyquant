# from sklearn import datasets#引入数据集,sklearn包含众多数据集
# from sklearn.model_selection import train_test_split#将数据分为测试集和训练集
# from sklearn.neighbors import KNeighborsClassifier#利用邻近点方式训练数据
#
# iris = datasets.load_iris()  # 引入iris鸢尾花数据,iris数据包含4个特征变量
# print(iris)
#
# print('-------------------')
# iris_X = iris.data  # 特征变量
# iris_y = iris.target  # 目标值
# X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)  # 利用train_test_split进行将训练集和测试集进行分开，test_size占30%
# #print(y_train)  # 我们看到训练数据的特征值分为3类
# print('------------------------------')
# '''
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2]
# '''
#
# ###训练数据###
# knn = KNeighborsClassifier()  # 引入训练方法
# knn.fit(X_train, y_train)  # 进行填充测试数据进行训练
#
# ###预测数据###
# #print(knn.predict(X_test))  # 预测特征值
# '''
# [1 1 1 0 2 2 1 1 1 0 0 0 2 2 0 1 2 2 0 1 0 0 0 0 0 0 2 1 0 0 0 1 0 2 0 2 0
# 1 2 1 0 0 1 0 2]
# '''
# print('---------------------------------')
# #print(y_test)  # 真实特征值
# '''
# [1 1 1 0 1 2 1 1 1 0 0 0 2 2 0 1 2 2 0 1 0 0 0 0 0 0 2 1 0 0 0 1 0 2 0 2 0
# 1 2 1 0 0 1 0 2]
# '''


# from sklearn import datasets
# from sklearn.linear_model import LinearRegression  # 引入线性回归模型
#
# ###引入数据###
# load_data = datasets.load_boston()
# print(type(load_data))
# data_X = load_data.data
# data_y = load_data.target
# # print(type(data_X))
# # for i in data_X:
# #     print(type(i))
# #print(type(data_y))
# #print(len(data_X))
#
# #print('----------------')
# #print(data_X.shape)
# #print('--------------')
# # (506, 13)data_X共13个特征变量
#
# ###训练数据###
# model = LinearRegression()
# model.fit(data_X, data_y)
# model.predict(data_X[:4, :])  # 预测前4个数据
#
# ###属性和功能###
# print(model.coef_)
# print(model.get_params())
# '''
# [ -1.07170557e-01 4.63952195e-02 2.08602395e-02 2.68856140e+00
# -1.77957587e+01 3.80475246e+00 7.51061703e-04 -1.47575880e+00
# 3.05655038e-01 -1.23293463e-02 -9.53463555e-01 9.39251272e-03
# -5.25466633e-01]
# '''

# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
#
# ###引入数据###
# iris = load_iris()
# X = iris.data
# y = iris.target
#
# ###训练数据###
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# # 引入交叉验证,数据分为5组进行训练
# print(X_train)
# print(y_train)
#
# from sklearn.model_selection import cross_val_score
#
# knn = KNeighborsClassifier(n_neighbors=5)  # 选择邻近的5个点
# scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')  # 评分方式为accuracy
# print(scores)  # 每组的评分结果
# # [ 0.96666667 1. 0.93333333 0.96666667 1. ]5组数据
# print(scores.mean())  # 平均评分结果
# # 0.973333333333
#
# if __name__=='__main__':

#print(model.intercept_)
# 36.4911032804
#print(model.get_params())  # 得到模型的参数
# {'copy_X': True, 'normalize': False, 'n_jobs': 1, 'fit_intercept': True}
#print(model.score(data_X, data_y))  # 对训练情况进行打分
# 0.740607742865

if __name__=='__main__':
    a=int(input())
    b=list(map(int,input().split(' ')))
    print(a)
    print(b)