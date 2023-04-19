import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from  matplotlib import cm


def plot_distribution_label(df):
    labels = 'BENIGN', 'TFTP', 'MSSQL', 'NetBIOS', 'UDP', 'Syn', 'DrDoS_SNMP', 'DrDoS_DNS', 'LDAP', 'DrDoS_SSDP', 'DrDoS_NTP', 'UDPLag', 'Portmap', 'WebDDoS'
    sizes = [len(df[df[' Label'] == 0]),
             len(df[df[' Label'] == 1]),
             len(df[df[' Label'] == 2]),
             len(df[df[' Label'] == 3]),
             len(df[df[' Label'] == 4]),
             len(df[df[' Label'] == 5]),
             len(df[df[' Label'] == 6]),
             len(df[df[' Label'] == 7]),
             len(df[df[' Label'] == 8]),
             len(df[df[' Label'] == 9]),
             len(df[df[' Label'] == 10]),
             len(df[df[' Label'] == 11]),
             len(df[df[' Label'] == 12]),
             len(df[df[' Label'] == 13])]

    colors = cm.rainbow(np.arange(len(sizes)) / len(sizes))  # colormaps: Paired, autumn, rainbow, gray,spring,Darks
    explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

    fig, axes = plt.subplots(figsize=(10, 5), ncols=2)  # 设置绘图区域大小
    ax1, ax2 = axes.ravel()

    # Plot
    plt.rcParams.update({'font.size': 12})
    patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                        shadow=True, startangle=140)
    ax2.axis('off')
    ax2.legend(patches, labels, loc='center left')
    plt.tight_layout()
    plt.axis('equal')
    plt.savefig('./Results_img/pie_gragh_label.png')

def plot_histogram_label(df):
    df[' Label'].loc[df[' Label'] == 0] = 'BENIGN'
    df[' Label'].loc[df[' Label'] == 1] = 'TFTP'
    df[' Label'].loc[df[' Label'] == 2] = 'MSSQL'
    df[' Label'].loc[df[' Label'] == 3] = 'NetBIOS'
    df[' Label'].loc[df[' Label'] == 4] = 'UDP'
    df[' Label'].loc[df[' Label'] == 5] = 'Syn'
    df[' Label'].loc[df[' Label'] == 6] = 'DrDoS_SNMP'
    df[' Label'].loc[df[' Label'] == 7] = 'DrDoS_DNS'
    df[' Label'].loc[df[' Label'] == 8] = 'LDAP'
    df[' Label'].loc[df[' Label'] == 9] = 'DrDoS_SSDP'
    df[' Label'].loc[df[' Label'] == 10] = 'DrDoS_NTP'
    df[' Label'].loc[df[' Label'] == 11] = 'UDPLag'
    df[' Label'].loc[df[' Label'] == 12] = 'Portmap'
    df[' Label'].loc[df[' Label'] == 13] = 'WebDDoS'

    plt.figure(figsize=(20, 16))
    sns.set(style="darkgrid")
    g1 = sns.countplot(x=' Label', hue=' Label', data=df[[' Label']], dodge=False)
    plt.savefig('./Results_img/histogram_label.png')


def plot_stem_Fwd(df):
    plt.figure(figsize=(15, 7))
    sns.set(style="whitegrid")
    result = df.groupby([" Label"])[' Total Fwd Packets'].sum().reset_index().sort_values(' Total Fwd Packets')
    plt.stem(result[' Label'], result[' Total Fwd Packets'], use_line_collection=True)
    plt.title('Total Fwd packets Visualization', fontsize=24)
    plt.savefig('./Results_img/stem_fwd_packets.png')

def plot_bar_Backward(df):
    sns.set(style="whitegrid")
    # Set the figure size
    plt.figure(figsize=(17, 7))
    result1 = df.groupby([" Label"])[' Total Backward Packets'].sum().reset_index().sort_values(
        ' Total Backward Packets')
    plt.title('Total Backward Packets Visualization', fontsize=24);
    sns.barplot(
        x=" Total Backward Packets",
        y=" Label",
        data=result1,
        estimator=sum,
        ci=None)
    plt.savefig('./Results_img/bar_backward_packets.png')

def plot_heatmap_features(df):
    df_feature = df[[' Bwd Packets/s', ' Total Fwd Packets', 'Total Length of Fwd Packets', ' Flow Duration',
                     ' Total Length of Bwd Packets', ' Total Backward Packets', ' Protocol', ' Inbound',
                     ' Min Packet Length', ' Fwd Packet Length Min', ' Packet Length Mean', ' Fwd Packet Length Max',
                     ' Average Packet Size', ' ACK Flag Count', ' Avg Fwd Segment Size', ' Fwd Packet Length Mean',
                     ' Max Packet Length', ' Protocol', 'Fwd Packets/s', 'Total Length of Fwd Packets',
                     ' Subflow Fwd Bytes', ' act_data_pkt_fwd']]
    corrMatrix = df_feature.corr()
    plt.figure(figsize=(25, 11))
    plt.title('Heatmap Between Selected Features ', fontsize=24);
    sns.heatmap(corrMatrix, annot=True)
    plt.savefig('./Results_img/heatmap_features.png')





