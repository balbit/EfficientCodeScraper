# getcontents.py searches through all current repositories in repolinks.txt and downloads 
# ones that haven't been downloaded already

# Currently, no filtering is being done, so all repositories are being downloaded. 
# Filtering can be easily added according to any of these attributes, avoiding unnecessary downloads:
# id  url full_name   stargazers_count    language    size    license

import csv
import subprocess
import json

idfile = open('doneids.txt','r+')
donelist = eval(idfile.read())
#print (donelist)
idfile.seek(0)

bad_licenses = {"lgpl-3.0", "agpl-3.0", "lgpl-2.1", "gpl-3.0", "gpl-2.0"} # Taken from ROOTS

with open('repolinks.txt', 'r') as f:
	R = csv.DictReader(f, delimiter='\t')
	for row in R:
		id = int(row['id'])
		if not id in donelist:
			if True:
#			if not row['license'] in bad_licenses:
				subprocess.run('./getrepo.sh ' + str(row['full_name']), shell=True)
				donelist.append(id)

idfile.write(str(donelist))
idfile.truncate()
