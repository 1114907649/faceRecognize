import pickle

import numpy as np


pids ,img_feats =[],[]
with open('feature/feature.pickle', 'rb') as f:
    pids ,img_feats = pickle.load(f)
pids=np.delete(pids,-1)
img_feats = np.delete(img_feats,-1, axis=0)
with open('feature/feature.pickle', 'wb') as f:
    pickle.dump([pids,img_feats],f)