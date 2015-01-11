#Assign countries to players

print "RISK... The Game of World Domination!\n"

#List for initial random assignment of countries.
#ISSUE: COUNTRIES GOES FROM 0-41, WHILE ALL ELSE GOES FROM 1-42. NEEDS TO BE CHANGED!!!
countries=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#List of names of countries, corresponding to c1-c42 lists of country info, where cnames[0]="n/a"
cnames = ["n/a","Eastern Australia","Western Australia","New Guinea","Indonesia","Siam","China","Mongolia","Japan","Kamchatka","Yakutsk","Irkutsk","Sibera","Ural","Afghanistan","India","Middle East","Ukraine","Scandanavia","Northern Europe","Southern Europe","Western Europe","Great Britain","Iceland","Greenland","Northeast Territory","Alaska","Alberta","Ontario","Quebec","Eastern United States","Western United States","Central America","Venezuela","Peru","Argentina","Brasil","Northern Africa","Congo","Southern Africa","Madagascar","Eastern Africa","Egypt"]

#Random mechanism for assigning countries.
import random
a = range(42)
b = random.sample(a, len(a))
# c = sorted(b) ... Confirms that b contains all of the elements of a

#Integer input for number of players.
numberofplayers = input("Number of players: ")
#Computer's got etiquette.
print "Thank You!"

#assign player numbers to countries list
#A MORE ELEGANT SOLUTION TO THIS IS DESIRED
# The same player numbers are assigned the extra countries. 
#	SOLUTION: RANDOMIZE PLAYER NUMBERS AFTER ASSIGNMENT?
#	SOLUTION: Create a Random distribution of extra countries!
if numberofplayers == 2:
	for x in range (0,14):
		countries[b[x]]=1
	for x in range (14,28):
		countries[b[x]]=2
	for x in range (28,42):
		countries[b[x]]=3
if numberofplayers == 3:
	for x in range (0,14):
		countries[b[x]]=1
	for x in range (14,28):
		countries[b[x]]=2
	for x in range (28,42):
		countries[b[x]]=3
if numberofplayers == 4:
	for x in range (0,10):
		countries[b[x]]=1
	for x in range (10,21):
		countries[b[x]]=2
	for x in range (21,32):
		countries[b[x]]=3
	for x in range (32,42):
		countries[b[x]]=4
if numberofplayers == 5:
	for x in range (0,8):
		countries[b[x]]=1
	for x in range (8,16):
		countries[b[x]]=2
	for x in range (16,24):
		countries[b[x]]=3
	for x in range (24,33): #Giving extra country to player 4
		countries[b[x]]=4
	for x in range (33,42): #Giving extra country to player 5
		countries[b[x]]=5
if numberofplayers == 6:
	for x in range (0,7):
		countries[b[x]]=1
	for x in range (7,14):
		countries[b[x]]=2
	for x in range (14,21):
		countries[b[x]]=3
	for x in range (21,28):
		countries[b[x]]=4
	for x in range (28,35):
		countries[b[x]]=5
	for x in range (35,42):
		countries[b[x]]=6

#Display the country player assignments.		
print countries

#Counting # of countries each player has.
nump0c=0
nump1c=0
nump2c=0
nump3c=0
nump4c=0
nump5c=0
nump6c=0

for x in range (0,42):
	if countries[x]==0:
		nump0c = nump0c + 1
	if countries[x]==1:
		nump1c = nump1c + 1
	if countries[x]==2:
		nump2c = nump2c + 1
	if countries[x]==3:
		nump3c = nump3c + 1
	if countries[x]==4:
		nump4c = nump4c + 1
	if countries[x]==5:
		nump5c = nump5c + 1
	if countries[x]==6:
		nump6c = nump6c + 1
print nump0c, nump1c, nump2c, nump3c, nump4c, nump5c, nump6c

#Defining countries by lists, in range (1,43)
#NEEDS TO BE COMPLETED!!!
c1 = [0,0,2,3,0,0,0,0]
c2 = [0,0,1,3,4,0,0,0]
c3 = [0,0,1,2,4,0,0,0]
c4 = [0,0,2,3,5,0,0,0]
c5 = [0,0,4,6,15,0,0,0]
c6 = [0,0,5,7,12,13,14,15]
c7 = [0,0,6,8,9,11,12,0]
c8 = [0,0,7,9,0,0,0,0]
c9 = [0,0,7,8,10,11,26,0]
c10 = [0,0,9,11,12,0,0,0]
c11 = [0,0,7,9,10,12,0,0]
c12 = [0,0,6,7,10,11,13,0]
c13 = [0,0,6,12,14,17,0,0]
c14 = [0,0,6,13,15,16,17,0]
c15 = [0,0,5,6,14,16,0,0] 
c16 = [0,0,14,15,17,20,41,42]
c17 = [0,0,13,14,16,18,19,20]
c18 = [0,0,17,19,22,23,0,0]
c19 = [0,0,17,18,20,21,22,0]
c20 = [0,0,16,17,19,21,37,42]
c21 = [0,0,19,20,22,37,0,0]
c22 = [0,0,18,19,21,23,0,0]
c23 = [0,0,18,22,24,0,0,0]
c24 = [0,0,23,25,28,29,0,0]
c25 = [0,0,24,26,27,28,0,0]
c26 = [0,0,9,25,27,0,0,0]
c27 = [0,0,25,26,28,31,0,0]
c28 = [0,0,24,25,27,29,30,31]
c29 = [0,0,24,28,30,0,0,0]
c30 = [0,0,28,29,31,32,0,0]
c31 = [0,0,27,28,30,32,0,0]
c32 = [0,0,30,31,33,0,0,0]
c33 = [0,0,32,34,36,0,0,0]
c34 = [0,0,33,35,36,0,0,0]
c35 = [0,0,34,36,0,0,0,0]
c36 = [0,0,33,34,35,37,0,0]
c37 = [0,0,20,21,36,38,41,42]
c38 = [0,0,37,39,41,0,0,0]
c39 = [0,0,38,40,41,0,0,0]
c40 = [0,0,39,41,0,0,0,0]
c41 = [0,0,16,37,38,39,40,42]
c42 = [0,0,16,20,37,41,0,0]
	
#Check by making a program to print the names of the countries.

initialassign = 0
for initialassign in range(1,43):
	exec "c%s[0] = countries[%s-1]" % (initialassign,initialassign)
	exec "print cnames[%s],': ', c%s" % (initialassign,initialassign)

	


#Counting # of countries each player has.
nump0c=0
nump1c=0
nump2c=0
nump3c=0
nump4c=0
nump5c=0
nump6c=0

for x in range (0,42):
	if countries[x]==0:
		nump0c = nump0c + 1
	if countries[x]==1:
		nump1c = nump1c + 1
	if countries[x]==2:
		nump2c = nump2c + 1
	if countries[x]==3:
		nump3c = nump3c + 1
	if countries[x]==4:
		nump4c = nump4c + 1
	if countries[x]==5:
		nump5c = nump5c + 1
	if countries[x]==6:
		nump6c = nump6c + 1
print nump0c, nump1c, nump2c, nump3c, nump4c, nump5c, nump6c


