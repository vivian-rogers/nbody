from generateBodies import MstBodies
#Return the color as a hex value
def getColor(i):
	return MstBodies()[i][5]
#Return the name of the body
def getName(i):
	return MstBodies()[i][0]
#Return the mass of a body
def getMass(i):
	return MstBodies()[i][1]
#Retrun x cord of a body
def getXCord(i):
	return MstBodies()[i][2][0]
#Retrun y cord of a body
def getYCord(i):
	return MstBodies()[i][2][1]
#Retrun z cord of a body
def getZCord(i):
	return MstBodies()[i][2][2]
#Retrun x vel of a body
def getXVel(i):
	return MstBodies()[i][3][0]
#Retrun y vel of a body
def getYVel(i):
	return MstBodies()[i][3][1]
#Retrun z vel of a body
def getZVel(i):
	return MstBodies()[i][3][2]