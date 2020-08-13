from os import system
from graphics import *

def calculateAccel(): #given a list of bodies, gives them accelerations from positions
	global bodies
	for i in bodies:
		fathercoords = i[2]
		for accel in i[4]:
			accel = float(0)
		for j in bodies:
			daughtercoords = j[2]
			if(i != j):
				dist = radius(fathercoords,daughtercoords)
				magnitude = i[1] * j[1] * gc / (absradius(dist) ** 3)
				for dim in range(3):
					i[4][dim] += (-1) * magnitude * dist[dim] 		#adds the forces on the object in each dimension
		for dim in range(3):
			i[4][dim] = i[4][dim] / i[1] #divide by mass to get accel	

def radius(coords1,coords2): #calculates distance vector between two coordinates
	rad = [coords1[0]-coords2[0],coords1[1]-coords2[1],coords1[2]-coords2[2]]
	return rad

def absradius(radius): #calculates |distance|
	rsq = 0
	for dim in range(3):
		rsq += radius[dim] ** 2
	return (rsq ** 0.5)

def printPositions(): #prints out all of the body's positions
	global bodies
	for i in bodies:
		print(i[0] + ":	"" mass: " + str(i[1]) + "kg,	coords: (", end = '')
		for j in i[2]:
			print(str(j/au) + ",", end ='')
		print(") a.u.")
	print()

def calculateVel(dt): #calculates velocities for bodies
	global bodies
	for i in bodies:
		for dim in range(3):
			i[3][dim] += i[4][dim] * dt

def calculatePos(dt): #calculates positions from velocities
	global bodies
	for i in bodies:
		for dim in range(3):
			i[2][dim] += i[3][dim] * dt

def scaleForPlot(x):
	return ( winx * x / (3*au) + winx/2)

def massScale(x):
	return (x ** 0.1)/(90*2)

def graphicsInit():
	for i in bodies:
		graphicObjects.append( Circle( Point( scaleForPlot(i[2][0]), scaleForPlot(i[2][1])) , massScale(i[1])))
		#graphicObjects.append( Circle( Point( winx/2 * i[2][0]/au + winx/2, winy/2 * i[2][1]/au + winy/2) , i[1] ** 0.0333))
	for i in graphicObjects:
		i.setFill("black")
		i.draw(win)

def updatePlot():
	for i in range(len(bodies)):
		temp = graphicObjects[i]
		graphicObjects[i] = Circle( Point(int(scaleForPlot(bodies[i][2][0])), int(scaleForPlot(bodies[i][2][1]))) , massScale(bodies[i][1]))
		graphicObjects[i].setFill("black")
		graphicObjects[i].draw(win)
		temp.undraw()
        #graphicObjects[i] = Circle( Point(scaleForPlot(bodies[i][2][0]),scaleForPlot(bodies[i][2][1])), i[1] ** 0.08)
		#graphicObjects.draw(win)

