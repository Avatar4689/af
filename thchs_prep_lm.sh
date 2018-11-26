#!/bin/bash
export IRSTLM=/home/asr2/Kaldi/kaldi-trunk/tools/irstlm
#for file in /home/asr2/Kaldi/kaldi-trunk/egs/thchs30/s4/data_thchs30/data_thchs30/data/*.wav.trn
#do
#   sed -n 1p $file | sed -e 's:^:<s> :' -e 's:$: </s>:' >> lm_train.text
#done
# cut -d' ' -f2- train.text | sed -e 's:^:<s> :' -e 's:$: </s>:' \
#  > lm_train.text
#/home/asr2/Kaldi/kaldi-trunk/tools/bin/build-lm.sh -i lm_train.text -n 2 -o lm_phone_bg.ilm.gz
/home/asr2/Kaldi/kaldi-trunk/tools/bin/build-lm.sh -i text -n 3 -o lm_word_bg.ilm.gz
