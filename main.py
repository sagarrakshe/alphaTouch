#! /usr/bin/python

'''
/* Copyright (c) 2013, Sagar Rakshe <sagarrakshe2@gmail.com>  
**
** Permission to use, copy, modify, and/or distribute this software for  
** any purpose with or without fee is hereby granted, provided that the  
** above copyright notice and this permission notice appear in all copies.  
**
** THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL  
** WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED  
** WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR  
** BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES  
** OR ANY DAMAGES WHATSOEVER RESULTING FORM LOSS OF USE, DATA OR PROFITS,  
** WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,  
** ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS  
** SOFTWARE.  
*/ 
'''

import commands
import time
import subprocess, shlex
import os
import ast

#Global variables
Left = 0
Right = 0
Top = 0
Bottom = 0

timeLimit = 0
Dot=[]
patterns = []
applications = []

def initialize():
	global patterns
	global applications

	patternFile = open("mapPattern","r")
	patternFileContent = patternFile.read()
	patternFile.close()

	patterns = eval(patternFileContent)
	#print patterns

	applicationFile = open("applications", "r")
	applicationFileContent = applicationFile.read()
	applicationFile.close()

	applications = eval(applicationFileContent)
	#print applications

#Read from the configuration file.
def createGrid():
	global timeLimit

	xDelta = 0
	yDelta = 0

	dotFile = open("CONFIGURATION","r")
	dotContent = dotFile.readlines()
	dotFile.close()

	Left = int(dotContent[0].strip('\n').split(' ')[1])
	Right = int(dotContent[1].strip('\n').split(' ')[1])
	Top = int(dotContent[2].strip('\n').split(' ')[1])
	Bottom = int(dotContent[3].strip('\n').split(' ')[1])

	timeLimit = dotContent.pop().strip().split(':')[1]

	#print Left, Right, Top, Bottom

	xDelta = (Right-Left)/4
	yDelta = (Bottom-Top)/4

	#print xDelta, yDelta

	x=Left; y=Top
	for i in range(5):
		for j in range(5):
			Dot.append((x,y))
			x += xDelta
		y += yDelta
		x = Left
	
	#print Dot

def isPresent(point):
	for i in range(0,len(Dot)):
		if ((Dot[i][0]-point[0])**2 + (Dot[i][1]-point[1])**2 - 500**2) <0:
			return i+1

def pattern(points):
	temp=[]
	numbers=[]

	for i in points:
		for j in i:
			point = isPresent(j)
			if point not in temp and point:
				temp.append(point)
		numbers.append(temp)
		temp=[]
	print numbers

	for i in range(len(patterns)):
		if numbers == patterns[i][0]:
			app = applications[patterns[i][2]]
			print app
			subprocess.Popen([app])
	
def main():
	global timeLimit

	initialize()

	createGrid()

	#print timeLimit
	command = 'timeout ' + timeLimit +' synclient -m 100 > .patternDrawn'
	subprocess.call(command, shell=True)

	file = open('.patternDrawn','r')
	lines = file.readlines()
	
	temp=[]
	Lines=[]
	lineNumber=-1

	for i in lines:
		line = filter(lambda x: x!='',i.split(' '))
		if not (line[0]=='time'):
			if not (line[4] == '0'):
				temp.append((int(line[1]), int(line[2])))
			elif (len(temp) > 0):
				Lines.append(temp)
				temp=[]
				
	pattern(Lines)

	file.close()
	os.remove("./.patternDrawn")

if __name__=='__main__':
	main()