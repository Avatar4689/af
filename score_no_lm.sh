#!/bin/bash
# Apache 2.0

[ -f ./path.sh ] && . ./path.sh

# begin configuration section.
cmd=run.pl
[ -f ./path.sh ] && . ./path.sh
. parse_options.sh || exit 1;


compute-wer --text --mode=present \
   ark:labels.test ark:predict || exit 1;
exit 0;
