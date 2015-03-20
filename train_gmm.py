# -*- coding: utf-8 -*-
 
from sklearn.datasets import make_classification
import numpy as np
import matplotlib.pyplot as plt
import pystan
 
 
NUM_MIXTURE_COMPONENTS = 4
NUM_DIMENSIONS = 2
 
 
def create_data(num_samples):
    """
    Creates data to train model parameters
    """
    # 乱数で混合重みを生成
    weights = np.random.random(NUM_MIXTURE_COMPONENTS)
    weights = (weights / weights.sum()).tolist()
 
    feature_vectors, labels = make_classification(
        n_samples=num_samples, n_features=NUM_DIMENSIONS, n_informative=NUM_DIMENSIONS, n_redundant=0,
        n_classes=NUM_MIXTURE_COMPONENTS, n_clusters_per_class=1, weights=weights)
 
    # グラフ描画用
    plt.scatter(feature_vectors[:, 0], feature_vectors[:, 1], marker='o')
    plt.show()
 
    return feature_vectors
 
 
def main():
    feature_vectors = create_data(1000)
 
    # create stan model
    compiled_model = pystan.StanModel(file='multi_dimensional_gmm.stan')
 
    # training
    training_data = dict(N=len(feature_vectors), D=2, M=NUM_MIXTURE_COMPONENTS, X=feature_vectors)
    optimized = compiled_model.optimizing(training_data)
 
    print(optimized)
 
 
if __name__ == '__main__':
    main()
