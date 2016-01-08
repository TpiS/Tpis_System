# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import datasets
from sklearn import mixture
import general_model
import pymongo
#import api_server as api
import classifier_csv as cc

#subject = api.saveWav(filename)
##   ファイルの読み込み   ###
con = pymongo.MongoClient()
coll = con.user_db.feature_result
col = coll.find({u'subject-id': 'P1'})
doc = []
for c in col:
#    print "\n"
#    print c
    doc.append(c)
data = map(lambda x: [x['result']['grade']] + x['feature_list'], doc)
#data_grade =   map(lambda x: x['result']['grade'], doc)
print "\n\n ==> data"
print data

grade1 = np.array(filter(lambda x: int(x[0]) == 0,data))
grade2 = np.array(filter(lambda x: int(x[0]) == 1,data))
grade3 = np.array(filter(lambda x: int(x[0]) == 2,data))
grade4 = np.array(filter(lambda x: int(x[0]) == 3,data))
grade5 = np.array(filter(lambda x: int(x[0]) == 4,data))

print ("grade1"+str(len(grade1)))
print ("grade2"+str(len(grade2)))
print ("grade3"+str(len(grade3)))
print ("grade4"+str(len(grade4)))
print ("grade5"+str(len(grade5)))

###   活性度1モデル   ###
grade1_model = mixture.GMM(n_components=2, covariance_type='full')
if len(grade1) < 2:
    pass
else:
    grade1_model.fit(grade1[:,1:])
###   活性度2モデル   ###
grade2_model = mixture.GMM(n_components=2, covariance_type='full')
if len(grade2) < 2:
    pass
else:
    grade2_model.fit(grade2[:,1:])
###   活性度3モデル   ###                                                                              
grade3_model = mixture.GMM(n_components=2, covariance_type='full')
if len(grade3) < 2:
    pass
else:
    grade3_model.fit(grade3[:,1:])
###   活性度4モデル   ###                                                                              
grade4_model = mixture.GMM(n_components=2, covariance_type='full')
if len(grade4) < 2:
    pass
else:
    grade4_model.fit(grade4[:,1:])
###   活性度5モデル   ###                                                                              
grade5_model = mixture.GMM(n_components=2, covariance_type='full')
if len(grade5) < 2:
    pass
else:
    grade5_model.fit(grade5[:,1:])


def classify_by_file(filename):
    features = general_model.print_features(filename)
    #print features
    return cc.classify(features)

def post_features(filename):
    features = general_model.get_features(filename)
    return features

def sample_classify():
    return classify([1,2,3,4,5,6])

def sample_classify_by_file():
    return classify_by_file("/home/sugaya/public_html/wav/20151013223903.wav")

