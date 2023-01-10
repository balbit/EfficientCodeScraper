idnum=$(cat lastid.txt)
gh api -H "Accept: application/vnd.github+json" /repositories?since=$idnum > repolist.txt
python3 cleanrepo.py >> repolinks.txt

