from pymedtermino import *
from pymedtermino.snomedct import *
from os import walk
import os
l=[]

def createsno(add,name):
	print add
	con=[]
	rep=[]
	per=[]
	with open(add) as fil:
		a = fil.readlines()
	a=[i.strip("\r\n") for i in a]

	for l in a:
		con.append(SNOMEDCT.search(l))
	finalArray=[]
	for i in con:
		results=[]
		for j in i:
			temp1=str(j).split("#")[0].split('[')[1].split(']')[0]
			results.append(temp1)
		finalArray.append(results)
	print "finalArrayLength",len(finalArray)
	print finalArray
	p1='/home/rajesh/Desktop/snownew'
	with open(p1+'/'+name,'w') as mk:
		for m in finalArray:
			if len(m)==0:
				mk.write(""+'\n')
			else:
				mk.write(" ".join(m)+'\n')
	return finalArray
			
'''	for k in con:
		for i,v in enumerate(k):
			rep.append(str(v[i]).split()[0].strip("SNOMEDCT"+'['+']'))
	
	return rep	'''


fep = []
path = '/home/rajesh/Desktop/snow'
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			x=createsno(dirpath+'/'+name,name)

			fep.append([x])
'''for i in fep:
	for j in i:
		print len(j)'''
'''print len(fep)
print fep[0]'''
