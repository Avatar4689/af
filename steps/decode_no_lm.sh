#!/bin/bash

# Apache 2.0
 
## Begin configuration section
stage=0
nj=16
cmd=run.pl
num_threads=1

acwt=0.9
min_active=200
max_active=7000 # max-active
beam=15.0       # beam used
lattice_beam=8.0
max_mem=50000000 # approx. limit to memory consumption during minimization in bytes
mdl=final.nnet

skip_scoring=false # whether to skip WER scoring
scoring_opts="--min-acwt 5 --max-acwt 10 --acwt-factor 0.1"
score_with_conf=false

# feature configurations; will be read from the training dir if not provided
norm_vars=
add_deltas=
subsample_feats=
splice_feats=
## End configuration section

echo "$0 $@"  # Print the command line for logging

[ -f ./path.sh ] && . ./path.sh;
. parse_options.sh || exit 1;

if [ $# != 4 ]; then
   echo "Wrong #arguments ($#, expected 3)"
   echo "Usage: steps/decode_ctc.sh [options] <graph-dir> <data-dir> <decode-dir>"
   echo " e.g.: steps/decode_ctc.sh data/lang data/test exp/train_l4_c320/decode"
   echo "main options (for others, see top of script file)"
   echo "  --stage                                  # starts from which stage"
   echo "  --nj <nj>                                # number of parallel jobs"
   echo "  --cmd <cmd>                              # command to run in parallel with"
   echo "  --acwt                                   # default 0.9, the acoustic scale to be used"
   exit 1;
fi

graphdir=$1
data=$2
srcdir=$3
dir=`echo $4 | sed 's:/$::g'` # remove any trailing slash.

#srcdir=`dirname $dir`; # assume model directory one level up from decoding directory.
#srcdir=/home/sundy/work/egs/hkust/exp/train_phn_l3_c320

sdata=$data/split$nj;

thread_string=
[ $num_threads -gt 1 ] && thread_string="-parallel --num-threads=$num_threads"

[ -z "$add_deltas" ] && add_deltas=`cat $srcdir/add_deltas 2>/dev/null`
[ -z "$norm_vars" ] && norm_vars=`cat $srcdir/norm_vars 2>/dev/null`
[ -z "$subsample_feats" ] && subsample_feats=`cat $srcdir/subsample_feats 2>/dev/null` || subsample_feats=false
[ -z "$splice_feats" ] && splice_feats=`cat $srcdir/splice_feats 2>/dev/null` || splice_feats=false

mkdir -p $dir/log
split_data.sh $data $nj || exit 1;
echo $nj > $dir/num_jobs

# Check if necessary files exist.
for f in $srcdir/label.counts $data/feats.scp; do
#for f in $graphdir/TLG.fst ./exp/train_phn_l5_c320/label.counts $data/feats.scp; do
  [ ! -f $f ] && echo "$0: no such file $f" && exit 1;
done

## Set up the features
echo "$0: feature: norm_vars(${norm_vars}) add_deltas(${add_deltas})"
feats="ark,s,cs:apply-cmvn --norm-vars=$norm_vars --utt2spk=ark:$sdata/JOB/utt2spk scp:$sdata/JOB/cmvn.scp scp:$sdata/JOB/feats.scp ark:- |"
$add_deltas && feats="$feats add-deltas ark:- ark:- |"
$splice_feats && feats="$feats splice-feats --left-context=1 --right-context=1 ark:- ark:- |"
$subsample_feats && feats="$feats subsample-feats --n=3 --offset=0 ark:- ark:- |"
##

#$cmd JOB=1:$nj $dir/log/decode.JOB.log \ 
#	net-output-extract --class-frame-counts=$srcdir/label.counts --apply-log=true --use-gpu="no" $srcdir/$mdl "$feats" ark,t:output.txt
#exit 1;
# Decode for each of the acoustic scales
$cmd JOB=1:$nj $dir/log/decode.JOB.log \
  net-output-extract --class-frame-counts=$srcdir/label.counts --apply-log=true --use-gpu="yes" $srcdir/$mdl "$feats" ark,t:$dir/trans.JOB.log || exit 1:
