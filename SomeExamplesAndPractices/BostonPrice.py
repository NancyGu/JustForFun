# coding : utf-8
# 2018-12-25 boston housing_price xgboost prediction

import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif']=['SimHei'] # To show Chinese Character
#plt.rcParams['axes.unicode.minus']=False # show -

# -1- get_dataset
from sklearn.datasets import load_boston
dir(load_boston())
#print(load_boston().DESCR)

# -2- extract x,y
x = load_boston().data
y = load_boston().target
df = pd.DataFrame(x,columns=load_boston().feature_names)
#print(df.shape) # (506,13)
#print(df.isnull().sum()) # 0 no-empty-data

# -3- EDA
# [1] crim
#Scatter

import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test =train_test_split(x,y,test_size=0.25)
gbm = lgb.LGBMRegressor(learning_rate=0.03,n_estimators=200,max_depth=8)
gbm.fit(X_train, y_train)
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration_)
print(y_pred)

