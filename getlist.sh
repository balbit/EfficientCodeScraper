#!/bin/bash

# getlist.sh downloads information about the 100 most recent directories after $idnum, 
# which is stored in lastid.txt, and cleans them into repolinks.txt, after which $idnum is updated

idnum=$(cat lastid.txt)
gh api -H "Accept: application/vnd.github+json" /repositories?since=$idnum > repolist.txt
python3 cleanrepo.py $1 >> repolinks.txt

