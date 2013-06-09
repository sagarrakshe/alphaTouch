#!/usr/bin/python

import commands
import math
import os

print "Configuring your touch-pad..."

#Diagonal-1
print "Slowly move your hand diagonally from Top-Left corner to Bottom-Right corner. Don't lift your hand."
commands.getoutput('timeout 4 synclient -m 100 > file1')
print "Once again repeat the same movement."
commands.getoutput('timeout 4 synclient -m 100 > file2')

#Diagonal-2
print "\nSlowly move your hand diagonally from Top-Right corner to Bottom-Left corner. Don't lift your hand."
commands.getoutput('timeout 4 synclient -m 100 > file3')
print "Once again repeat the same movement."
commands.getoutput('timeout 4 synclient -m 100 > file4')

file1 = open('file1','r')
contentFile1 = file1.readlines()
file1.close()

file2 = open('file2','r')
contentFile2 = file2.readlines()
file2.close()

file3 = open('file3','r')
contentFile3 = file3.readlines()
file3.close()

file4 = open('file4','r')
contentFile4 = file4.readlines()
file4.close()

#X-min
X = []
X.append(filter(lambda x: x!='',contentFile1[2].split(' '))[1])
X.append(filter(lambda x: x!='',contentFile2[2].split(' '))[1])

X.append(filter(lambda x: x!='',contentFile3[-2].split(' '))[1])
X.append(filter(lambda x: x!='',contentFile4[-2].split(' '))[1])

xMin = int(math.floor((int(X[0]) + int(X[1]) + int(X[2]) + int(X[3]))/4))

print X
print xMin

#X-max
X = []
X.append(filter(lambda x: x!='',contentFile1[-2].split(' '))[1])
X.append(filter(lambda x: x!='',contentFile2[-2].split(' '))[1])

X.append(filter(lambda x: x!='',contentFile3[2].split(' '))[1])
X.append(filter(lambda x: x!='',contentFile4[2].split(' '))[1])

xMax = int(math.floor((int(X[0]) + int(X[1]) + int(X[2]) + int(X[3]))/4))

print X
print xMax

#Y-min
Y = []
Y.append(filter(lambda x: x!='',contentFile1[2].split(' '))[2])
Y.append(filter(lambda x: x!='',contentFile2[2].split(' '))[2])

Y.append(filter(lambda x: x!='',contentFile3[2].split(' '))[2])
Y.append(filter(lambda x: x!='',contentFile4[2].split(' '))[2])

yMin = int(math.floor((int(Y[0]) + int(Y[1]) + int(Y[2]) + int(Y[3]))/4))

print Y
print yMin


#Y-max
Y = []
Y.append(filter(lambda x: x!='',contentFile1[-2].split(' '))[2])
Y.append(filter(lambda x: x!='',contentFile2[-2].split(' '))[2])

Y.append(filter(lambda x: x!='',contentFile3[-2].split(' '))[2])
Y.append(filter(lambda x: x!='',contentFile4[-2].split(' '))[2])

yMax = int(math.floor((int(Y[0]) + int(Y[1]) + int(Y[2]) + int(Y[3]))/4))

print Y
print yMax

os.remove("file1")
os.remove("file2")
os.remove("file3")
os.remove("file4")

#Creating configuration file
config = open("CONFIGURATION","w")

config.write("Left: " + str(xMin)+'\n')
config.write("Right: " + str(xMax)+'\n')
config.write("Top: " + str(yMin)+'\n')
config.write("Bottom: " + str(yMax)+'\n\n')

config.write("Time-Limit: 8\n")

config.close()
