#!/bin/bash

echo "0" > down
d1=$(du -s /media/bo/0123-4567/MTK/got | cut -f1)

for i in $(seq 1); do
echo "Getting List";
s1=$(date +%s);
./getlist.sh $1;
s2=$(date +%s)
echo "Downloading Content";
python3 getcontents.py;
s3=$(date +%s);
echo $(($s2-$s1))" seconds taken to get list";
echo $(($s3-$s2))" seconds taken to download";
d2=$(du -s /media/bo/0123-4567/MTK/got | cut -f1)
echo $(($d2-$d1))", "$(cat down)": took, got";
sleep 1;
done
