import fileinput, sys, os

fileInput = raw_input("Input file name?: ")
fileOutput = raw_input("Output file name?: ")

f1 = open(fileInput, 'r')
f2 = open('temp.txt', 'w')

lines = f1.readlines()

for i in range(38,107):
	d = lines[i]
	f2.write(d)
	
f1.close()
f2.close()
	
f1 = open('temp.txt', 'r')
f2 = open(fileOutput,'w')

c = f1.read()
c = c.replace(',','')	#Getting rid of commas
c = c.replace('0','-')	#Converting 0s to -s
c = c.replace('0 ','-')	
c = c.replace(' ','')	#Getting rid of whitespace


c = c.replace('2','R')	#Replace 2 with bricks
c = c.replace('3','B')	#Replace 3 with Bridges
c = c.replace('4','C')	#Replace 4 with crates
c = c.replace('5','D')	#Replace 5 with dirt

c = c.replace('7','S')	#Replace 7 with stone
c = c.replace('8','T')	#Replace 8 with tree?

f2.write(c)

f1.close()
os.remove('temp.txt')
f2.close()

