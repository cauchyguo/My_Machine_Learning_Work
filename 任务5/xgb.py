# -*- coding: utf-8 -*-
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler

dataset1 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset1.csv')
dataset1.label.replace(-1, 0, inplace=True)
dataset2 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset2.csv')
dataset2.label.replace(-1, 0, inplace=True)
dataset3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\dataset3.csv')

dataset1.drop_duplicates(inplace=True)
dataset2.drop_duplicates(inplace=True)
dataset3.drop_duplicates(inplace=True)

dataset12 = pd.concat([dataset1,dataset2],axis=0)

dataset1_y = dataset1.label
dataset1_x = dataset1.drop(['user_id','label'],axis=1)  # 'day_gap_before','day_gap_after' cause overfitting, 0.77
dataset2_y = dataset2.label
dataset2_x = dataset2.drop(['user_id','label'],axis=1)
dataset12_y = dataset12.label
dataset12_x = dataset12.drop(['user_id','label'],axis=1)
dataset3_preds = dataset3[['user_id','coupon_id','date_received']]
dataset3_x = dataset3.drop(['user_id','coupon_id','date_received'],axis=1)

print (dataset1_x.shape,dataset2_x.shape,dataset3_x.shape)

# dataset1 = xgb.DMatrix(dataset1_x,label=dataset1_y)
# dataset2 = xgb.DMatrix(dataset2_x,label=dataset2_y)
dataset12 = xgb.DMatrix(dataset12_x,label=dataset12_y)
dataset3 = xgb.DMatrix(dataset3_x)

params={'booster':'gbtree',
	    'objective': 'rank:pairwise',
	    'eval_metric':'auc',
	    'gamma':0.1,
	    'min_child_weight':1,
	    'max_depth':5,
	    'lambda':10,
	    'subsample':0.7,
	    'colsample_bytree':0.8,
	    'colsample_bylevel':0.8,
	    'eta': 0.01,
	    'tree_method':'exact',
	    'seed':0,
	    'nthread':12
	    }

watchlist = [(dataset12,'train')]
model = xgb.train(params,dataset12,num_boost_round=3500,evals=watchlist)

#添加观察窗口
#predict test set
dataset3_preds['label'] = model.predict(dataset3)
dataset3_preds.label = MinMaxScaler().fit_transform(dataset3_preds.label.values.reshape(-1, 1))
dataset3_preds.sort_values(by=['coupon_id','label'],inplace=True)
dataset3_preds.to_csv(r"E:\PycharmProjects\O2O_work\xgb_preds.csv",index=None,header=None)
print (dataset3_preds.describe())
    
#保存特征分数
feature_score = model.get_fscore()
feature_score = sorted(feature_score.items(), key=lambda x:x[1],reverse=True)
fs = []
for (key,value) in feature_score:
    fs.append("{0},{1}\n".format(key,value))
    
with open(r'E:\PycharmProjects\O2O_work\xgb_feature_score.csv','w') as f:
    f.writelines("feature,score\n")
    f.writelines(fs)

