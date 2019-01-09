import os
import sys
import collections
import re
num_dic = {"1":0, "2":4, "3":12, "4":15, "5":18, "6":23, "7":27, "8":30, "9":34, "10":36, "11":39, "12":42, "13":45, "14":49, "15":51, "16":54}

def p2af(phonefile,affile,affileright,wf,num):
	af_dic = collections.OrderedDict()
	a = open(phonefile)
	astr = a.read()
	with open(affile, 'r') as f:
		i=0
		for line in f.readlines():
			line_list = line.split()
			af_dic[line_list[0]] = line_list[1]
	with open(affileright, 'r') as f:
		i=0
		for line in f.readlines():
			line_list = line.split()
			af_dic[line_list[0]] = line_list[1]
	list=[]
	for i in af_dic:
		list.append(i)
	List_new = sorted(list,key = lambda i:len(i),reverse=True)
	new_dic = collections.OrderedDict()
	for i in range(len(List_new)):
		new_dic[List_new[i]] = af_dic[List_new[i]]
	strat=num_dic[num]
	end=num_dic[str(int(num)+1)]
	if int(num)<8:
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+" ", astr)
	else:
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+af_dic[key][15:18]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+af_dic[key][15:18]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+af_dic[key][15:18]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(" "+key), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+af_dic[key][15:18]+" ", astr)
		for key in af_dic:
                        reg = re.compile(re.escape(key+" "), re.IGNORECASE)
                        astr=reg.sub(" "+af_dic[key][strat:end]+af_dic[key][15:18]+" ", astr)
	astr=astr.replace("  "," ")
	B  = open(wf,'w')
	B .write(astr)
	B .close()

def adddict(num):
    fwrite = open("/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/dict/lexicon.txt", "w")
    fwrite.write("<UNK> SPN\n")
    len=num_dic[str(int(num)+1)]-num_dic[num]
    if int(num)<8:
        for i in range(len):
            for j in range(len):
                if i+j==len-1:
                    fwrite.write("1")
                else:
                    fwrite.write("0")
            fwrite.write(" ")
            for j in range(len):
                if i+j==len-1:
                    fwrite.write("1")
                else:
                    fwrite.write("0")
            fwrite.write("\n")
    else:
        for i in range(len):
            for k in range(3):
                for j in range(len):
                    if i+j==len-1:
                        fwrite.write("1")
                    else:
                        fwrite.write("0")
                if k==0:
                    fwrite.write("001 ")
                if k==1:
                    fwrite.write("010 ")
                if k==2:  
                    fwrite.write("100 ")

                for j in range(len):
                    if i+j==len-1:
                        fwrite.write("1")
                    else:
                        fwrite.write("0")
                if k==0:
                    fwrite.write("001\n")
                if k==1:
                    fwrite.write("010\n")
                if k==2:    
                    fwrite.write("100\n")
       
if __name__ == "__main__":
    #starttime = datetime.datetime.now()
    print("the af you want:")
    print("eg:1")
    if len(sys.argv) == 2:
        adddict(sys.argv[1])
        p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/train/word.txt','AF_chn_all.txt','AF_eng_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/train/text',sys.argv[1])
        p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/dev/word.txt','AF_chn_all.txt','AF_eng_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/dev/text',sys.argv[1])
        p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/test_th/word.txt','AF_eng_all.txt','AF_chn_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/test_th/text',sys.argv[1])
        p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/test_lib/word.txt','AF_chn_all.txt','AF_eng_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/lib100/data/test_lib/text',sys.argv[1])
    else:
        print("please check the input parameters")
	
    #endtime = datetime.datetime.now()
    #T = endtime - starttime
    #print ('This process takes %s(time'%(T))
