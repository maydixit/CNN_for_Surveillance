import sys
import os
from subprocess import check_output
import subprocess

path = str(sys.argv[1])
print ("path: " ,path)
model = str(sys.argv[2])
print ("model: ", model)

def extract_score(line):
        return float(line.split()[3].replace(")", ""))

cmd = "ls " +path 
proc = subprocess.Popen(cmd, shell=True ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
files = proc.communicate()[0] 

a = 0
b = 0
for filename in files.splitlines():
        abandoned = 0
        background = 0
        
        filename = filename.decode('ascii')     
        if filename is "": 
                continue
        print (filename) 
        cmd_classify = "python classify.py " + path + filename + " " + model + " labels/bag_detection.txt"
        proc_classify = subprocess.Popen(cmd_classify, shell=True ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        lines = proc_classify.communicate()[0].splitlines()
        print (cmd_classify)
        for line in lines:
                line = line.decode('ascii')
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
        print ("scores: " , abandoned, background)
        print ("counts: " , a, b )
print ("Abandoned: " , a )
print (" Background: ", b)
