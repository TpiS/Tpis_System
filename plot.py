#coding:utf-8
import struct
import sys
from pylab import *

if len(sys.argv) != 2:
    print "usage: python plot.py [raw file]"
    sys.exit()
rawfile = sys.argv[1]

# 音声波形をロード
wave = []
f = open(rawfile, "rb")
while True:
    # 2バイト（SHORT）ずつ読み込む
    b = f.read(2)
    if b == "": break;
    # 読み込んだ2バイトをSHORT型（h）でアンパック
    val = struct.unpack("h", b)[0]
    wave.append(val)
f.close()

# プロット
plot(range(len(wave)), wave)
xlabel("sample")
ylabel("amplitude")
xlim([0, len(wave)])
ylim([-32768, 32767])
show()
