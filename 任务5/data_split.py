import pandas as pd
import numpy as np

from feature_extract import *
#
if __name__ == '__main__':
    off_train = pd.read_csv(r'E:\PycharmProjects\O2O_work\ccf_offline_stage1_train.csv',
                            keep_default_na=False)
    off_train.columns = ['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received', 'date']
    off_test = pd.read_csv(r'E:\PycharmProjects\O2O_work\ccf_offline_stage1_test_revised.csv',
                           keep_default_na=False)
    off_test.columns = ['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received']
    on_train = pd.read_csv(r'E:\PycharmProjects\O2O_work\ccf_online_stage1_train.csv',
                           keep_default_na=False)
    on_train.columns = ['user_id', 'merchant_id', 'action', 'coupon_id', 'discount_rate', 'date_received', 'date']


    off_train = off_train[off_train.date_received != 'null']

    dataset3 = off_test
    feature3 = off_train[((off_train.date >= '20160315') & (off_train.date <= '20160630')) | ((
            (off_train.date == 'null') & (off_train.date_received >= '20160315') & (
            off_train.date_received <= '20160630')))]
    dataset2 = off_train[(off_train.date_received >= '20160515') & (off_train.date_received <= '20160615')]
    feature2 = off_train[((off_train.date >= '20160201') & (off_train.date <= '20160514')) | ((
            (off_train.date == 'null') & (off_train.date_received >= '20160201') & (
            off_train.date_received <= '20160514')))]
    dataset1 = off_train[(off_train.date_received >= '20160414') & (off_train.date_received <= '20160514')]
    feature1 = off_train[((off_train.date >= '20160101') & (off_train.date <= '20160413')) | ((
            (off_train.date == 'null') & (off_train.date_received >= '20160101') & (
            off_train.date_received <= '20160413')))]

    # user3 = feature3[['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received', 'date']]
    # user_feature_data = add_user_feature(user3)
    # user_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_feature3.csv",index=False)
    #
    # user2 = feature2[['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received', 'date']]
    # user_feature_data = add_user_feature(user2)
    # user_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_feature2.csv",index=False)
    #
    # user1 = feature1[['user_id', 'merchant_id', 'coupon_id', 'discount_rate', 'distance', 'date_received', 'date']]
    # user_feature_data = add_user_feature(user1)
    # user_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_feature1.csv",index=False)
    #
    #
    # merchant3 = feature3[['merchant_id', 'coupon_id', 'discount_rate','distance', 'date_received', 'date']]
    # merchant_feature_data = add_merchant_feature(merchant3)
    # merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\merchant3_feature.csv",index=False)
    #
    # merchant2 = feature2[['merchant_id', 'coupon_id', 'discount_rate','distance', 'date_received', 'date']]
    # merchant_feature_data = add_merchant_feature(merchant2)
    # merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\merchant2_feature.csv",index=False)
    #
    # merchant1 = feature1[['merchant_id', 'coupon_id', 'discount_rate','distance', 'date_received', 'date']]
    # merchant_feature_data = add_merchant_feature(merchant1)
    # merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\merchant1_feature.csv",index=False)
    #
    #
    # coupon3 = dataset3[['user_id','merchant_id','coupon_id', 'discount_rate','date_received']]
    # coupon_feature_data = add_coupon_feature(coupon3)
    # coupon_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\coupon3_feature.csv",index=False)
    #
    # coupon2 = dataset2[['user_id','coupon_id','merchant_id', 'discount_rate','date_received','date']]
    # coupon_feature_data = add_coupon_feature(coupon2)
    # coupon_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\coupon2_feature.csv",index=False)
    #
    # coupon1 = dataset1[['user_id','coupon_id','merchant_id','discount_rate','date_received','date']]
    # coupon_feature_data = add_coupon_feature(coupon1)
    # coupon_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\coupon1_feature.csv",index=False)
    #
    # #
    # user_merchant3 = feature3[['user_id','merchant_id','coupon_id','date']]
    # user_merchant_feature_data = add_user_merchant_feature(user_merchant3)
    # user_merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_merchant3_feature.csv", index=False)
    #
    # user_merchant2 = feature2[['user_id','merchant_id','coupon_id','date']]
    # user_merchant_feature_data = add_user_merchant_feature(user_merchant2)
    # user_merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_merchant2_feature.csv", index=False)
    #
    # user_merchant1 = feature1[['user_id','merchant_id','coupon_id','date']]
    # user_merchant_feature_data = add_user_merchant_feature(user_merchant1)
    # user_merchant_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\user_merchant1_feature.csv", index=False)


    other_feature3 = dataset3[['user_id','coupon_id','date_received']]
    other_feature_data = add_other_feature(other_feature3)
    other_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\other_feature3.csv", index=False)

    other_feature2 = dataset2[['user_id','coupon_id','date_received']]
    other_feature_data = add_other_feature(other_feature2)
    other_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\other_feature2.csv", index=False)

    other_feature1 = dataset1[['user_id','coupon_id','date_received']]
    other_feature_data = add_other_feature(other_feature1)
    other_feature_data.to_csv(r"E:\PycharmProjects\O2O_work\data\other_feature1.csv", index=False)



    coupon3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\coupon3_feature.csv')
    merchant3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\merchant3_feature.csv')
    user3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_feature3.csv')
    user_merchant3 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_merchant3_feature.csv')
    other_feature3 = pd.read_csv(r"E:\PycharmProjects\O2O_work\data\other_feature3.csv")
    dataset3 = pd.merge(coupon3, merchant3, on='merchant_id', how='left')
    dataset3 = pd.merge(dataset3, user3, on='user_id', how='left')
    dataset3 = pd.merge(dataset3, user_merchant3, on=['user_id', 'merchant_id'], how='left')
    dataset3 = pd.merge(dataset3, other_feature3, on=['user_id', 'coupon_id', 'date_received'], how='left')
    dataset3.drop_duplicates(inplace=True)



    dataset3.user_merchant_buy_total = dataset3.user_merchant_buy_total.replace(np.nan, 0)
    dataset3.user_merchant_received = dataset3.user_merchant_received.replace(np.nan, 0)
    dataset3['is_weekend'] = dataset3.day_of_week.apply(lambda x: 1 if x in (6, 7) else 0)
    weekday_dummies = pd.get_dummies(dataset3.day_of_week)
    weekday_dummies.columns = ['weekday' + str(i + 1) for i in range(weekday_dummies.shape[1])]
    dataset3 = pd.concat([dataset3, weekday_dummies], axis=1)
    dataset3.drop(['merchant_id', 'day_of_week', 'coupon_count'], axis=1, inplace=True)
    dataset3 = dataset3.replace('null', np.nan)
    dataset3.to_csv('E:\PycharmProjects\O2O_work\dataset3.csv', index=None)
