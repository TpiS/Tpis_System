#!/usr/bin/env python                                                                                  
# -*- coding: utf-8 -*- 

#インポート
import numpy as np
from scipy import loadtxt
import codecs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import datasets
from sklearn import mixture
import csv
import urllib



"""
data = np.genfromtxt( "f0_data.csv", delimiter=",", filling_values=(1, 2, 3, 4, 5, 6, 7) )
#f0 = datasets.load_f0_data.csv()
print(data)
"""



"""
f = open('f0_tadaima.csv', 'rb')
dataReader = csv.reader(f)

##改行区切り##                                                                                                                                             
output = f.splitlines()
##float変換##                                                                                                                                             
output = map(float,output)

f.readline()  # skip the header
data = np.loadtxt(f)

for row in dataReader:
    print ','.join(row)
"""




url = "/home/sugaya/Tpis_System/f0_tadaima.csv"

# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset)


