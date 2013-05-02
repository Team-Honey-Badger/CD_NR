import fileinput, sys, os

#Opens up temp file and copies only data portion into temp file

fileInput = raw_input("Input file name?: ")
fileOutput = raw_input("Output file name?: ")

f1 = open(fileInput, 'r')
f2 = open('temp.txt', 'w')

lines = f1.readlines()

for i in range(38,108):
	d = lines[i]
	f2.write(d)
	
f1.close()
f2.close()

#Open temp file to convert from the data portion to usable text file
f1 = open('temp.txt', 'r')
f2 = open(fileOutput,'w')

c = f1.read()

#''' Replacement Definitions '''#

numToReplace = ['4','5','6','7','8','9','10','11',
	'12','13','14','15','16','17','18','19','20','21',
	'22','23','24','25','26','27','28','29','30','31',
	'32','33','34','35','36']

replacementChars = ['B','C','D','S','T','R','L','=','_',
	'|','/','\\','@','#','$','%','X','J','V','I','O','Temp',
	'1','2','3','<','>','q','w','e','r','s','G']

#'''						 '''#

for char, rep in reversed(zip(numToReplace,replacementChars)):
	c = c.replace(char,rep)

c = c.replace(',','')	#Getting rid of commas
c = c.replace('0','-')	#Converting 0s to -s
c = c.replace('0 ','-')	
c = c.replace('Temp','0')
c = c.replace(' ','')	#Getting rid of whitespace

f2.write(c)

f1.close()
os.remove('temp.txt')
f2.close()

