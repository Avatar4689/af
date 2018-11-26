#!/bin/bash
. ./cmd.sh ## You'll want to change cmd.sh to something that will work on your system.
           ## This relates to the queue.
. path.sh

. parse_options.sh
H=`pwd`
corpus_dir=$H/corpus

echo =====================================================================
echo "                       TLG WFST Construction                       "
echo =====================================================================
#Data preparation
#local/thchs-30_data_prep.sh $H $corpus_dir

# Construct the phoneme-based dict.
# We get 216 tokens, representing phonemes with tonality.
local/thchs-30_prepare_phn_dict.sh || exit 1;

# Compile the lexicon and token FSTs
utils/ctc_compile_dict_token.sh --dict-type "phn" data/dict_phn data/lang_tmp data/lang || exit 1;
