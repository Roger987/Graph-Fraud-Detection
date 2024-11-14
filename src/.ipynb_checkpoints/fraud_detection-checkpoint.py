import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import igraph as ig


plot_settings = {'ytick.labelsize': 16,
                        'xtick.labelsize': 16,
                        'font.size': 22,
                        'figure.figsize': (10, 5),
                        'axes.titlesize': 22,
                        'axes.labelsize': 18,
                        'lines.linewidth': 2,
                        'lines.markersize': 3,
                        'legend.fontsize': 11
                }
plt.style.use(plot_settings)

classes_path = "../elliptic_bitcoin_dataset/elliptic_txs_classes.csv"
edges_path = "../elliptic_bitcoin_dataset/elliptic_txs_edgelist.csv"
features_path = "../elliptic_bitcoin_dataset/elliptic_txs_features.csv"

classes = pd.read_csv(classes_path)
edges = pd.read_csv(edges_path)
feat_cols = ['txId', 'time_step'] + [f'trans_feat_{i}' for i in range(93)] + [f'agg_feat_{i}' for i in range(72)]
feats = pd.read_csv(features_path, header=None, names=feat_cols)

classes.columns = ['txId', 'label']
df = classes.set_index('txId').join(feats.set_index('txId'))
total = df['time_step'].value_counts().sort_index()
illicit = df['time_step'][df['label']=='1'].value_counts().sort_index()
licit = df['time_step'][df['label']=='2'].value_counts().sort_index()
unknown = df['time_step'][df['label']=='unknown'].value_counts().sort_index()