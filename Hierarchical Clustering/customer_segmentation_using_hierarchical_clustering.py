# -*- coding: utf-8 -*-
"""Customer Segmentation using Hierarchical Clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MXH0GlOm_ziQHKH5czxJlnZ681Duk55X
"""

import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster

data = pd.read_excel('hierarchical_clustering_dataset.xlsx')
features = data[['Age', 'Annual Income', 'Spending Score ']]# Select features for clustering

linkage_matrix = linkage(features, method='ward')# 'ward' minimizes variance within clusters
#method='single', method='complete, method='average', method='centroid', method='median'''

# Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix)
plt.title("Dendrogram for Hierarchical Clustering")
plt.xlabel("Customer")
plt.ylabel("Euclidean distances")
plt.show()

clusters = fcluster(linkage_matrix, t=50, criterion='distance') # t means threshold and threshold means the distance in y axis
num_clusters = len(set(clusters))
print(num_clusters)

''' Ward’s Method: Merges clusters that minimize the increase in total within-cluster variance.
Best for: Creating compact, spherical clusters.

Single Linkage:Merges clusters based on the minimum distance between points in each cluster.
Best for: Finding elongated or irregularly shaped clusters.d.

Complete Linkage:Merges clusters based on the maximum distance between points in each cluster.
Best for: Forming compact clusters and avoiding chaining.

Average Linkage:Merges clusters based on the average distance between all points in the two clusters.
Best for: Moderately compact clusters, balances chaining and compactness.

Centroid Linkage:Merges clusters based on the distance between cluster centroids (the center points).
Best for: Data with normally distributed clusters.

Median Linkage:Similar to centroid linkage but uses a weighted average for merging clusters.
Best for: Balancing the impact of each point in cluster formation.
'''