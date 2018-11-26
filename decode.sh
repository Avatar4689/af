#!/bin/bash
. ./cmd.sh ## You'll want to change cmd.sh to something that will work on your system.
           ## This relates to the queue.
. path.sh

. parse_options.sh

#model_dir=exp/model_l4_c320
model_dir=exp/model_af02
echo =====================================================================
echo "                             Decoding                              "
echo =====================================================================
# decoding
steps/decode_no_lm.sh --cmd "$decode_cmd" --nj 8 --beam 17.0 --lattice_beam 8.0 --max-active 5000 --acwt 0.9 \
    data/search_Graph data/test_ti $model_dir $model_dir/decode_test_ti || exit 1;
steps/decode_no_lm.sh --cmd "$decode_cmd" --nj 8 --beam 17.0 --lattice_beam 8.0 --max-active 5000 --acwt 0.9 \
    data/search_Graph data/test_th $model_dir $model_dir/decode_test_th || exit 1;
