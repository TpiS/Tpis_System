#!/usr/bin/env python
# -*- encoding: utf-8 -*-


##インポート##
import subprocess
import numpy 
import struct
import sys
from pylab import *
import matplotlib.pyplot as plt

##f０抽出##
output = subprocess.check_output(['get_f0s','20141127105859'])


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


##プリント##
print("max: %s" % max(output))
print("min: %s" % min(output))
print("range: %s" % e)
print("average: %s" % b)
print("var: %s" % c)
print("size: %s" % d)


