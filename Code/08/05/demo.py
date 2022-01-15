from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
data, target = make_blobs(n_samples=500, n_features=2, centers=3)


from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(data)
plt.scatter(data[:, 0], data[:, 1], c=y_pred)
plt.show()
