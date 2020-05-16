#!/usr/bin/env python

import sys, os.path
from string import *
from sys import argv
from subr import *

if len(argv) < 4:
	print "Usage: %s testing_file testing_output_file training_class" % (argv[0])
	sys.exit(1)

def main():
	original = read_first_column(argv[1])
	test_output = read_first_column(argv[2])
	train_new_class = read_first_column(argv[3])
	percentage = argv[4]

	#print original
	#print test_output
	#print train_new_class

	predict = test_output
	#predict = []
	#for i in range(len(test_output)):
		#idx = atoi(test_output[i][0]) #string to integer
		#print idx, train_new_class[idx-1]
		#predict.append(train_new_class[idx-1])
	#exit()

	if(len(predict) != len(original)):
		print "Error: lines of %s and %s are different." % (argv[1],argv[2])
		sys.exit(1)

	labels = []
	for i in range(len(train_new_class)):
		for lab in train_new_class[i]:
			if (lab not in labels):
				labels.append(lab)

	print "number of labels = %s" % len(labels)

	result = measure(original,predict,labels)
	#print original
	#print predict
	#print labels

	print "Exact match ratio: %s" % result[0]
	print "Microaverage F-measure: %s" % result[1]
	print "Macroaverage F-measure: %s" % result[2]

	record = "{}, {}, {}, {}\n".format(percentage,round(result[0],3),round(result[1],3),round(result[2],3))

	file_fscore = "./UK(3)_(CLO)(1221).csv"
	F_score = open(file_fscore, "a")
	F_score.write(record)

main()