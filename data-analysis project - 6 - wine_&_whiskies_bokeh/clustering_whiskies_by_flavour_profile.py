from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
model.rows_
# >>>np.sum(model.rows_, axis=1)
# >>>np.sum(model.rows_, axis=0)
model.row_labels_
