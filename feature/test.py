import pickle

import numpy as np


pids ,img_feats =[],[]
with open('feature/feature.pickle', 'rb') as f:
    pids ,img_feats = pickle.load(f)

print(pids)