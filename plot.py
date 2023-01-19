import matplotlib.pyplot as plt
import numpy as np
import math

f = open('quality')
l = f.readlines()

items = []
x = []
y = []
s = []
c = []
for e in l:
	try:
		a,b=map(int, e.split()) # data downloaded, data used
		x.append(math.log10(a))
		y.append(b/a)
		s.append(15 + math.log10(a)*0.5)
		c.append(-(0.2-b/a) * (a + 3000)) 
	except:
		pass
# mapping "badness": 
# We set the standard for a decent scrape to 0.2 content ratio, 
# and then weigh it by how much time it consumes, which we approximate
# with the downloaded data amount + 3MB, which should cover for the base
# API query time
# Basically if we can find a way to remove the really bad nodes it'll help speed a lot

tt = sorted(c)[int(len(c)*0.03)] # normalize 3% of worst offenders
c = [max(tt, e) for e in c]

plt.title("Programming code fertility by repository")
plt.xlabel("log(kB of data downloaded)")
plt.ylabel("Ratio of programming code (by kB)")

plt.scatter(np.array(x), np.array(y), np.array(s), c=np.array(c), cmap='RdYlGn', alpha=0.75)
plt.show()
