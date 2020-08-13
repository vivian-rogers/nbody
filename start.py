from grabInput import *
import pickle
bodies = []
#Prompts the user if they want to add any bodies, then update everything to the getBodies.txt file
def startup():
	global bodies
	#Promp the user for the question and then store within qest
	qest = question()
	#Check to see if they input yes 
	if(qest == "y" or qest == "Y"):
		#If so prompt for the number of bodies to be added
		numBodies = findNumBodies()
		#For the num of bodies to be added, append the input from from the user to the master list of boides 
		for x in range(numBodies):
			bodies.append(promptBodyInfo())
		#Store the master list of bodies to a getBodies.txt to update the file
		with open('getBodies.txt', "wb") as f:
			pickle.dump(bodies,f)
		f.close()
		#Clear the current bodies
		bodies.clear()
		#Update the master bodies list to what was updateed to the getBodies.txt
		bodies = convFileToBodies()
#Remove bodies from the master list, please make sure there are bodies to remove before this
def removal():
	global bodies
	#Print the master list of bodies 
	print("List of bodies: \n " + str(bodies))
	#Prompt if user would like to remove any bodies from the master list
	yorn = input("Would you like to remove a body (y/n)?: \n")
	#If yes, prompt the user to input the index for which body they desire to be removed 	
	while(yorn == "y" or yorn == "Y"):
		#Store and ask user for which body they want removed
		x = input("Which body would you like to remove from this list \n" + str(bodies) + " \n")
		#Remove the body of said index
		bodies.pop(int(x))
		#Update the file
		with open('getBodies.txt', "wb") as f:
			pickle.dump(bodies,f)
		f.close()
		#Promp again if the user would like to continue to remove bodies 
		yorn = input("Would you like to continue remove a body (y/n)?: \n")

#Return the master list of bodies 
def MstBodies():
	return bodies

#Ask the user if it's the first time running anything in the program, so that if they're is nothing within the master list it does not attempt to read from it
firstTime = input("Is this the first tile running the file? (y/n): \n")
if(firstTime == 'y' or firstTime == 'Y'):
    f = open("getBodies.txt", "w+")
    f.write("")
    f.close()
else:
    with open('getBodies.txt', "rb") as f:
      bodies = pickle.load(f)
    f.close()

startup()
removal()

#If nothing is in the master list of boides, exit the program
if not bodies:
	exit()