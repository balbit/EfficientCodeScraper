# Github Code Scraper

Scripts to scrape source code from Github in sequential order through obtaining repo data from its API, cloning desired repositories, and dumping programming code into the folder got/

Edit lastid.txt to select which id to start scraping from
Run ./run.sh {{token}} to download one batch of data, where {{token}} is the fine-grained token.

The executed command should look something like 
```./run.sh github_pat_12345...```


Edit ext to change the list of allowed extensions
Information including star count and license are in repolinks.txt

---

Author: Elliot Liu, MediaTek Research Intern
