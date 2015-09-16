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

"""
print["label","max","min","range","average","var","size"]
"""


def print_features(file,label):
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
        print ",".join([str(label),str(max(output)),str(min(output)),str(e),str(b),str(c),str(d)])



high_files = [
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_high_20150128162519_b6c77913-cd59-43cc-bbec-6d3610c959c1",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_high_20150128162531_387a4e2f-c006-4efa-8d19-b90f7c1cef42",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_high_20150128162541_f459a283-8dd3-450b-8ce4-272d83dd7b89",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_high_20150128162549_218f626f-b618-453c-b1ac-0bccd6d219b3",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_high_20150128162556_c5d8dc87-00ed-4f20-b251-9d71f89a7f06"]
              

law_files = [
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_low_20150128164521_d80b8c55-545d-4b1a-84f3-5973491f5595",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_low_20150128164533_047ab794-b100-4a23-8423-b231ca12c117",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_low_20150128164540_c334bfef-6fc0-4e1b-98b8-37dd3e711358",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_low_20150128164550_8407aa0c-f750-4c11-a4de-e27867e31083",
"/home/sw/public_html/wave_receiver/wave/panda/sugaya_low_20150128164555_64c2f132-7b0f-4040-9dbf-2bf23f95c492"]


 
feature_table = []




for file in high_files:
    print_features(file,0)
    
for file in law_files:
    print_features(file,1)


FILE ='sugaya_tadaima.csv'

f = open(FILE,'wb')

writecsv = csv.writer(f,lineterminator='\n')
writecsv.writerow(["label","max","min","range","average","var","size"])

for file in high_files:
    writecsv.writerow(print_features(file,0))


for file in law_files:
    writecsv.writerow(print_feature(file,1))


f.close()

