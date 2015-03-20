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

"""
data = np.genfromtxt( "f0_data.csv", delimiter=",", filling_values=(1, 2, 3, 4, 5, 6, 7) )
#f0 = datasets.load_f0_data.csv()
print(data)
"""

D = np.genfromtxt("f0_data.csv", delimiter=",", skip_header=1)

