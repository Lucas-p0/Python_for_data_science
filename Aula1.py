import numpy as np


km = np.loadtxt('data/carros-km.txt')
anos = np.loadtxt('data/carros-anos.txt', dtype=int)
km_media_nan = km / (2019 - anos)

km_media = km_media_nan[np.isfinite(km_media_nan)]
print(km_media)
