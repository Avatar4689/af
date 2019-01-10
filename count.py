# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:27:24 2019

@author: jfhz4
"""
import os
import sys
import datetime


def addto(file, num):
    fwrite = open(file, "r")
    line = fwrite.readline().strip('[').strip('\n').strip(']').strip(' ').split(' ')
    print(line)
    while len(line)<int(num):
        line.append("1")
    fwrite.close()
    print(line)
    fwrite = open(file, "w")
    fwrite.write("[ ")
    for i in range(len(line)):
        fwrite.write(line[i]+" ")
    fwrite.write("]")

if __name__ == "__main__":
    starttime = datetime.datetime.now()
    if len(sys.argv) == 3:
        addto(sys.argv[1], sys.argv[2])
    else:
        print("please check the input parameters")
    endtime = datetime.datetime.now()
    T = endtime - starttime
    print ('This process takes %s(time)'%(T))
