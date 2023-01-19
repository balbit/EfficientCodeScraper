#!/bin/bash

if (($# < 1)); then
	echo "Input your token after the command"
	exit 0
fi

echo "0" > down


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
sleep 1;
done
