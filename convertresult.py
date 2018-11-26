# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:41:34 2018

@author: jfhz4
"""
import re
import numpy as np
import scipy.io
from itertools import groupby
def find_lcseque(s1, s2): 
	 # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
	m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
	# d用来记录转移方向
	d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
 
	for p1 in range(len(s1)): 
		for p2 in range(len(s2)): 
			if s1[p1] == s2[p2]:            #字符匹配成功，则该位置的值为左上方的值加1
				m[p1+1][p2+1] = m[p1][p2]+1
				d[p1+1][p2+1] = 'ok'          
			elif m[p1+1][p2] > m[p1][p2+1]:  #左值大于上值，则该位置的值为左值，并标记回溯时的方向
				m[p1+1][p2+1] = m[p1+1][p2] 
				d[p1+1][p2+1] = 'left'          
			else:                           #上值大于左值，则该位置的值为上值，并标记方向up
				m[p1+1][p2+1] = m[p1][p2+1]   
				d[p1+1][p2+1] = 'up'         
	(p1, p2) = (len(s1), len(s2)) 
	s = [] 
	while m[p1][p2]:    #不为None时
		c = d[p1][p2]
		if c == 'ok':   #匹配成功，插入该字符，并向左上角找下一个
			s.append(s1[p1-1])
			p1-=1
			p2-=1 
		if c =='left':  #根据标记，向左找下一个
			p2 -= 1
		if c == 'up':   #根据标记，向上找下一个
			p1 -= 1
	s.reverse() 
	return ''.join(s) 
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
        elif re.search(r'\]',line):
            listline=line.strip().strip(']').strip().split(' ')
            newavlist.append(listline.index(max(listline)))
            qc=[]
            qc=[x[0] for x in groupby(newavlist)]
            while 0 in qc:
                qc.remove(0)
            total.append(qc)
        else:
            listline=line.strip().strip(' ').split(' ')
            newavlist.append(listline.index(max(listline)))
def getlabel(path):
    file = open(path)
    total=[]
    while 1:
        line = file.readline();
        if not line:
#       save=total[0:10001]
            return total
        listline=line.strip().split(' ')
        del listline[0]
        total.append(listline)
if __name__ == '__main__':
    a=0
    b=0
    predict=ctc("trans.1.log")+ctc("trans.2.log")+ctc("trans.3.log")+ctc("trans.4.log")+ctc("trans.5.log")+ctc("trans.6.log")+ctc("trans.7.log")+ctc("trans.8.log")
    label=getlabel("labels.test")
    predict_new=[]
    for i in range (len(predict)):
        new = [str(x) for x in predict[i]]
        predict_new.append(new)
    for i in range (len(predict_new)):
        p2s="".join(predict_new[i])
        l2s="".join(label[i])
        result=find_lcseque(l2s,p2s)
        a=a+len(l2s)
        b=b+len(result)
    print(b/a)                                                             
