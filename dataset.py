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

	for ki in pol:
		#for i, l in enumerate(texps):
		if ki.split() in (l.split() for i,l in enumerate(texps)):
			#print l
			training.append({"class":os.path.splitext(nam)[0] ,"sentence":ki.decode("utf-8").encode("ascii").strip()})
	return training

bek =[]
path = '/home/rajesh/Desktop/samp'
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			bek.extend(bets(dirpath+'/'+name))

kil = []
for it in bek:
		kil.append(it.decode("utf-8").encode("ascii").strip())

training_data=[]
for (dirpath, dirnames, filenames) in walk(path):
  	for name in filenames:
		if name.endswith((".txt")):
			training_data.extend(trainin_data(kil,dirpath+'/'+name,name))
print "LEngth",len(training_data)
words = []
classes = []
documents = []
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

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

# remove duplicates
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# create our training data
training = []
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
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)
#print len(output[0])
# sample training/output
i = 0
w = documents[i][0]
#print ([stemmer.stem(word.lower()) for word in w])
#print (training[i])
#print (output[i])

