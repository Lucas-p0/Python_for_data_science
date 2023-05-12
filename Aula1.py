import numpy as np


km = np.loadtxt('data/carros-km.txt')
anos = np.loadtxt('data/carros-anos.txt', dtype=int)

km_media = km / (2019 - anos)
km_media_nan = km_media[np.isfinite(km_media)]
print(km_media_nan)
