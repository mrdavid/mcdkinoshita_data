#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DATA_DIR="$( echo $DIR )/../../00_data/"
OUTPUT="$( echo $DATA_DIR)mcd_homepage_new_items_raw.html"

if [ -f $OUTPUT ]; then
   echo "File $FILE exists. Not downloading again."
else
   echo "File $FILE does not exist. Downloading."
   wget -O $OUTPUT http://www.mcdonalds.co.jp/campaign/archive/
fi

python $DIR/mcd_new_items_parse.py $OUTPUT
