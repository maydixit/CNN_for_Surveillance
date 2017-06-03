import sys
import os
from subprocess import check_output
import subprocess

path = sys.argv[1]
print "path: " ,path
model = sys.argv[2]
print "model: ", model

def extract_score(line):
	return float(line.split(" ")[3].replace(")", ""))

cmd = "ls " +path 
proc = subprocess.Popen(cmd, shell=True ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
files = proc.communicate()[0] 

a = 0
b = 0

for file in files.split('\n'):
	abandoned = 0
	background = 0
	
	
	if file is "": 
		continue 
	cmd_classify = "python classify.py " + path + file + " " + model + " labels/bag_detection.txt"
	print cmd_classify
	proc_classify = subprocess.Popen(cmd_classify, shell=True ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	lines = proc_classify.communicate()[0].split('\n')
	print file
	for line in lines:
		if 'score' in line:
			score = extract_score(line)
			if 'abandoned' in line: 
				abandoned = score
			else:
				background = score
	if abandoned > background: 
		a += 1
	else: 
		b += 1
	print a, b

print "Abandoned: " , a 
print " Background: ", b
