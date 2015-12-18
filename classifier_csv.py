# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import datasets
from sklearn import mixture
import general_model

##   ファイルの読み込み   ###
data = np.genfromtxt('general_model.csv', delimiter=',', skiprows=1)
np.random.seed(1)
grade1 = np.array(filter(lambda x: int(x[0]) == 1,data))
grade2 = np.array(filter(lambda x: int(x[0]) == 2,data))
grade3 = np.array(filter(lambda x: int(x[0]) == 3,data))
grade4 = np.array(filter(lambda x: int(x[0]) == 4,data))
grade5 = np.array(filter(lambda x: int(x[0]) == 5,data))

###   活性度1モデル   ###
grade1_model = mixture.GMM(n_components=5, covariance_type='full')
grade1_model.fit(grade1[:,1:])
###   活性度2モデル   ###
grade2_model = mixture.GMM(n_components=5, covariance_type='full')
grade2_model.fit(grade2[:,1:])
###   活性度3モデル   ###                                                                                                    
grade3_model = mixture.GMM(n_components=5, covariance_type='full')
grade3_model.fit(grade3[:,1:])
###   活性度4モデル   ###                                                                                                     
grade4_model = mixture.GMM(n_components=5, covariance_type='full')
grade4_model.fit(grade4[:,1:])
###   活性度5モデル   ###                                                                                                    
grade5_model = mixture.GMM(n_components=5, covariance_type='full')
grade5_model.fit(grade5[:,1:])

### 分類 ###
def classify(feature_list):    
    grade1_score = grade1_model.score([feature_list])[0]
    grade2_score = grade2_model.score([feature_list])[0]
    grade3_score = grade3_model.score([feature_list])[0]
    grade4_score = grade4_model.score([feature_list])[0]
    grade5_score = grade5_model.score([feature_list])[0]
    grade_score=[]
    grade_score=[grade1_score,grade2_score,grade3_score,grade4_score,grade5_score]
    max(grade_score)
    for i in range(len(grade_score)):
            if grade_score[i] == max(grade_score):
                print "grade_score: %s" % i    
    """
    if grade5_score >= grade4_score:
        return {"result" : "grade5",
                "score" : grade5_score}
    elif grade4_score >= grade3_score and grade4_score < grade5_score:
        return {"result" : "grade4",
                "score" : grade4_score}
    elif grade3_score >= grade2_score and grade3_score < grade4_score:
        return {"result" : "grade3",
                "score" : grade3_score}
    elif grade2_score >= grade1_score and grade2_score < grade3_score:
        return {"result" : "grade2",
                "score" : grade2_score}
    elif grade1_score < grade2_score:
        return {"result" : "grade1",
                "score" : grade1_score}
    """

def classify_by_file(filename):
    features = general_model.print_features(filename)
    #print features
    return classify(features)

def sample_classify():
    return classify([1,2,3,4,5,6])
def sample_classify_by_file():
    return classify_by_file("/home/sugaya/public_html/wav/20151013223903.wav")

