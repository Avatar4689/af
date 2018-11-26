#!/bin/bash

# Copyright 2015  Yajie Miao    (Carnegie Mellon University)
# Apache 2.0

[ -f path.sh ] && . ./path.sh; 

. utils/parse_options.sh || exit 1;
dir=exp/model_l4_c120


# Convert the model marker from "<BiLstmParallel>" to "<BiLstm>" (no longer needed)
format-to-nonparallel $dir/nnet/nnet.iter2 $dir/final.nnet >& $dir/log/model_to_nonparal.log || exit 1;

echo "Training succeeded. The final model $dir/final.nnet"
