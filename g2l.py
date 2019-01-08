# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:49:55 2018

@author: jfhz4
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:41:34 2018

@author: jfhz4
"""
import re
import numpy as np
import scipy.io
from itertools import groupby
def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+' ')
    file.write('\n')
    file.close()
def ctc(path):
    file = open(path)
    total=[]
    while 1:
        line = file.readline();
        if not line:
#       save=total[0:10001]
            return total
        if  re.search(r'\[',line):
            newavlist=[]
            newavlist.append(line.strip().strip('[').strip())
        elif re.search(r'\]',line):
            listline=line.strip().strip(']').strip().split(' ')
            listline.pop()
            newavlist.append(listline.index(max(listline)))
            qc=[]
            qc=[x[0] for x in groupby(newavlist)]
            while 0 in qc:
                qc.remove(0)
            total.append(qc)
        else:
            listline=line.strip().strip(' ').split(' ')
            listline.pop()
            newavlist.append(listline.index(max(listline)))
if __name__ == '__main__':
    predict=ctc("trans.1.log")+ctc("trans.2.log")+ctc("trans.3.log")+ctc("trans.4.log")+ctc("trans.5.log")+ctc("trans.6.log")+ctc("trans.7.log")+ctc("trans.8.log")
    for i in range (len(predict)):
        text_save(predict[i],"predict",mode='a')
