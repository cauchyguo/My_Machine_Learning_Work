# -*- coding: utf-8 -*-
# File: feature_extract.py

import pandas as pd
from datetime import *
import numpy as np

df = pd.read_csv("E:\PycharmProjects\O2O_work\ccf_offline_stage1_train.csv",keep_default_na=False)
df.columns = ['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received', 'date']

def get_date(date_str):
    '''得到具体日期'''
    return date(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))

def get_time_gap(recdate,condate):
    '''计算时间间隔'''
    return (get_date(condate) - get_date(recdate)).days

    
def get_label(str):
    '''打标'''
    s = str.split(':')
    if s[1] == 'null' or s[1] == 'nan':
        return 0
    elif get_time_gap(s[0],s[1]) <= 15:
        return 1
    else:
        return -1

#feature about user

def user_count_merchants_cal(df):
    '''用户去过的商家数'''
    frame = df[['user_id','merchant_id']][df.date != 'null']
    frame.columns = ['user_id', 'user_count_merchants']
    frame.drop_duplicates(inplace=True)
    frame.user_count_merchants = 1
    frame = frame.groupby('user_id').agg('sum').reset_index()
    return frame

def user_min_distance_cal(df):
    '''用户使用优惠券的最小距离'''
    frame = df[['user_id','distance']][(df.date != 'null') & (df.coupon_id != 'null')]
    frame.replace('null',-1,inplace=True)
    frame.distance = frame.distance.astype('int')
    frame.replace(-1,np.nan,inplace=True)
    frame = frame.groupby('user_id').agg('min').reset_index()
    frame.columns = ['user_id','user_min_distance']
    return frame

def user_max_distance_cal(df):
    '''用户使用优惠券的最大距离'''
    frame = df[['user_id','distance']][(df.date != 'null') & (df.coupon_id != 'null')]
    frame.replace('null',-1,inplace=True)
    frame.distance = frame.distance.astype('int')
    frame.replace(-1,np.nan,inplace=True)
    frame = frame.groupby('user_id').agg('max').reset_index()
    frame.columns = ['user_id','user_max_distance']
    return frame

def user_most_distance_cal(df):
    '''用户使用优惠券最多的距离'''
    frame = df[['user_id','distance']][(df.date != 'null') & (df.coupon_id != 'null') & (df.distance != 'null')]
    # frame.replace('null',-1,inplace=True)
    frame.distance = frame.distance.astype('int')
    # frame.replace(-1,np.nan,inplace=True)
    frame = frame.groupby('user_id').agg(lambda x: x.value_counts().index[0]).reset_index()
    frame.columns = ['user_id','user_most_distance']
    return frame

def user_avg_distance_cal(df):
    '''用户使用优惠券的平均距离'''
    frame = df[['user_id','distance']][(df.date != 'null') & (df.coupon_id != 'null')]
    frame.replace('null',-1,inplace=True)
    frame.distance = frame.distance.astype('int')
    frame.replace(-1,np.nan,inplace=True)
    frame = frame.groupby('user_id').agg('mean').reset_index()
    frame.columns = ['user_id','user_avg_distance']
    return frame

user_distance_relat = [user_min_distance_cal,user_max_distance_cal,
                 user_most_distance_cal,user_avg_distance_cal]

def buy_total_cal(df):
    '''用户总的消费次数'''
    frame = df[df.date != 'null'][['user_id']]
    frame['buy_total'] = 1
    frame = frame.groupby('user_id').agg('sum').reset_index()
    return frame

def buy_use_coupon_cal(df):
    '''用户使用优惠券的次数'''
    frame = df[(df.date != 'null') & (df.coupon_id != 'null')][['user_id','coupon_id']]
    frame['buy_use_coupon'] = 1
    frame = frame.groupby('user_id').agg('sum').reset_index()
    return frame


def user_coupon_received_cal(df):
    '''用户领取到的优惠券的数量'''
    frame = df[df.coupon_id != 'null'][['user_id']]
    frame['user_coupon_received'] = 1
    frame = frame.groupby('user_id').agg('sum').reset_index()
    return frame

user_buy_relat = [buy_total_cal,buy_use_coupon_cal,user_coupon_received_cal]

