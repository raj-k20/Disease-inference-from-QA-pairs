from os import walk
import sys
import os
import re
import sys
import networkx as nx
import urllib2
from itertools import combinations
def all_pairs(items):
    """Make all unique pairs (order doesn't matter)"""
    pairs = []
    nitems = len(items)
    for i, wi in enumerate(items):
        for j in range(i+1, nitems):
            pairs.append((wi, items[j]))
    return pairs

def co_occurrences(lines, words):
    
    wpairs = all_pairs(words)

    co_occur = {}
    for w1, w2 in wpairs:
        rx = re.compile('%s .*%s|%s .*%s' % (w1, w2, w2, w1))
        co_occur[w1, w2] = sum([1 for line in lines if rx.search(line)])
    print "\n\co-occur\n\n",co_occur

    return co_occur

def create_wordhist(lines, words):
	word_hist={}	
	for l in words:
		word_hist[l] = 0
		for k in lines:
			if l in k:
				word_hist[l] = word_hist[l]+1

	return word_hist


       
def co_occurrences_graph(word_hist, co_occur, cutoff=1):

    g = nx.Graph()
    for word, count in word_hist.items():
        g.add_node(word, count=count)
    for (w1, w2), count in co_occur.iteritems():
        if count<=cutoff:
            continue
        g.add_edge(w1, w2, weight=count)
    return g
def bets(add):
	final=[]
	with open(add,'r') as fil:
		bet = fil.readlines()
	for l in bet:
		final.append(l.strip().replace(',',' '))
	return final

def normally(bek):
	kil=[]
	for k in bek:
			kil.append(k.strip())
	return kil

L1=[]
L2=[]
po=[]
path = '/home/rajesh/Desktop/bridges'
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			L1.append(bets(dirpath+'/'+name))
			po.append(name)

path = '/home/rajesh/Desktop/bridges1'
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			L2.append(bets(dirpath+'/'+name))

def writehid(datas,fnames):
	path2 = '/home/rajesh/Desktop/bridgehid'
	for k,l in zip(datas,fnames):
		with open(path2+'/'+l,'w') as fils:
			fils.write(k)



def k_cliques(graph):
    # 2-cliques
    #print graph.edges()
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 4
    
    while cliques:
        # result
        yield k, cliques
        
        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u, v in combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u | w))
        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1
def print_cliques(graph):
	hiddenl = []
	numcl = []
	for k, cliques in k_cliques(graph):
		hiddenl.append(cliques)
		numcl.append(k)
		info = k, len(cliques), cliques[:3]
		print('%d-cliques: #%d, %s ...' % info)
		print "you have cliques"
	return hiddenl,numcl

print L1
#print L2
ko = []
lo = []
for j,k in zip(L1,L2):
	gip = {}
	bik={}
	gip = co_occurrences(k, j)
	bik = create_wordhist(k, j)
	#print "cooccurences ________________________________________________"
	#print co_occurrences(k, j)
	#print"_______________________________________________________________"
	print bik
	gg =  co_occurrences_graph(bik, gip)
	#print gg.nodes()
	print gg.edges()
	ch , mk = print_cliques(gg)
	ko.append(ch)
	lo.append(mk)
print "\n ----------------------------------------------- \n"
print "GIP",gip
path2 = '/home/rajesh/Desktop/bridgehid'

for ki,li,pi in zip(ko,lo,po):
	#print len(ki) , len(li)
	leno = len(li)
	i = 0
	with open(path2+'/'+pi,'w') as fils:
		while(leno != 0):
			pl = []
			if i > 1:
				fils = open(path2+'/'+pi,'a')
			#print k[i]
			for pit in ki[i]:
				fils.write(str(pit)+"\n")
			i=i+1
			leno = leno - 1