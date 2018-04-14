#%%
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use("ggplot")
%matplotlib inline
from numpy.random import randn
from sklearn.cluster import KMeans
%config InlineBackend.figure_format = 'retina'
#%%
x = randn(100)
y = randn(100)
X = np.array([[x[i], y[i]] for i in range(0,len(x))])
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","b.","c.","y."]
for i in range(len(X)):
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
plt.scatter(centroids[:,0],centroids[:,1],marker="x",s=150,linewidths=5,zorder=10)