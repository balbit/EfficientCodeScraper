# Github Code Scraper

Scripts to scrape source code from Github in sequential order through obtaining repo data from its API, cloning desired repositories, and dumping programming code into the folder got/

Currently the program does no filtering (it simply clones all found repositories and downloads all its programming files) but it can be added through editing ```getcontents.py```, which can decide which files to download based on stars/language/size/license/etc. 

Edit lastid.txt to select which id to start scraping from
Run ./run.sh {{token}} to download one batch of data, where {{token}} is the fine-grained token.

The executed command should look something like 
```./run.sh github_pat_12345...```


Edit ext to change the list of allowed extensions
Information including star count and license are in repolinks.txt

---

Author: Elliot Liu, MediaTek Research Intern
