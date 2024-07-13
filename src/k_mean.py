import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

def load_data(data_dir):
    data = load_files(data_dir, encoding='latin1')
    return data

def preprocess_data(data, method='tfidf'):
    if method == 'tfidf':
        vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    else:
        vectorizer = CountVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(data.data)
    return vectorizer, X

def apply_kmeans(X):
    kmeans = KMeans(n_clusters=20, random_state=42)
    kmeans.fit(X)
    return kmeans

def visualize_kmeans(kmeans, vectorizer, X, output_path, prefix):
    feature_names = vectorizer.get_feature_names_out()
    clusters = kmeans.labels_

    for cluster_id in range(kmeans.n_clusters):
        cluster_indices = (clusters == cluster_id)
        cluster_X = X[cluster_indices].toarray()
        centroid = cluster_X.mean(axis=0)
        top_features_indices = centroid.argsort()[::-1][:10]
        top_features = [feature_names[i] for i in top_features_indices]
        
        plt.figure(figsize=(5, 3))
        plt.barh(top_features, centroid[top_features_indices])
        plt.xlabel('Feature Value')
        plt.title(f'Cluster {cluster_id}')
        plt.gca().invert_yaxis()
        plt.savefig(f"{output_path}/{prefix}_cluster_{cluster_id}.png")
        plt.close()

def main():
    script_dir = os.path.dirname(__file__)
    mini_newsgroups_dir = os.path.join(script_dir, '..', 'mini_newsgroups')
    newsgroups20_dir = os.path.join(script_dir, '..', '20_newsgroups')
    
    output_path = os.path.join(script_dir, 'static', 'images')
    os.makedirs(output_path, exist_ok=True)
    
    # Process mini_newsgroups
    data = load_data(mini_newsgroups_dir)
    vectorizer, X = preprocess_data(data)
    kmeans = apply_kmeans(X)
    visualize_kmeans(kmeans, vectorizer, X, output_path, 'mini')

    # Process 20_newsgroups
    data = load_data(newsgroups20_dir)
    vectorizer, X = preprocess_data(data)
    kmeans = apply_kmeans(X)
    visualize_kmeans(kmeans, vectorizer, X, output_path, '20newsgroups')

if __name__ == "__main__":
    main()
