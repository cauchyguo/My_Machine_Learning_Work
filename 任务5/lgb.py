#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Cauchy
@file: lgb.py
@time: 2019/9/4 21:56
"""
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler


# 提取了特征的训练集
dataset1 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset1.csv')
dataset1.label.replace(-1, 0, inplace=True)

# 提取了特征的要预测的数据集
dataset2 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset3.csv')

dataset1.drop_duplicates(inplace=True)
dataset2.drop_duplicates(inplace=True)

dataset1 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset1.csv')
dataset1.label.replace(-1, 0, inplace=True)
dataset2 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset2.csv')
dataset2.label.replace(-1, 0, inplace=True)
dataset3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset3.csv')

# dataset1.drop_duplicates(inplace=True)
# dataset2.drop_duplicates(inplace=True)
# dataset3.drop_duplicates(inplace=True)

dataset12 = pd.concat([dataset1,dataset2],axis=0)

dataset1_y = dataset1.label
dataset1_x = dataset1.drop(['user_id','label'],axis=1)  # 'day_gap_before','day_gap_after' cause overfitting, 0.77
dataset2_y = dataset2.label
dataset2_x = dataset2.drop(['user_id','label'],axis=1)
dataset12_y = dataset12.label
dataset12_x = dataset12.drop(['user_id','label',],axis=1)
dataset3_preds = dataset3[['user_id','coupon_id','date_received']]
dataset3_x = dataset3.drop(['user_id','coupon_id','date_received',],axis=1)

# dataset1_y = dataset1.label
# dataset1_x = dataset1.drop(['user_id','label'],axis=1)
#
# dataset2_preds = dataset2[['user_id','coupon_id','date_received']]
# dataset2_x = dataset2.drop(['user_id','coupon_id','date_received'],axis=1)


params = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'learning_rate': 0.03,
    'metric':'auc',
    'lambda_l1': 0.1,
    'lambda_l2': 0.2,
    'max_depth': 6,
    'num_leaves': 31,
    'min_child_weight': 25,
    # 'device':'gpu'
}

if __name__ == '__main__':
    scaler = MinMaxScaler()
    X = dataset12_x
    train_X = scaler.fit_transform(X)
    train_Y = dataset12_y
    x_pred = scaler.fit_transform(dataset3_x)

    # train_X, val_X,train_Y,val_Y = train_test_split(train_X,train_Y,test_size=0.1)

    X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\O2O_work\models\model_lgb.txt')
    y_pred = gbm.predict(x_pred, num_iteration=gbm.best_iteration)


    # y_val = gbm.predict(val_X,num_iteration=gbm.best_iteration)
    print("Val result:\n")
    # print(accuracy_score(val_Y,y_val))
    dataset3_preds['auc'] = pd.Series(pd.Series(y_pred))
    dataset3_preds.to_csv(r'data\lgm_result3.csv',header=None,columns=None,index=False)