x = []
y = []
labels = []
mass = []
dt=60*60*1 #units of seconds
gc=6.67384 * 10 ** (-9)
#gc=6.67384 * 10 ** (-11)
au = 149597870700
bodies = [
		[	"sun",
			float(1.98925 * 10**28),
			[float(0),float(0),float(0)],
			[float(0),float(-505.94),float(0)],
			[float(0),float(0),float(0)]
		],
		[	"mars_kinda",
			float(6 * (10**26)),				#mass in kg
			[float(149597870700 * 0.5),float(0),float(0)], 	#location in metres, xyz
			[float(-25*10),float(50.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]				#acceleration m/s/s
		],			#acceleration 
		[	"mars_kinda",
			float(6 * (10**26)),				#mass in kg
			[float(149597870700 * 0.1),float(0),float(0)], 	#location in metres, xyz
			[float(-25*10),float(60.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]				#acceleration m/s/s
		],			#acceleration 
		[	"mars_kinda",
			float(6 * (10**26)),				#mass in kg
			[float(149597870700 * 0.6),float(0),float(0)], 	#location in metres, xyz
			[float(-25*10),float(40.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]				#acceleration m/s/s
		],			#acceleration 
		[	"mars_kinda",
			float(6 * (10**26)),				#mass in kg
			[float(-149597870700 * 0.6),float(0),float(0)], 	#location in metres, xyz
			[float(35*100),float(-40.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]				#acceleration m/s/s
		],			#acceleration 
		[	"crazy",
			float(5.972 * (10**26)),				#mass in kg
			[float(149597870700*1.05),float(0),float(10000000)], 	#location in metres, xyz
			[float(0),float(15.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]
		],
        [	"crazy2",
			float(3 * (10**26)),				#mass in kg
			[float(-119597870700*.95),float(0),float(100000000)], 	#location in metres, xyz
			[float(0),float(-19.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]
		],
		[	"earth",
			float(5.972 * (10**24)),				#mass in kg
			[float(149597870700),float(0),float(10000000)], 	#location in metres, xyz
			[float(0),float(35.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]
		],
		[	"moon",
			float(7.3459 * (10**24)),				#mass in kg
			[float(149597870700),float(-0.3844*3 * (10 ** 10)),float(0)], 	#location in metres, xyz
			[float(1022/2),float(35.78*1000),float(0)],		#velocity in m/s
			[float(0),float(0),float(0)]
		]
	]			#acceleration 

#bodies = [
#		[	"sun",
#			float(1.98925 * 10**30),
#			[float(0),float(0),float(0)],
#			[float(0),float(-0.0894),float(0)],
#			[float(0),float(0),float(0)]
#		],
#		[	"mars_kinda",
#			float(6 * (10**26)),				#mass in kg
#			[float(149597870700 * 0.6),float(0),float(0)], 	#location in metres, xyz
#			[float(-25*10),float(40.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]				#acceleration m/s/s
#		],			#acceleration 
#		[	"mars_kinda",
#			float(6 * (10**26)),				#mass in kg
#			[float(-149597870700 * 0.6),float(0),float(0)], 	#location in metres, xyz
#			[float(35*100),float(-40.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]				#acceleration m/s/s
#		],			#acceleration 
#		[	"crazy",
#			float(5.972 * (10**26)),				#mass in kg
#			[float(149597870700*1.05),float(0),float(10000000)], 	#location in metres, xyz
#			[float(0),float(15.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]
#		],
 #       [	"crazy2",
	#		float(3 * (10**26)),				#mass in kg
	#		[float(-149597870700*.95),float(0),float(100000000)], 	#location in metres, xyz
	#		[float(0),float(-19.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]
#		],
#		[	"earth",
#			float(5.972 * (10**24)),				#mass in kg
#			[float(149597870700),float(0),float(10000000)], 	#location in metres, xyz
#			[float(0),float(29.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]
#		],
#		[	"moon",
#			float(7.3459 * (10**24)),				#mass in kg
#			[float(149597870700),float(-0.3844*3 * (10 ** 9)),float(0)], 	#location in metres, xyz
#			[float(1022/2),float(29.78*1000),float(0)],		#velocity in m/s
#			[float(0),float(0),float(0)]
#		]
#	]			#acceleration 

winx = 1000
winy = 1000
graphicObjects = []
win = GraphWin('solarsystem',winx,winy)
#sun = Circle(Point(100,20),25)
#sun.setFill('yellow')
#sun.draw(win)
graphicsInit()
years=10025.0
for i in range(0,int(years*365.25*24*3600/dt)):
	#system('clear')
	#print("Timestep: " + str(i) + ", dt=" + str(dt) + ", " + str(i*dt/(3600*24)) + " days elapsed")
	#printPositions()
	calculateAccel()
	calculateVel(dt)
	calculatePos(dt)
	updatePlot()
	
