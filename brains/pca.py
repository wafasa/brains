#!/usr/bin/env python
# performs principal component analysis
# on file given in argv

import numpy as np
import sys

# load data and compute means and covariance matrix
data = np.loadtxt(sys.argv[1], delimiter = ",")
s = np.cov(data, rowvar = 0)

# find eigenvalues and eigenvectors of covariance matrix
evals, evecs = np.linalg.eig(s)

# find leading eigenvectors of s
energy = evals.sum()
idx = range(0, len(evals))
idx.sort(lambda a, b: cmp(evals[b], evals[a]))
e = 0
bestevals = []
while e / energy < 0.9:
    e += evals[idx[0]]
    bestevals.append(idx[0])
    idx = idx[1:]
weights = evecs[bestevals]

# find new array with principal components
datam = data - data.mean(axis = 0)
z = np.dot(weights, datam.T) # transpose datam because samples are rows
print(z)
