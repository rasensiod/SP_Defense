import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from sklearn.preprocessing import StandardScaler
from keras.utils.np_utils import to_categorical # convert to one-hot-encoding


data_dir = '/scratch/zczqlzh/ddos_lab/dataset/01-12/'
df_path = '/scratch/zczqlzh/ddos_lab/dataset/01-12/df.csv'
df_path_0311 = '/scratch/zczqlzh/ddos_lab/dataset/03-11/df.csv'
df_path_merge = '/scratch/zczqlzh/ddos_lab/dataset/01-12/df_merge.csv'
df_merge_clean_path = '/scratch/zczqlzh/ddos_lab/dataset/01-12/df_clean.csv'


def merge_dataset():
    df_SYN = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/Syn.csv')
    df_MSSQL = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/MSSQL.csv')
    df_UDPLag = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/UDPLag.csv')
    df_LDAP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/LDAP.csv')
    df_UDP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/UDP.csv')
    df_Portmap = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/Portmap.csv')
    df_NetBIOS = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/03-11/NetBIOS.csv')
    df_0311 = pd.concat([df_SYN, df_MSSQL, df_UDPLag, df_LDAP, df_UDP, df_Portmap, df_NetBIOS], axis=0)
    df_0311.to_csv(df_path_0311)


    df_DrDoS_SNMP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_SNMP.csv')
    df_Syn = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/Syn.csv')
    df_DrDoS_NetBIOS = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_NetBIOS.csv')
    df_DrDoS_NTP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_NTP.csv')
    df_DrDoS_MSSQL = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_MSSQL.csv')
    df_DrDoS_LDAP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_LDAP.csv')
    df_TFTP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/TFTP.csv')
    df_DrDoS_SSDP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_SSDP.csv')
    df_UDPLag = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/UDPLag.csv')
    df_DrDoS_UDP = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_UDP.csv')
    df_DrDoS_DNS = pd.read_csv('/scratch/zczqlzh/ddos_lab/dataset/01-12/DrDoS_DNS.csv')
    df_0112 = pd.concat(
        [df_DrDoS_SNMP, df_Syn, df_DrDoS_NetBIOS, df_DrDoS_NTP, df_DrDoS_MSSQL, df_DrDoS_LDAP, df_TFTP, df_DrDoS_SSDP,
         df_UDPLag, df_DrDoS_UDP, df_DrDoS_DNS], axis=0)
    df_0112.to_csv(df_path)

    return df_0311, df_0112

    # df = pd.read_csv(df_path_merge)

def loading_dataset(df_0311, df_0112):
    df = pd.concat([df_0112, df_0311])
    df = df.drop(labels=['Unnamed: 0'], axis=1)
    df = df.drop(labels=['Unnamed: 0.1'], axis=1)
    return df

def feature_selection(df):
    ##types of object remove flowid and timestamp
    for col in df.columns:
        if df[col].dtypes == 'object':
            unique = len(df[col].unique())
            print("Feature '{col}' has {unique} categories".format(col=col, unique=unique))

    df = df.drop(labels=['Flow ID'], axis=1)
    df = df.drop(labels=[' Timestamp'], axis=1)
    df = df.drop(labels=[' Source IP'], axis=1)
    df = df.drop(labels=[' Destination IP'], axis=1)
    df = df.drop(labels=['SimillarHTTP'], axis=1)

    ##types of int:  Protocol
    list = []
    for col in df.columns:
        if df[col].dtypes == 'int64':
            unique = len(df[col].unique())
            if unique == 1:
                list.append(col)
            print("Feature '{col}' has {unique} categories".format(col=col, unique=unique))
    print("The following features have the same value:")
    print(list)

    for i in list:
        df = df.drop(labels=[i], axis=1)
        print(f"successfully remove the feature {i} which have the same value")

    ##types of float
    for col in df.columns:
        if df[col].dtypes == 'float64':
            unique = len(df[col].unique())
            print("Feature '{col}' has {unique} categories".format(col=col, unique=unique))
    print(df.shape)
    return df

def data_cleaning(df):
    df_nan = drop_nan(df)
    # drop nan, inplace means based on original df
    df.drop(index=df_nan, inplace=True)
    print(df.shape)
    decoder(df)
    df_inf = drop_infinity(df)
    df_inf.to_csv(df_merge_clean_path)
    df_weights = df_inf[' Label']
    class_weights = class_weight.compute_class_weight('balanced',
                                                      classes=np.unique(df_weights),
                                                      y=df_weights)
    class_weights = dict(enumerate(class_weights))

    df_std, df_Y = normalization(df_inf)
    return df_inf, df_std, df_Y, class_weights

def drop_nan(df):
    df_nan = df[df.isnull().T.any()]
    df_nan = df_nan.index.tolist()
    return df_nan

def decoder(df):
    df[' Label'].loc[df[' Label'] == 'BENIGN'] = 0
    df[' Label'].loc[df[' Label'] == 'TFTP'] = 1
    df[' Label'].loc[df[' Label'] == 'MSSQL'] = 2
    df[' Label'].loc[df[' Label'] == 'NetBIOS'] = 3
    df[' Label'].loc[df[' Label'] == 'UDP'] = 4
    df[' Label'].loc[df[' Label'] == 'Syn'] = 5
    df[' Label'].loc[df[' Label'] == 'DrDoS_SNMP'] = 6
    df[' Label'].loc[df[' Label'] == 'DrDoS_DNS'] = 7
    df[' Label'].loc[df[' Label'] == 'LDAP'] = 8
    df[' Label'].loc[df[' Label'] == 'DrDoS_SSDP'] = 9
    df[' Label'].loc[df[' Label'] == 'DrDoS_NTP'] = 10
    df[' Label'].loc[df[' Label'] == 'UDPLag'] = 11
    df[' Label'].loc[df[' Label'] == 'Portmap'] = 12
    df[' Label'].loc[df[' Label'] == 'WebDDoS'] = 13
    # avoid can not drop infinity below
    df[' Label'] = df[' Label'].astype("int64")
    return df

def drop_infinity(df):
    df_inf = df[np.isfinite(df).all(1)]
    return df_inf

def dividing_dataset(df_std, df_Y):
    # divide trainset and test set
    train_X, test_X, train_y, test_y = train_test_split(df_std, df_Y, test_size=0.1, random_state=5)
    # divide train set and valid set
    train_X, valid_x, train_y, valid_y = train_test_split(train_X, train_y, test_size=1 / 9, random_state=5)
    return train_X, train_y, valid_x, valid_y, test_X, test_y



def normalization(df_inf):
    df_Y = df_inf[[' Label']].astype("int64")
    df_Y = to_categorical(df_Y, num_classes=14)
    df_inf = df_inf.drop(labels=[' Label'], axis=1)
    df_inf = df_inf.drop(labels=['Unnamed: 0'], axis=1)
    df_inf = df_inf.drop(labels=['Unnamed: 0.1'], axis=1)
    ss = StandardScaler()
    df_std = ss.fit_transform(df_inf)
    return df_std, df_Y













