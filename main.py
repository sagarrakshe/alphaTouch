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

#Global variables
Left = 0
Right = 0
Top = 0
Bottom = 0

timeLimit = 0

Dot=[]


'''
dots = [(1300, 900), (2400, 900), (3500, 900), (4600, 900), (5700, 900),
		(1300, 1825), (2400, 1825), (3500, 1825), (4600, 1825), (5700, 1825),
		(1300, 2900), (2400, 2900), (3500, 2900), (4600, 2900), (5700, 2900),
		(1300, 3975), (2400, 3975), (3500, 3975), (4600, 3975), (5700, 3975),
		(1300, 5000), (2400, 5000), (3500, 5000), (4600, 5000), (5700, 5000)]

'''
patterns = [
			[[[2, 7, 12, 17, 22], [2, 3, 4], [4, 9, 14, 19, 24], [12, 13, 14]], 4, 'A'],
			[[[3, 8, 13, 18, 23], [3, 4, 5, 10, 15, 14, 13], [13, 14, 15, 20, 25, 24, 23]], 3, 'B'],
			[[[3, 2, 6, 11, 16, 22, 23]], 1, 'C'],
			[[[3, 8, 13, 18, 23], [3, 4, 10, 15, 20, 24, 23]], 2, 'D'],
			[[[3, 8, 13, 18, 23], [3, 4, 5], [13, 14], [23, 24, 25]], 4, 'E'],
			[[[3, 8, 13, 18, 23], [3, 4, 5], [13, 14]], 3, 'F'], 
			[[[4, 3, 2], [2, 7, 12, 17, 22], [22, 23, 24], [14, 19, 24], [13, 14, 15]], 5, 'G'],
			[[[2, 7, 12, 17, 22], [4, 9, 14, 19, 24], [12, 13, 14]], 3, 'H'],
			[[[2, 3, 4], [3, 8, 13, 18, 23], [22, 23, 24]], 3, 'I'],
			[[[2, 3, 4], [3, 8, 13, 18, 23, 22, 17]], 2, 'J'],
			[[[3, 8, 13, 18, 23], [5, 9, 13], [13, 19, 25]], 3, 'K'],
			[[[3, 8, 13, 18, 23], [23, 24, 25]], 2, 'L'],
			[[[1, 6, 11, 16, 21], [1, 7, 13], [5, 9, 13], [5, 10, 15, 20, 25]], 4, 'M'],
			[[[1, 6, 11, 16, 21], [1, 7, 13, 19, 25], [5, 10, 15, 20, 25]], 4, 'N'],
			[[[3, 2, 7, 12, 17, 22, 23, 24, 19, 14, 9, 4]], 1, 'O'],
			[[[3, 8, 13, 18, 23], [3, 4, 5, 10, 15, 14, 13]], 2, 'P'],
			[[[2, 7, 12, 17, 18, 19, 14, 9, 4, 3], [13, 19, 25]], 2, 'Q'],
			[[[3, 8, 13, 18, 23], [3, 4, 5, 10, 15, 14, 13], [13, 19, 25]], 3, 'R'],
			[[[4, 3, 2, 7, 12, 13, 14, 19, 24, 23, 22]], 1, 'S'],
			[[[2, 3, 4], [3, 8, 13, 18, 23]], 2, 'T'],
			[[[2, 7, 12, 17, 22], [22, 23, 24], [4, 9, 14, 19, 24]], 3, 'U'],
			[[[1, 7, 12, 17, 23], [5, 9, 14, 18, 23]], 2, 'V'],
			[[[1, 6, 11, 16, 21], [21, 17, 13], [13, 19, 25], [5, 10, 15, 20, 25]], 4, 'W'],
			[[[1, 7, 13, 19, 25], [5, 9, 13, 17, 21]], 2, 'X'],
			[[[4, 9, 14, 19, 24], [2, 7, 12], [12, 13, 14]], 3, 'Y'],
			[[[1, 2, 3, 4, 5], [5, 9, 13, 17, 21], [21, 22, 23, 24, 25]], 3, 'Z'],
			[[[3, 8, 13, 18, 23], [11, 12, 13, 14, 15]], 2, '+'],
			[[[23], [17, 18, 19], [11, 12, 13, 14, 15]], 3, '^'],
			[[[3, 2, 1, 6, 11, 16, 21, 22, 23, 24, 25, 20, 15, 10, 5, 4]], 1, '0']
			]

applications ={
				'A':'apt-get',
				'B':'bash',
				'C':'cd ~',
				'D':'date',
				'E':'echo',
				'F':'find',
				'G':'grep',
				'H':'host',
				'I':'ifconfig',
				'J':'jobs',
				'K':'kill',
				'L':'ls',
				'M':'man',
				'N':'nmcli',
				'O':'oclock',	
				'P':'ping',
				'Q':'qmake',
				'R':'reboot',
				'S':'sudo',
				'T':'tty',
				'U':'USB',
				'V':'vim',
				'W':'whoami',
				'X':'xterm',
				'Y':'yum',
				'Z':'zsh',
				
				'+':'Calculator',
				'^':'Wi-Fi',
				'0':'reboot'
				}

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
			
			print applications[patterns[i][2]]

def main():
	global timeLimit

	createGrid()

	#print timeLimit
	command = 'timeout ' + timeLimit +' synclient -m 100 > .pattern'
	subprocess.call(command, shell=True)

	file = open('.pattern','r')
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
	os.remove("./.pattern")

if __name__=='__main__':
	main()