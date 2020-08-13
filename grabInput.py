import pickle
counter = 1
#Prompt the user to enter the number of bodies they want to append and return value
def findNumBodies(): 
     numBodies = input("Please enter the number of bodies to add in this simulation: \n")
     return int(numBodies)
#Prompt the user for all data related to the new body and return said body
def promptBodyInfo():
     global counter
     bodyInfo = []
     bodyInfo.append(input("Please enter the name of the " + str(counter) + " body: \n"))
     bodyInfo.append(float(input("Please enter the mass of the " + str(counter) + " body in kg: \n")))
     tempCords = input("Please enter the cords of the " + str(counter) + " body in meters: \n").split()
     bodyInfo.append(list(map(float, tempCords)))
     tempVelocity = input("Please enter the velocity in 3d space of the " +str(counter)+" body in m/s: \n").split()
     bodyInfo.append(list(map(float, tempVelocity)))
     tempColor = input("Please enter the color of the "+str(counter)+" body in hex: \n")
     bodyInfo.append(int(tempColor))
     counter+=1
     return bodyInfo
#Prompt the user to ask if they want to add more bodies to the master list 
def question():
     q = input ("Would you like to add more bodies to the current list? (y/n) \n")
     return q
#Read the data currently in the getBodies.txt and add to a list, and return
def convFileToBodies():
     bCopy = []
     with open('getBodies.txt', "rb") as f:
          bCopy = pickle.load(f)
     f.close()
     return bCopy
