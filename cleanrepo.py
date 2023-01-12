import json
import requests
import sys

f = open('repolist.txt')

l = json.load(f)

imp = ['id','url','full_name','stargazers_count','language','size']



if len(sys.argv) > 1 and len(sys.argv[1]) <= 1:
	print('\t'.join(imp + ['license']))
	sys.exit()

tok = sys.argv[1] if len(sys.argv)>1 else ''


for e in l:
#	print(e['url'])
	try:
		info = requests.get(e['url'], headers={'Authorization':'Bearer '+tok}).json()
#		print(info)
		li = 'null'
		try:
			li = info['license']['key']
		except:
			li = 'null'
		print('\t'.join([str(info[r]) for r in imp] + [li]))
	except:
		pass			
t = open('lastid.txt', 'w')
t.write(str(l[-1]['id']))
