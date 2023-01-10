import json
import requests
import sys

f = open('repolist.txt')

l = json.load(f)

imp = ['id','url','full_name','stargazers_count','language','size']

if len(sys.argv) > 1:
	print('\t'.join(imp + ['license']))
	sys.exit()


for e in l:
#	print(e['url'])
	try:
		info = requests.get(e['url'], headers={'Authorization':'Bearer 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'}).json()
		# print (info)
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
