import csv
import subprocess
import json

idfile = open('doneids.txt','r+')
donelist = eval(idfile.read())
#print (donelist)
idfile.seek(0)

with open('repolinks.txt', 'r') as f:
	R = csv.DictReader(f, delimiter='\t')
	for row in R:
		id = int(row['id'])
		if not id in donelist:
			subprocess.run('./getrepo.sh ' + str(row['full_name']), shell=True)
			donelist.append(id)

idfile.write(str(donelist))
idfile.truncate()
