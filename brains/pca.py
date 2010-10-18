import numpy as np

def pca(data):
    """Finds principal components of data and generates
    transformed dataset."""
    s = np.cov(data, rowvar = 0)
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
    return z.T

