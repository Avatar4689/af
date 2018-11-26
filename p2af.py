import collections
def p2af(phonefile,affile,affileright,wf):
    af_dic = collections.OrderedDict()
    a = open(phonefile)
    str = a.read()
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
    for key in af_dic:
        str=str.replace(" "+key+" "," "+af_dic[key][15:18]+" ")
    for key in af_dic:
        str=str.replace(" "+key," "+af_dic[key][15:18]+" ")
    for key in af_dic:
        str=str.replace(key+" "," "+af_dic[key][15:18]+" ")
    for key in af_dic:
        str=str.replace(" "+key," "+af_dic[key][15:18]+" ")
    for key in af_dic:
        str=str.replace(key+" "," "+af_dic[key][15:18]+" ")
    str=str.replace("  "," ")
    B  = open(wf,'w')
    B .write(str)
    B .close()
p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/train/word.txt','AF_eng_all.txt','AF_chn_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/train/text')
p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/dev/word.txt','AF_eng_all.txt','AF_chn_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/dev/text')
p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/test_th/word.txt','AF_eng_all.txt','AF_chn_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/test_th/text')
p2af('/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/test_ti/word.txt','AF_chn_all.txt','AF_eng_all.txt','/home/asr2/Kaldi/kaldi-master/eesen-master/asr_egs/eesen-for-thchs30-master/data/test_ti/text')
