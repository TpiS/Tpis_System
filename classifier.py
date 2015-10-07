# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import datasets
from sklearn import mixture
import f0_tadaima
#import sugaya_tadaima

###   ファイルの読み込み   ###
data = np.genfromtxt('f0_tadaima.csv', delimiter=',')
np.random.seed(1)

high_data = np.array(filter(lambda x: int(x[0]) == 0,data))
low_data  = np.array(filter(lambda x: int(x[0]) == 1,data))


###   活性度が高いモデル   ###
high_model = mixture.GMM(n_components=2, covariance_type='full')
high_model.fit(high_data[:,1:])


###   活性度が低いモデル   ###
low_model = mixture.GMM(n_components=2, covariance_type='full')
low_model.fit(low_data[:,1:])





###　　ファイルの読み込み(個人)　###                                                                    

data2 = np.genfromtxt('sugaya_tadaima.csv', delimiter=',')
np.random.seed(1)

high_sugaya = np.array(filter(lambda x: int(x[0]) == 0,data2))
low_sugaya = np.array(filter(lambda x: int(x[0]) == 1,data2))


###　活性度が高いモデル(個人)　###                                                                       
high_model_sugaya = mixture.GMM(n_components=2, covariance_type='full')
high_model_sugaya.fit(high_sugaya[:,1:])


###   活性度が低いモデル(個人)   ### 
low_model_sugaya = mixture.GMM(n_components=2, covariance_type='full')
low_model_sugaya.fit(low_sugaya[:,1:])



### 分類 ###
def classify(feature_list):
    high_score = high_model.score([feature_list])[0]
    low_score  = low_model.score([feature_list])[0]
    if high_score > low_score:
        return {"result" : "high",
                "high-score" : high_score,
                "low_score"  : low_score}
    elif high_score < low_score:
        return {"result" : "low",
                "high-score" : high_score,
                "low_score"  : low_score}
    else:
        return {"result" : "same",
                "high-score" : high_score,
                "low_score"  : low_score}


def classify_by_file(filename):
    features = f0_tadaima.feature(filename)
#   print features
    return classify(features)

def sample_classify():
    return classify([1,2,3,4,5,6])

def sample_classify_by_file():
    return classify_by_file("/home/sugaya/Tpis_System/high_activation_level/20141212163944")



### 分類(個人) ###                                                                                                 
def classify_sugaya(feature_list):
    high_sugaya_score = high_model_sugaya.score([feature_list])[0]
    low_sugaya_score  = low_model_sugaya.score([feature_list])[0]

    if high_sugaya_score > low_sugaya_score:
        return {"result" : "high",
                "high-score" : high_sugaya_score,
                "low_score"  : low_sugaya_score}
    elif high_sugaya_score < low_sugaya_score:
        return {"result" : "low",
                "high-score" : high_sugaya_score,
                "low_score"  : low_sugaya_score}
    else:
        return {"result" : "same",
                "high-score" : high_sugaya_score,
                "low_score"  : low_sugaya_score}

def classify_by_file_sugaya(filename):
    features2 = sugaya_tadaima.feature(filename)
    return classify(features)

def sample_classify_sugaya():
    return classify_sugaya([1,2,3,4,5,6])

def sample_classify_by_file_sugaya():
    return classify_by_file_sugaya("/home/sugaya/Tpis_System/high_activation_level/20141212163944")


