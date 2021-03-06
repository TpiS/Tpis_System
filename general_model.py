#!/usr/bin/env python
# -*- coding: utf-8 -*-

##インポート##                                                                                                                
import subprocess
import numpy
import struct
import sys
import codecs
import pickle
from sklearn import datasets
import csv
import os
import math

def print_features(file):
    ##f０抽出##
    output = subprocess.check_output(['get_f0s',file])
    ##改行区切り##
    output = output.splitlines()
    ##float変換##
    output = map(float,output)
    ##無音区間削除##
    ##空要素削除##
    output = filter(lambda x:x!='',output)
    output = filter(lambda x:x != 0,output)
    if(output != []):
        ##各指標計算##
        a = numpy.array(output)
        b = numpy.average(a)
        c = numpy.var(a)
        d = a.size
        e = max(output)-min(output)
        print ["max","min","range","average","var","size"]
        print ",".join([str(max(output)),str(min(output)),str(e),str(b),str(c),str(d)])
    return[max(output),min(output),e,b,c,d]


files = [
"/home/sugaya/public_html/wav/20151013223903.wav",
"/home/sugaya/public_html/wav/20151013223913.wav",
"/home/sugaya/public_html/wav/20151013223944.wav",
"/home/sugaya/public_html/wav/20151013223959.wav",
"/home/sugaya/public_html/wav/20151013224052.wav",
"/home/sugaya/public_html/wav/20151013224103.wav",
"/home/sugaya/public_html/wav/20151013224211.wav",
"/home/sugaya/public_html/wav/20151013224328.wav",
"/home/sugaya/public_html/wav/20151013224344.wav",
"/home/sugaya/public_html/wav/20151013224410.wav",
"/home/sugaya/public_html/wav/20151013224423.wav",
"/home/sugaya/public_html/wav/20151013224437.wav",
"/home/sugaya/public_html/wav/20151013224539.wav",
"/home/sugaya/public_html/wav/20151013224556.wav",
"/home/sugaya/public_html/wav/20151013224610.wav",
"/home/sugaya/public_html/wav/20151013224626.wav",
"/home/sugaya/public_html/wav/20151013224646.wav",
"/home/sugaya/public_html/wav/20151013224720.wav",
"/home/sugaya/public_html/wav/20151013224811.wav",
"/home/sugaya/public_html/wav/20151013224832.wav",
"/home/sugaya/public_html/wav/20151013224842.wav",
"/home/sugaya/public_html/wav/20151013224854.wav",
"/home/sugaya/public_html/wav/20151013224924.wav",
"/home/sugaya/public_html/wav/20151013224938.wav",
"/home/sugaya/public_html/wav/20151013224955.wav",
"/home/sugaya/public_html/wav/20151013225011.wav",
"/home/sugaya/public_html/wav/20151013225022.wav",
"/home/sugaya/public_html/wav/20151013225035.wav",
"/home/sugaya/public_html/wav/20151013225052.wav",
"/home/sugaya/public_html/wav/20151013225123.wav",
"/home/sugaya/public_html/wav/20151014115206.wav",
"/home/sugaya/public_html/wav/20151014115239.wav",
"/home/sugaya/public_html/wav/20151014115313.wav",
"/home/sugaya/public_html/wav/20151014115329.wav",
"/home/sugaya/public_html/wav/20151014115416.wav",
"/home/sugaya/public_html/wav/20151014115449.wav",
"/home/sugaya/public_html/wav/20151014115513.wav",
"/home/sugaya/public_html/wav/20151014115559.wav",
"/home/sugaya/public_html/wav/20151014115619.wav",
"/home/sugaya/public_html/wav/20151014115648.wav",
"/home/sugaya/public_html/wav/20151014115712.wav",
"/home/sugaya/public_html/wav/20151014115737.wav",
"/home/sugaya/public_html/wav/20151014115800.wav",
"/home/sugaya/public_html/wav/20151014115841.wav",
"/home/sugaya/public_html/wav/20151014115916.wav",
"/home/sugaya/public_html/wav/20151014115945.wav",
"/home/sugaya/public_html/wav/20151014120007.wav",
"/home/sugaya/public_html/wav/20151014120029.wav",
"/home/sugaya/public_html/wav/20151014120053.wav",
"/home/sugaya/public_html/wav/20151014120114.wav",
"/home/sugaya/public_html/wav/20151014120147.wav",
"/home/sugaya/public_html/wav/20151014120209.wav",
"/home/sugaya/public_html/wav/20151014120309.wav",
"/home/sugaya/public_html/wav/20151014120343.wav",
"/home/sugaya/public_html/wav/20151014120453.wav",
"/home/sugaya/public_html/wav/20151014120526.wav",
"/home/sugaya/public_html/wav/20151014120550.wav",
"/home/sugaya/public_html/wav/20151014120706.wav",
"/home/sugaya/public_html/wav/20151014120734.wav",
"/home/sugaya/public_html/wav/20151014120754.wav",
"/home/sugaya/public_html/wav/20151016005139.wav",
"/home/sugaya/public_html/wav/20151016005146.wav",
"/home/sugaya/public_html/wav/20151016005158.wav",
"/home/sugaya/public_html/wav/20151016005209.wav",
"/home/sugaya/public_html/wav/20151016005217.wav",
"/home/sugaya/public_html/wav/20151016005227.wav",
"/home/sugaya/public_html/wav/20151016005238.wav",
"/home/sugaya/public_html/wav/20151016005239.wav",
"/home/sugaya/public_html/wav/20151016005247.wav",
"/home/sugaya/public_html/wav/20151016005258.wav",
"/home/sugaya/public_html/wav/20151016005307.wav",
"/home/sugaya/public_html/wav/20151016005315.wav",
"/home/sugaya/public_html/wav/20151016005325.wav",
"/home/sugaya/public_html/wav/20151016005335.wav",
"/home/sugaya/public_html/wav/20151016005345.wav",
"/home/sugaya/public_html/wav/20151016005353.wav",
"/home/sugaya/public_html/wav/20151016005402.wav",
"/home/sugaya/public_html/wav/20151016005411.wav",
"/home/sugaya/public_html/wav/20151016005420.wav",
"/home/sugaya/public_html/wav/20151016005429.wav",
"/home/sugaya/public_html/wav/20151016005440.wav",
"/home/sugaya/public_html/wav/20151016005448.wav",
"/home/sugaya/public_html/wav/20151016005458.wav",
"/home/sugaya/public_html/wav/20151016005507.wav",
"/home/sugaya/public_html/wav/20151016005516.wav",
"/home/sugaya/public_html/wav/20151016005525.wav",
"/home/sugaya/public_html/wav/20151016005533.wav",
"/home/sugaya/public_html/wav/20151016005542.wav",
"/home/sugaya/public_html/wav/20151016005552.wav",
"/home/sugaya/public_html/wav/20151016005601.wav",
"/home/sugaya/public_html/wav/20151016173332.wav",
"/home/sugaya/public_html/wav/20151016173357.wav",
"/home/sugaya/public_html/wav/20151016173407.wav",
"/home/sugaya/public_html/wav/20151016174614.wav",
"/home/sugaya/public_html/wav/20151016174615.wav",
"/home/sugaya/public_html/wav/20151016181401.wav",
"/home/sugaya/public_html/wav/20151016181539.wav",
"/home/sugaya/public_html/wav/20151016181546.wav",
"/home/sugaya/public_html/wav/20151016181551.wav",
"/home/sugaya/public_html/wav/20151016181556.wav",
"/home/sugaya/public_html/wav/20151016181607.wav",
"/home/sugaya/public_html/wav/20151016181612.wav",
"/home/sugaya/public_html/wav/20151016181617.wav",
"/home/sugaya/public_html/wav/20151016181625.wav",
"/home/sugaya/public_html/wav/20151016181631.wav",
"/home/sugaya/public_html/wav/20151016181636.wav",
"/home/sugaya/public_html/wav/20151016181641.wav",
"/home/sugaya/public_html/wav/20151016181647.wav",
"/home/sugaya/public_html/wav/20151016181652.wav",
"/home/sugaya/public_html/wav/20151016181657.wav",
"/home/sugaya/public_html/wav/20151016181705.wav",
"/home/sugaya/public_html/wav/20151016181710.wav",
"/home/sugaya/public_html/wav/20151016181715.wav",
"/home/sugaya/public_html/wav/20151016181722.wav",
"/home/sugaya/public_html/wav/20151016181729.wav",
"/home/sugaya/public_html/wav/20151016181736.wav",
"/home/sugaya/public_html/wav/20151016181742.wav",
"/home/sugaya/public_html/wav/20151016181746.wav",
"/home/sugaya/public_html/wav/20151016181800.wav",
"/home/sugaya/public_html/wav/20151016181805.wav",
"/home/sugaya/public_html/wav/20151016195615.wav",
"/home/sugaya/public_html/wav/20151016195749.wav",
"/home/sugaya/public_html/wav/20151016195825.wav",
"/home/sugaya/public_html/wav/20151016195908.wav",
"/home/sugaya/public_html/wav/20151016195928.wav",
"/home/sugaya/public_html/wav/20151016200017.wav",
"/home/sugaya/public_html/wav/20151016200030.wav",
"/home/sugaya/public_html/wav/20151016200045.wav",
"/home/sugaya/public_html/wav/20151016200116.wav",
"/home/sugaya/public_html/wav/20151016200238.wav",
"/home/sugaya/public_html/wav/20151016200251.wav",
"/home/sugaya/public_html/wav/20151016200311.wav",
"/home/sugaya/public_html/wav/20151016200328.wav",
"/home/sugaya/public_html/wav/20151016200349.wav",
"/home/sugaya/public_html/wav/20151016200406.wav",
"/home/sugaya/public_html/wav/20151016200422.wav",
"/home/sugaya/public_html/wav/20151016200445.wav",
"/home/sugaya/public_html/wav/20151016200543.wav",
"/home/sugaya/public_html/wav/20151016200602.wav",
"/home/sugaya/public_html/wav/20151016200621.wav",
"/home/sugaya/public_html/wav/20151016200637.wav",
"/home/sugaya/public_html/wav/20151016200648.wav",
"/home/sugaya/public_html/wav/20151016200740.wav",
"/home/sugaya/public_html/wav/20151016200757.wav",
"/home/sugaya/public_html/wav/20151016200813.wav",
"/home/sugaya/public_html/wav/20151016200827.wav",
"/home/sugaya/public_html/wav/20151016200849.wav",
"/home/sugaya/public_html/wav/20151016200912.wav",
"/home/sugaya/public_html/wav/20151016200926.wav",
"/home/sugaya/public_html/wav/20151016200952.wav",
"/home/sugaya/public_html/wav/20151016212836.wav",
"/home/sugaya/public_html/wav/20151016212900.wav",
"/home/sugaya/public_html/wav/20151016212919.wav",
"/home/sugaya/public_html/wav/20151016212935.wav",
"/home/sugaya/public_html/wav/20151016212949.wav",
"/home/sugaya/public_html/wav/20151016213057.wav",
"/home/sugaya/public_html/wav/20151016213110.wav",
"/home/sugaya/public_html/wav/20151016213125.wav",
"/home/sugaya/public_html/wav/20151016213137.wav",
"/home/sugaya/public_html/wav/20151016213155.wav",
"/home/sugaya/public_html/wav/20151016213209.wav",
"/home/sugaya/public_html/wav/20151016213223.wav",
"/home/sugaya/public_html/wav/20151016213237.wav",
"/home/sugaya/public_html/wav/20151016213256.wav",
"/home/sugaya/public_html/wav/20151016213320.wav",
"/home/sugaya/public_html/wav/20151016213341.wav",
"/home/sugaya/public_html/wav/20151016213357.wav",
"/home/sugaya/public_html/wav/20151016213413.wav",
"/home/sugaya/public_html/wav/20151016213430.wav",
"/home/sugaya/public_html/wav/20151016213447.wav",
"/home/sugaya/public_html/wav/20151016213501.wav",
"/home/sugaya/public_html/wav/20151016213514.wav",
"/home/sugaya/public_html/wav/20151016213529.wav",
"/home/sugaya/public_html/wav/20151016213543.wav",
"/home/sugaya/public_html/wav/20151016213600.wav",
"/home/sugaya/public_html/wav/20151016213615.wav",
"/home/sugaya/public_html/wav/20151016213628.wav",
"/home/sugaya/public_html/wav/20151016213642.wav",
"/home/sugaya/public_html/wav/20151016213658.wav",
"/home/sugaya/public_html/wav/20151016213712.wav",
"/home/sugaya/public_html/wav/20151020171002.wav",
"/home/sugaya/public_html/wav/20151020171156.wav",
"/home/sugaya/public_html/wav/20151020171207.wav",
"/home/sugaya/public_html/wav/20151020171216.wav",
"/home/sugaya/public_html/wav/20151020171225.wav",
"/home/sugaya/public_html/wav/20151020171232.wav",
"/home/sugaya/public_html/wav/20151020171240.wav",
"/home/sugaya/public_html/wav/20151020171259.wav",
"/home/sugaya/public_html/wav/20151020171307.wav",
"/home/sugaya/public_html/wav/20151020171313.wav",
"/home/sugaya/public_html/wav/20151020171321.wav",
"/home/sugaya/public_html/wav/20151020171328.wav",
"/home/sugaya/public_html/wav/20151020171335.wav",
"/home/sugaya/public_html/wav/20151020171344.wav",
"/home/sugaya/public_html/wav/20151020171351.wav",
"/home/sugaya/public_html/wav/20151020171404.wav",
"/home/sugaya/public_html/wav/20151020171405.wav",
"/home/sugaya/public_html/wav/20151020171413.wav",
"/home/sugaya/public_html/wav/20151020171420.wav",
"/home/sugaya/public_html/wav/20151020171427.wav",
"/home/sugaya/public_html/wav/20151020171446.wav",
"/home/sugaya/public_html/wav/20151020171451.wav",
"/home/sugaya/public_html/wav/20151020171457.wav",
"/home/sugaya/public_html/wav/20151020171503.wav",
"/home/sugaya/public_html/wav/20151020171509.wav",
"/home/sugaya/public_html/wav/20151020171516.wav",
"/home/sugaya/public_html/wav/20151020171526.wav",
"/home/sugaya/public_html/wav/20151020171528.wav",
"/home/sugaya/public_html/wav/20151020171535.wav",
"/home/sugaya/public_html/wav/20151020171543.wav",
"/home/sugaya/public_html/wav/20151020233513.wav",
"/home/sugaya/public_html/wav/20151020233517.wav",
"/home/sugaya/public_html/wav/20151020233617.wav",
"/home/sugaya/public_html/wav/20151020233627.wav",
"/home/sugaya/public_html/wav/20151020233640.wav",
"/home/sugaya/public_html/wav/20151020233700.wav",
"/home/sugaya/public_html/wav/20151020233708.wav",
"/home/sugaya/public_html/wav/20151020233717.wav",
"/home/sugaya/public_html/wav/20151020233725.wav",
"/home/sugaya/public_html/wav/20151020233733.wav",
"/home/sugaya/public_html/wav/20151020233743.wav",
"/home/sugaya/public_html/wav/20151020233752.wav",
"/home/sugaya/public_html/wav/20151020233758.wav",
"/home/sugaya/public_html/wav/20151020233808.wav",
"/home/sugaya/public_html/wav/20151020233815.wav",
"/home/sugaya/public_html/wav/20151020233836.wav",
"/home/sugaya/public_html/wav/20151020233842.wav",
"/home/sugaya/public_html/wav/20151020233855.wav",
"/home/sugaya/public_html/wav/20151020233901.wav",
"/home/sugaya/public_html/wav/20151020233908.wav",
"/home/sugaya/public_html/wav/20151020233915.wav",
"/home/sugaya/public_html/wav/20151020233940.wav",
"/home/sugaya/public_html/wav/20151020233947.wav",
"/home/sugaya/public_html/wav/20151020233953.wav",
"/home/sugaya/public_html/wav/20151020234021.wav",
"/home/sugaya/public_html/wav/20151020234029.wav",
"/home/sugaya/public_html/wav/20151020234035.wav",
"/home/sugaya/public_html/wav/20151020234044.wav",
"/home/sugaya/public_html/wav/20151020234058.wav",
"/home/sugaya/public_html/wav/20151020234132.wav"]
 
feature_table = []

"""
for file in files:
    print_features(file,"general")

FILE ='general_model.csv'
f = open(FILE,'wb')
writecsv = csv.writer(f,lineterminator='\n')
writecsv.writerow(["label","max","min","range","average","var","size"])

for file in files:
    writecsv.writerow(print_features(file,'general'))

f.close()
"""
