#!/usr/bin/env python
# -*- coding: utf-8 -*-


##インポート##
import subprocess
import numpy 
import numpy as np
import struct
import sys
from pylab import *
import matplotlib.pyplot as plt
import random
import codecs
import pickle
from sklearn import datasets
import csv
import os
import math

def feature(file):
    
    ##f０抽出##    
    output = subprocess.check_output(['get_f0s',file])

    ##改行区切り##
    output = output.splitlines()

    ##無音区間削除##
    while '0.000000' in output: output.remove('0.000000')

    ##空要素削除##
    output = filter(lambda x:x!='',output)

    ##float変換##
    output = map(float,output)

    ##各指標計算##
    a = numpy.array(output)
    b = numpy.average(a)
    c = numpy.var(a)
    d = a.size
    e = max(output)-min(output)    

    return [max(output),min(output),e,b,c,d]

"""
if __name__ == '__main__':

    ##print feature('/home/sugaya/Tpis_System/high_activation_level/20141212163944','high')
    
    
    high_files = [
        "/home/sugaya/Tpis_System/high_activation_level/20141212163944",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163930",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163847",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163840",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163831",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163816",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163752",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163740",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163730",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163703",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163655",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163646",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163633",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163621",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163615",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163609",
        "/home/sugaya/Tpis_System/high_activation_level/20141212163533"]
    
    law_files = ["/home/sugaya/Tpis_System/law_activation_level/20141212164350",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164343",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164333",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164304",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164301",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164257",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164249",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164242",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164234",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164216",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164209",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164201",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164153",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164145",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164137",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164127",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164119",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164110",
                 "/home/sugaya/Tpis_System/law_activation_level/20141212164100"] 

    ## print ##
    print["label","max","min","range","average","var","size"]    
    for file in high_files:
        print ["1"]+feature(file)
        
    for file in law_files:
        print ["0"]+feature(file)
"""
