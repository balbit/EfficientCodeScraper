#!/bin/bash

reg="\\.("$(paste ext -sd'|')")\$"

gh repo clone $1 tmp_dir

sz () {
	du -s $1 | cut -f1
}

mysize=$(sz tmp_dir)

echo $(($(cat down) + $mysize)) > down

# find tmp_dir | egrep "\.(cs|cpp|cxx|hpp|c++|h++|cc|hh|C|H|go|java|js|lua|php|php3|php4|php5|phps|phpt|py|rb|rs|scala|ts|tsx|v|vhdl)$" > todo.txt
find tmp_dir -type f | egrep $reg > todo.txt

filename=$(echo "$1" | tr / \#) # The pound sign is not used for github repos

echo $filename

touch tgot/$filename

while read -r i; do cat $i >> tgot/$filename; done < todo.txt

addedsize=$(sz tgot/$filename)

mv tgot/$filename got/$filename

rm -rf tmp_dir

echo -e $mysize'\t'$addedsize >> quality