def user_time_gap_cal(df):
    '''用户使用优惠券的时间间隔'''
    frame = df[['user_id','date_received','date']][(df.date != 'null') & (df.date_received != 'null')]
    frame['user_time_gap'] = frame.apply(lambda row:get_time_gap(row['date_received'],row['date']), axis=1)
    return frame[['user_id','user_time_gap']]

def user_avg_time_gap_cal(df):
    '''用户使用优惠券的平均时间间隔'''
    frame = df[['user_id', 'date_received', 'date']][(df.date != 'null') & (df.date_received != 'null')]
    frame['user_avg_time_gap'] = frame.apply(lambda row:get_time_gap(row['date_received'],row['date']), axis=1)
    frame = frame.groupby('user_id').agg('mean').reset_index()
    return frame

def user_max_time_gap_cal(df):
    '''用户使用优惠券的最长时间间隔'''
    frame = df[['user_id', 'date_received', 'date']][(df.date != 'null') & (df.date_received != 'null')]
    frame['user_max_time_gap'] = frame.apply(lambda row:get_time_gap(row['date_received'],row['date']), axis=1)
    frame = frame.groupby('user_id').agg('max').reset_index()
    return frame[['user_id','user_max_time_gap']]

def user_min_time_gap_cal(df):
    '''用户使用优惠券的最短时间间隔'''
    frame = df[['user_id', 'date_received', 'date']][(df.date != 'null') & (df.date_received != 'null')]
    frame['user_min_time_gap'] = frame.apply(lambda row:get_time_gap(row['date_received'],row['date']), axis=1)
    frame = frame.groupby('user_id').agg('min').reset_index()
    return frame[['user_id','user_min_time_gap']]

def user_most_time_gap_cal(df):
    '''用户使用优惠券的最多的时间间隔'''
    frame = df[['user_id', 'date_received', 'date']][(df.date != 'null') & (df.date_received != 'null')]
    frame['user_most_time_gap'] = frame.apply(lambda row:get_time_gap(row['date_received'],row['date']), axis=1)
    frame = frame.groupby('user_id').agg(lambda x: x.value_counts().index[0]).reset_index()
    return frame[['user_id','user_most_time_gap']]

user_time_gap_relat = [user_time_gap_cal,user_avg_time_gap_cal,user_max_time_gap_cal,
                 user_min_time_gap_cal,user_most_time_gap_cal]

