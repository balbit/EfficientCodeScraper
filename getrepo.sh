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
mkdir tgot 2> /dev/null
touch tgot/$filename

##################
# Currently, the program concatenates all programming langauge content in the repository into a document, 
# and adds that document to the folder got/ under the name AUTHOR#REPO
# This behavior can be changed by modifying the following lines
##################

while read -r i; do cat $i >> tgot/$filename; done < todo.txt

addedsize=$(sz tgot/$filename)

mv tgot/$filename got/$filename

rm -rf tmp_dir

echo -e $mysize'\t'$addedsize >> quality
