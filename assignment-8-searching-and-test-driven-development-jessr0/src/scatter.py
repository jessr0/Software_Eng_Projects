import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.use('Agg')

data_file = sys.argv[1]
out_file = sys.argv[2]
title = sys.argv[3]
x = sys.argv[4]
y = sys.argv[5]

X = []
Y = []
for line in open(data_file):
    A = line.rstrip().split()
    X.append(float(A[0]))
    Y.append(float(A[1]))

fig, ax = plt.subplots()
ax.scatter(X, Y)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file, bbox_inches='tight')