def user_max_discount_rate_cal(df):
    '''用户核销优惠券的最高折扣率'''
    frame = df[['user_id','discount_rate']][(df.date_received != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['user_id','user_max_discount_rate']
    frame = frame.groupby('user_id').agg('max').reset_index()
    return frame

def user_min_discount_rate_cal(df):
    '''用户核销优惠券的最低折扣率'''
    frame = df[['user_id','discount_rate']][(df.date_received != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['user_id','user_min_discount_rate']
    frame = frame.groupby('user_id').agg('min').reset_index()
    return frame

def user_avg_discount_rate_cal(df):
    '''用户核销优惠券的平均折扣率'''
    frame = df[['user_id','discount_rate']][(df.date_received != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['user_id','user_avg_discount_rate']
    frame = frame.groupby('user_id').mean().reset_index()
    return frame

# def user_most_discount_rate_cal(df):
#     '''用户核销优惠券的众数折扣率'''
#     frame = df[['user_id','discount_rate']][(df.date_received != 'null') & (df.discount_rate != 'null')]
#     frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
#     frame.columns = ['user_id','user_most_discount_rate']
#     frame = frame.groupby('user_id').agg(lambda x: x.value_counts().index[0]).reset_index()
#     return frame

user_discount_rate_relat = [user_max_discount_rate_cal,user_min_discount_rate_cal,user_avg_discount_rate_cal]

def add_user_feature(df):
    user_features = [user_count_merchants_cal]
    user_features.extend(user_distance_relat)
    user_features.extend(user_buy_relat)
    user_features.extend(user_time_gap_relat)
    user_features.extend(user_discount_rate_relat)

    user_feature_data = df[['user_id']].drop_duplicates('user_id')
    for fun in user_features:
        frame = fun(df)
        user_feature_data = pd.merge(user_feature_data,frame, on='user_id', how='left')

    user_feature_data.buy_use_coupon = user_feature_data.buy_use_coupon.replace(np.nan, 0)
    # 用户使用优惠券购买的比例
    user_feature_data['user_buy_use_coupon_rate'] = user_feature_data.buy_use_coupon.astype('float') / \
                                                    user_feature_data.buy_total.astype('float')
    # 用户领取到的优惠券核销率
    user_feature_data['user_coupon_trans_rate'] = user_feature_data.buy_use_coupon.astype('float') / \
                                                  user_feature_data.user_coupon_received.astype('float')
    # 用户平均在每个商家的核销慈湖
    user_feature_data['user_avg_cons_of_merchant'] = user_feature_data.buy_total.astype('float') / \
                                                     user_feature_data.user_count_merchants.astype('float')
    # 用户平均在每个商家的核销优惠券次数
    user_feature_data['user_avg_coupon_of_merchant'] = user_feature_data.buy_use_coupon.astype('float') / \
                                                       user_feature_data.user_count_merchants.astype('float')
    # user_feature_data.user_count_merchants = user_feature_data.user_count_merchants.replace(np.nan, 0)
    # user_feature_data.buy_total = user_feature_data.buy_total.replace(np.nan, 0)
    # user_feature_data = user_feature_data.user_coupon_received.replace(np.nan, 0)

    return user_feature_data



# feature about merchant

def total_sales_cal(df):
    '''商家总的交易次数'''
    frame = df[['merchant_id']][df.date != 'null']
    # frame.drop_duplicates(inplace=True)
    frame['total_sales'] = 1
    frame = frame.groupby('merchant_id').agg('sum').reset_index()
    return frame

def total_coupon_cal(df):
    '''商家的优惠券发行数量'''
    frame = df[['merchant_id']][df.coupon_id != 'null']
    frame['total_coupon'] = 1
    frame = frame.groupby('merchant_id').agg('sum').reset_index()
    return frame

def total_coupon_types_cal(df):
    '''商家发行的优惠券种类数'''
    frame = df[['merchant_id','discount_rate']][df.discount_rate != 'null']
    frame.drop_duplicates(inplace=True)
    frame.discount_rate = 1
    frame = frame.groupby('merchant_id').agg('sum').reset_index()
    frame.columns = ['merchant_id','total_coupon_types']
    return frame

def coupon_sales_cal(df):
    '''商家优惠券交易的数量'''
    frame = df[['merchant_id']][(df.coupon_id != 'null') & (df.date != 'null')]
    frame['coupon_sales'] = 1
    frame = frame.groupby('merchant_id').agg('sum').reset_index()
    return frame

merchant_sales_relat = [total_sales_cal,total_coupon_cal,total_coupon_types_cal,coupon_sales_cal]

def merchant_coupon_sales_rate_cal(df):
    '''商家优惠券交易占比率'''
    df.total_sales.replace(np.nan, 0,inplace=True)
    df['merchant_coupon_sales_rate'] = df.coupon_sales.astype('float') / df.total_sales
    return df

def merchant_coupon_used_rate_cal(df):
    '''商家优惠券被使用率'''
    df.coupon_sales.replace(np.nan, 0, inplace=True)
    df['merchant_coupon_used_rate'] = df.coupon_sales.astype('float') / df.total_coupon
    df.total_coupon.replace(np.nan, 0, inplace=True)
    return df

def merchant_avg_distance_cal(df):
    '''商家优惠券交易的平均距离'''
    frame = df[['merchant_id', 'distance']][(df.date != 'null') & (df.coupon_id != 'null') & (df.distance != 'null')]
    # frame.replace('null', -1, inplace=True)
    frame.distance = frame.distance.astype('int')
    # frame.replace(-1, np.nan, inplace=True)
    frame = frame.groupby('merchant_id').agg('mean').reset_index()
    frame.columns = ['merchant_id','merchant_avg_distance']
    return frame

def merchant_max_distance_cal(df):
    '''商家优惠券交易的最大距离'''
    frame = df[['merchant_id', 'distance']][(df.date != 'null') & (df.coupon_id != 'null') & (df.distance != 'null')]
    # frame.replace('null', -1, inplace=True)
    frame.distance = frame.distance.astype('int')
    # frame.replace(-1, np.nan, inplace=True)
    frame = frame.groupby('merchant_id').agg('max').reset_index()
    frame.columns = ['merchant_id','merchant_max_distance']
    return frame

def merchant_min_distance_cal(df):
    '''商家优惠券交易的最小距离'''
    frame = df[['merchant_id', 'distance']][(df.date != 'null') & (df.coupon_id != 'null') & (df.distance != 'null')]
    # frame.replace('null', -1, inplace=True)
    frame.distance = frame.distance.astype('int')
    # frame.replace(-1, np.nan, inplace=True)
    frame = frame.groupby('merchant_id').agg('min').reset_index()
    frame.columns = ['merchant_id','merchant_min_distance']
    return frame

def merchant_most_distance_cal(df):
    '''商家优惠券交易的众数距离'''
    frame = df[['merchant_id', 'distance']][(df.date != 'null') & (df.coupon_id != 'null') & (df.distance != 'null')]
    # frame.replace('null', -1, inplace=True)
    frame.distance = frame.distance.astype('int')
    # frame.replace(-1, np.nan, inplace=True)
    frame = frame.groupby('merchant_id').agg(lambda x: x.value_counts().index[0]).reset_index()
    frame.columns = ['merchant_id','merchant_most_distance']
    return frame

merchant_distance_relat = [merchant_avg_distance_cal,merchant_max_distance_cal,
                           merchant_min_distance_cal,merchant_most_distance_cal]

def merchant_max_discount_rate_cal(df):
    '''商家发行优惠券的最高折扣率'''
    frame = df[['merchant_id','discount_rate']][(df.coupon_id != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['merchant_id','merchant_max_discount_rate']
    frame = frame.groupby('merchant_id').agg('max').reset_index()
    return frame

def merchant_min_discount_rate_cal(df):
    '''商家发行优惠券的最低折扣率'''
    frame = df[['merchant_id','discount_rate']][(df.coupon_id != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['merchant_id','merchant_min_discount_rate']
    frame = frame.groupby('merchant_id').agg('min').reset_index()
    return frame

def merchant_avg_discount_rate_cal(df):
    '''商家发行优惠券的平均折扣率'''
    frame = df[['merchant_id','discount_rate']][(df.coupon_id != 'null') & (df.discount_rate != 'null')]
    frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
    frame.columns = ['merchant_id','merchant_avg_discount_rate']
    frame = frame.groupby('merchant_id').agg('mean').reset_index()
    return frame

# def merchant_most_discount_rate_cal(df):
#     '''商家发行优惠券的众数折扣率'''
#     frame = df[['merchant_id','discount_rate']][(df.coupon_id != 'null') & (df.discount_rate != 'null')]
#     frame.discount_rate = frame.discount_rate.apply(get_discount_rate)
#     frame.columns = ['merchant_id','merchant_most_discount_rate']
#     frame = frame.groupby('merchant_id').agg(lambda x: x.value_counts().index[0]).reset_index()
#     return frame

merchant_discount_rate_relat = [merchant_max_discount_rate_cal,merchant_min_discount_rate_cal,merchant_avg_discount_rate_cal]

def add_merchant_feature(df):
    merchant_features = []
    merchant_features.extend(merchant_sales_relat)
    merchant_features.extend(merchant_distance_relat)
    merchant_features.extend(merchant_discount_rate_relat)

    merchant_feature_data = df[['merchant_id']].drop_duplicates('merchant_id')
    for fun in merchant_features:
        frame = fun(df)
        merchant_feature_data = pd.merge(merchant_feature_data,frame, on='merchant_id', how='left')

    merchant_feature_data = merchant_coupon_sales_rate_cal(merchant_feature_data)
    merchant_feature_data = merchant_coupon_used_rate_cal(merchant_feature_data)

    return merchant_feature_data



#feature about coupon(discount rate)

def is_man_jian_cal(s):
    '''优惠券类型（是否为满减类)'''
    s = str(s)
    s = s.split(':')
    if len(s) == 1:
        return 0
    else:
        return 1

def discount_man_cal(s):
    '''计算满减的满额'''
    s = str(s)
    s = s.split(':')
    if len(s) == 1:
        return 'null'
    else:
        return int(s[0])

def discount_jian_cal(s):
    '''计算满减的减额'''
    s = str(s)
    s = s.split(':')
    if len(s) == 1:
        return 'null'
    else:
        return int(s[1])

def get_discount_rate(s):
    '''将满减转化为实际优惠折扣率'''
    s = str(s)
    x = s.split(':')
    if  len(x) == 1:
        return float(s)
    elif len(x) > 1:
        return 1 - float(x[1]) / float(x[0])

def discount_rate_total_nums_cal(df):
    '''计算相同折扣率的优惠券发行数量'''
    frame = df[df.coupon_id.astype('str') != 'null'][['discount_rate']]
    frame['discount_rate_total_nums'] = 1
    frame.groupby('discount_rate').agg('sum').reset_index()
    return frame
#
# def discount_rate_used_nums_cal(df):
#     '''计算相同折扣率的优惠券核销数量'''
#     frame = df[['dicount_rate']][df.coupon_id.astype('str') != 'null' and df.date != 'null']
#     frame['discount_rate_used_nums'] = 1
#     frame.groupby('discount_rate').agg('sum').reset_index()
#     return frame

def day_of_week(str):
    '''得到该优惠券领取时的工作日'''
    return get_date(str).weekday() + 1

def day_of_month(str):
    '''得到该优惠券领取时的月份'''
    return get_date(str).month

def coupon_count_cal(df):
    '''统计相同id的优惠券的数量'''
    frame = df[['coupon_id']]
    frame['coupon_count'] = 1
    frame = frame.groupby('coupon_id').agg('sum').reset_index()
    return frame

# coupon_discout__relat = [is_man_jian_cal,discount_rate_total_nums_cal]
def add_coupon_feature(df):
    df['day_of_week'] = df.date_received.astype('str').apply(day_of_week)
    df['day_of_month'] = df.date_received.astype('str').apply(day_of_month)
    df['is_man_jian'] = df.discount_rate.apply(is_man_jian_cal)
    df['discount_man'] = df.discount_rate.apply(discount_man_cal)
    df['discount_jian'] = df.discount_rate.apply(discount_jian_cal)
    df['discount_rate'] = df.discount_rate.apply(get_discount_rate)

    print('666')
    # df = pd.merge(df,discount_rate_total_nums_cal(df),on='discount_rate',how='left')
    # df = df.merge(discount_rate_used_nums_cal(df),on='discount_rate',how='left')
    # df['discount_rate_trans_rate'] = df.discount_rate_used_nums.astype(float) / df.discount_rate_total_nums.astype('float')

    df = df.merge(coupon_count_cal(df),on='coupon_id',how='left')

    return df

# feature between user and merchant
def user_merchant_buy_total_cal(df):
    '''用户在该商家的总消费次数'''
    frame = df[['user_id','merchant_id']][df.date != 'null']
    frame['user_merchant_buy_total'] = 1
    frame = frame.groupby(['user_id','merchant_id']).agg('sum').reset_index()
    frame.drop_duplicates(inplace=True)
    return frame

def user_merchant_received_cal(df):
    '''用户在该商家收到的优惠券总数'''
    frame = df[['user_id','merchant_id']][df.coupon_id != 'null']
    frame['user_merchant_received'] = 1
    frame = frame.groupby(['user_id', 'merchant_id']).agg('sum').reset_index()
    frame.drop_duplicates(inplace=True)
    return frame

def user_merchant_buy_use_coupon_cal(df):
    '''用户在该商家购物使用的优惠券数量'''
    frame = df[['user_id', 'merchant_id']][(df.coupon_id != 'null') & (df.date != 'null')]
    frame['user_merchant_buy_use_coupon'] = 1
    frame = frame.groupby(['user_id', 'merchant_id']).agg('sum').reset_index()
    frame.drop_duplicates(inplace=True)
    return frame

def user_merchant_buy_no_coupon_cal(df):
    '''用户在该商家购物不使用的优惠券数量'''
    frame = df[['user_id', 'merchant_id']][(df.coupon_id == 'null') & (df.date != 'null')]
    frame['user_merchant_buy_no_coupon'] = 1
    frame = frame.groupby(['user_id', 'merchant_id']).agg('sum').reset_index()
    frame.drop_duplicates(inplace=True)
    return frame

# def user_merchant_records_cal(df):
#     '''用户商家总记录条数'''
#     frame = df[['user_id', 'merchant_id']]
#     frame['user_merchant_records'] = 1
#     frame = frame.groupby(['user_id', 'merchant_id']).agg('sum').reset_index()
#     frame.drop_duplicates(inplace=True)
#     return frame

user_merchant_relat = [user_merchant_buy_total_cal,user_merchant_received_cal,
                       user_merchant_buy_use_coupon_cal,user_merchant_buy_no_coupon_cal]

def add_user_merchant_feature(df):
    user_merchant_features = user_merchant_relat

    user_merchant_data = df[['user_id', 'merchant_id']]
    user_merchant_data.drop_duplicates(inplace=True)
    for fun in user_merchant_features:
        frame = fun(df)
        user_merchant_data = pd.merge(user_merchant_data,frame,on=['user_id', 'merchant_id'],how='left')

    user_merchant_data['user_merchant_coupon_trans_rate'] = user_merchant_data.user_merchant_buy_use_coupon.astype('float') / \
        user_merchant_data.user_merchant_received.astype('float')
    user_merchant_data['user_merchant_use_coupon_rate'] = user_merchant_data.user_merchant_buy_use_coupon.astype('float') / \
        user_merchant_data.user_merchant_buy_total.astype('float')
    user_merchant_data['user_merchant_no_coupon_rate'] = user_merchant_data.user_merchant_buy_no_coupon.astype('float') / \
        user_merchant_data.user_merchant_buy_total.astype('float')
    # user_merchant_data['user_merchant_record_rate'] = user_merchant_data.user_merchant_buy_use_coupon.astype('float') / \
    #     user_merchant_data.user_merchant_records.astype('float')

    # user_merchant_data.pop('date')
    return user_merchant_data

# # other feature
# def til_now_receive_coupon_cal(df):
#     '''该用户截止当天收到的优惠券数量'''
#     frame = df[['user_id']][df.date_received != 'null']
#     frame['this_month_receive_coupon'] = 1
#     frame = frame.groupby('user_id').agg('sum').reset_index()
#     return frame

def nowday_receive_coupon_cal(df):
    '''当天收到的优惠券数量'''
    frame = df[['user_id','date_received']][df.date_received != 'null']
    frame['nowday_receive_coupon'] = 1
    frame = frame.groupby(['user_id','date_received']).agg('sum').reset_index()
    return frame

def user_first_same_coupon_date_cal(df):
    '''收到第一张同样优惠券的时间'''
    frame = df[['user_id','coupon_id','date_received']][df.date_received != 'null']
    frame.date_received = frame.date_received.astype('int')
    frame = frame.groupby(['user_id','coupon_id']).agg('min').reset_index()
    frame.columns = ['user_id','coupon_id','user_first_same_coupon_date']
    return frame

def user_last_same_coupon_date_cal(df):
    '''收到最后一张同样优惠券的时间'''
    frame = df[['user_id','coupon_id','date_received']][df.date_received != 'null']
    frame.date_received = frame.date_received.astype('int')
    frame = frame.groupby(['user_id','coupon_id']).agg('max').reset_index()
    frame.columns = ['user_id','coupon_id','user_last_same_coupon_date']
    return frame

def is_firstlastone(x):
    if x == 0:
        return 1
    elif x > 0:
        return 0

def add_other_feature(df):
    other_feature_data = df[['user_id','coupon_id','date_received']][df.date_received != 'null']
    other_feature_data = pd.merge(other_feature_data,nowday_receive_coupon_cal(df),on=['user_id','date_received'],how='left')
    other_feature_data = pd.merge(other_feature_data,user_first_same_coupon_date_cal(df),on=['user_id','coupon_id'],how='left')
    other_feature_data = pd.merge(other_feature_data,user_last_same_coupon_date_cal(df),on=['user_id','coupon_id'],how='left')
    other_feature_data['is_first'] = other_feature_data.date_received.astype('int') - other_feature_data.user_first_same_coupon_date.astype('int')
    other_feature_data['is_last'] = other_feature_data.user_last_same_coupon_date.astype('int') - other_feature_data.date_received.astype('int')
    other_feature_data.is_first = other_feature_data.is_first.apply(is_firstlastone)
    other_feature_data.is_last = other_feature_data.is_last.apply(is_firstlastone)

    return other_feature_data


















