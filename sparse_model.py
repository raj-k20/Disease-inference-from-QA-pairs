import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import nltk
from os import walk
import os

import codecs
stemmer = LancasterStemmer()

def bets(add):
	with codecs.open(add , 'r' , "utf-8") as f:
		pol = f.readlines()
	return pol

def trainin_data(texps,add,nam):
	training = []
	with codecs.open(add , 'r' , "utf-8") as f:
		pol = f.readlines()
	for i, l in enumerate(texps):
		for ki in pol:
			if l.split() == ki.split():
				#print l
				training.append({"class":os.path.splitext(nam)[0] ,"sentence":texps[i]})
	return training

bek =[]
path = '/home/rajesh/Desktop/bridges'
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			bek.extend(bets(dirpath+'/'+name))
        '''print "filename"+name
        for l in bek:
            print l.decode("utf-8").encode("ascii").strip()'''


kil = []
for it in bek:
	kil.append(it.decode("utf-8").encode("ascii").strip())

hidn =[]
pathh = '/home/rajesh/Desktop/bridgehid'
for (dirpath, dirnames, filenames) in walk(pathh):
    for name in filenames:
        if name.endswith((".txt")):
            hidn.extend(bets(dirpath+'/'+name))

hidnn = []
pathhh = '/home/rajesh/Desktop/bridgehid'
for (dirpath, dirnames, filenames) in walk(pathh):
    for name in filenames:
        if name.endswith((".txt")):
            hidn.extend(bets(dirpath+'/'+name))

wil = []
for it in hidn:
        wil.append(it.decode("utf-8").encode("ascii").strip())


qil = [] 
for it in hidnn:
        qil.append(it.decode("utf-8").encode("ascii").strip())


training_data=[]
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			training_data.extend(trainin_data(kil,dirpath+'/'+name,name))

hiden_la=[]
for (dirpath, dirnames, filenames) in walk(pathh):
    for name in filenames:
        if name.endswith((".txt")):
            hiden_la.extend(trainin_data(wil,dirpath+'/'+name,name))

hiden_la2=[]
for (dirpath, dirnames, filenames) in walk(pathhh):
    for name in filenames:
        if name.endswith((".txt")):
            hiden_la2.extend(trainin_data(wil,dirpath+'/'+name,name))


words = []
hidwords = []
hidwords2 = []
classes = []
documents = []
hiddocuments = []
hiddocuments2= []
ignore_words = ['?']
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

for pattern in hiden_la:
    w = nltk.word_tokenize(pattern['sentence'])
    hidwords.extend(w)
    hiddocuments.append((w, pattern['class']))
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

for pattern in hiden_la2:
    w = nltk.word_tokenize(pattern['sentence'])
    hidwords2.extend(w)
    hiddocuments2.append((w, pattern['class']))
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))
hidwords = [stemmer.stem(w.lower()) for w in hidwords if w not in ignore_words]
hidwords = list(set(hidwords))
hidwords2 = [stemmer.stem(w.lower()) for w in hidwords2 if w not in ignore_words]
hidwords2 = list(set(hidwords2))
# remove duplicates
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# create our training data
training = []
hidden1 = []
hidden2 = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern

    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]    

    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag

for doc in hiddocuments:
    
    hidbag = [] 

    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]    

    for w in words:
        hidbag.append(1) if w in pattern_words else hidbag.append(0)
    hidden1.append(hidbag)


for doc  in hiddocuments2:
    hidbag2 =[]
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        hidbag2.append(1) if w in pattern_words else hidbag2.append(0)
    hidden2.append(hidbag2)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)



# sample training/output
i = 0
w = documents[i][0]
print ([stemmer.stem(word.lower()) for word in w])
print (training[i])
print (output[i])
print (hidden1[0])
print len(hidden1)
print len(hidden2)
print hiddocuments2
'''for doc in hiddocuments2:
    
    hidbag = [] 

    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]    

    for w in words:
        hidbag.append(1) if w in pattern_words else hidbag.append(0)
    hidden2.append(hidbag)'''