#
    coupon2 = pd.read_csv('E:\PycharmProjects\O2O_work\data\coupon2_feature.csv')
    merchant2 = pd.read_csv('E:\PycharmProjects\O2O_work\data\merchant2_feature.csv')
    user2 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_feature2.csv')
    user_merchant2 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_merchant2_feature.csv')
    other_feature2 = pd.read_csv(r'data/other_feature2.csv')

    coupon2['label'] = coupon2.date_received.astype('str') + ':' + coupon2.date.astype('str')
    coupon2['label'] = coupon2.label.apply(get_label)

    dataset2 = pd.merge(coupon2, merchant2, on='merchant_id', how='left')
    dataset2 = pd.merge(dataset2, user2, on='user_id', how='left')
    dataset2 = pd.merge(dataset2, user_merchant2, on=['user_id', 'merchant_id'], how='left')
    dataset2 = pd.merge(dataset2, other_feature2, on=['user_id', 'coupon_id', 'date_received'], how='left')
    # dataset2['label'] = dataset2.date_received.astype('str') + ':' + dataset2.date.astype('str')
    # dataset2['label'] = dataset2.label.apply(get_label)
    dataset2.drop_duplicates(inplace=True)



    dataset2.user_merchant_buy_total = dataset2.user_merchant_buy_total.replace(np.nan, 0)
    dataset2.user_merchant_received = dataset2.user_merchant_received.replace(np.nan, 0)
    dataset2['is_weekend'] = dataset2.day_of_week.apply(lambda x: 1 if x in (6, 7) else 0)
    weekday_dummies = pd.get_dummies(dataset2.day_of_week)
    weekday_dummies.columns = ['weekday' + str(i + 1) for i in range(weekday_dummies.shape[1])]
    dataset2 = pd.concat([dataset2, weekday_dummies], axis=1)
    dataset2.drop(['merchant_id', 'day_of_week', 'date', 'date_received', 'coupon_id', 'coupon_count'], axis=1,
                  inplace=True)
    dataset2 = dataset2.replace('null', np.nan)
    dataset2.to_csv('E:\PycharmProjects\O2O_work\dataset2.csv', index=None)


    coupon1 = pd.read_csv('E:\PycharmProjects\O2O_work\data\coupon1_feature.csv')
    merchant1 = pd.read_csv('E:\PycharmProjects\O2O_work\data\merchant1_feature.csv')
    user1 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_feature1.csv')
    user_merchant1 = pd.read_csv(r'E:\PycharmProjects\O2O_work\data\user_merchant1_feature.csv')
    other_feature1 = pd.read_csv(r'data/other_feature1.csv')

    coupon1['label'] = coupon1.date_received.astype('str') + ':' + coupon1.date.astype('str')
    coupon1['label'] = coupon1.label.apply(get_label)

    dataset1 = pd.merge(coupon1, merchant1, on='merchant_id', how='left')
    dataset1 = pd.merge(dataset1, user1, on='user_id', how='left')
    dataset1 = pd.merge(dataset1, user_merchant1, on=['user_id', 'merchant_id'], how='left')
    dataset1 = pd.merge(dataset1, other_feature1, on=['user_id', 'coupon_id', 'date_received'], how='left')
    # dataset1['label'] = dataset1.date_received.astype('str') + ':' + dataset1.date.astype('str')
    # dataset1['label'] = dataset1.label.apply(get_label)
    dataset1.drop_duplicates(inplace=True)



    dataset1.user_merchant_buy_total = dataset1.user_merchant_buy_total.replace(np.nan, 0)
    dataset1.user_merchant_received = dataset1.user_merchant_received.replace(np.nan, 0)
    dataset1['is_weekend'] = dataset1.day_of_week.apply(lambda x: 1 if x in (6, 7) else 0)
    weekday_dummies = pd.get_dummies(dataset1.day_of_week)
    weekday_dummies.columns = ['weekday' + str(i + 1) for i in range(weekday_dummies.shape[1])]
    dataset1 = pd.concat([dataset1, weekday_dummies], axis=1)
    dataset1.drop(['merchant_id', 'day_of_week', 'date', 'date_received', 'coupon_id', 'coupon_count'], axis=1,
                  inplace=True)
    dataset1 = dataset1.replace('null', np.nan)
    dataset1.to_csv('E:\PycharmProjects\O2O_work\dataset1.csv', index=None)


    print("Ok")
