import copy, numpy as np
np.random.seed(0)
from mark5 import *
 
# compute sigmoid nonlinearity
def sigmoid(x):
	output = 1/(1+np.exp(-x))
	return output
 
# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
	return output*(1-output)
 

 
# input variables
alpha = 0.1
input_dim = len(training[0])
hidden_dim = len(training[0])
output_dim = len(classes)
 
 
# initialize neural network weights
synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1
synapse_1 = 2*np.random.random((hidden_dim,output_dim)) - 1
synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) - 1

 
synapse_0_update = np.zeros_like(synapse_0)
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)
overallError = 0
# training logic
for j in range(10000):
 
 
	layer_2_deltas = list()
	layer_1_values = list()
	layer_1_values.append(np.zeros(hidden_dim))
 
# moving along the positions in the binary encoding
	X = np.array(training)
	y = np.array(output)
 
	layer_1 = sigmoid(np.dot(X,synapse_0))
 
# output layer (new binary representation)
	layer_2 = sigmoid(np.dot(layer_1,synapse_1))
 
# did we miss?... if so, by how much?
	layer_2_error = y - layer_2
	for r in range(len(layer_2_error)):
		layer_2_deltas.append((layer_2_error[r])*sigmoid_output_to_derivative(layer_2[r]))
	overallError += np.abs(layer_2_error[0])
 
# store hidden layer so we can use it in the next timestep
	layer_1_values=[]
	for k in layer_1:
		layer_1_values.append(k)
	future_layer_1_delta = np.zeros(hidden_dim)

	print "------------------------------------"
	print len(layer_2_deltas[0])
	print len(layer_2_error[0])
	print len(layer_1_values[0])
	bindd = len(training)
	for pos in range(bindd):
		X = np.array(training[pos])
		layer_1 = layer_1_values[-pos-1]
		prev_layer_1 = layer_1_values[-pos-2] 
		#print pos
		#print len(layer_1)
 		#print "--------------------------------------------"
# error at output layer    
		layer_2_delta = layer_2_deltas[-pos-1]
 		#print layer_1
 		temp=[]
 		for k in range(len(layer_1)):
 			temp.append(layer_2_delta.dot(synapse_1.T) * sigmoid_output_to_derivative(layer_1[k]))
 		print(len(layer_2_delta))
 		print(len(layer_1))
		layer_1_delta = (future_layer_1_delta.dot(synapse_h.T)) + temp
# let's update all our weights so we can try again
		#print len(layer_1)
		#print len(layer_2_delta)
		synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
		synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
		synapse_0_update += X.T.dot(layer_1_delta)
	future_layer_1_delta = layer_1_delta
 
 
	synapse_0 += synapse_0_update * alpha
	synapse_1 += synapse_1_update * alpha
	synapse_h += synapse_h_update * alpha   
 
	synapse_0_update *= 0
	synapse_1_update *= 0
	synapse_h_update *= 0
# print out progress
	if(j % 1000 == 0):
		print "Error:" + str(overallError)
		#print "Pred:" + str(d)
		#print "True:" + str(c)