# Github Code Scraper

Scripts to scrape source code from Github in sequential order through obtaining repo data from its API, cloning desired repositories, and dumping programming code into the folder ```got/```

Information including star count and license are stored in ```repolinks.txt```

## Instructions for Usage

+ Edit the simlink ```got/``` to a desired folder for output, or simply create a directory called ```got/```
+ **Edit lastid.txt to select which id to start scraping from**
  + This is especially important for parallel downloading, as the script scrapes in sequential order starting from the given ID
+ Run ./run.sh {{token}} to download one batch of data (100 repos), where {{token}} is your fine-grained access token.

Follow the instructions [here](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/#:~:text=Fine%2Dgrained%20PATs%20are%20available,in%20your%20account's%20Developer%20Settings.) to create a token, or simply go to your [Github developer settings](https://github.com/settings/tokens?type=beta). 

Then the executed command should look something like 
```./run.sh github_pat_12345...```

## Adding Filtering

Currently the program does no filtering (it simply clones all found repositories and downloads all their programming files) but it can be added through editing ```getcontents.py```, which can decide which files to download based on stars/language/size/license/etc. 

Edit ```ext``` to change the list of allowed extensions

---

Author: Elliot Liu, MediaTek Research Intern
