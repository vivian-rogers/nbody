//VIV MADE THIS
//WELCOME TO THE VIV ZONE
//RUN WITH ./nbody [timestep in hours] [number of years to run]

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>



#define maxBodies 20
#define au 149597870700			//astronomical units in metres
#define gc 6.67384e-11 			//gravitational constant in N*m^2/kg^2


typedef struct body { // declares the attributes of a body
	char name[20];
	double mass;
	double pos[3];
	double vel[3];
	double acc[3];
	int color;
} body;

int currentBodies = maxBodies;			//initializes the current number of bodies to the max 

body *solarSystem[maxBodies];			//array of pointers to bodies


void initSystem(body *solarSystem[],const body _initBodies[]);
void freeMem(body *solarSystem[]);
void calculateAccel(body* solarSystem[]);
void calculateVel(body* solarSystem[], int dt);
void calculatePos(body* solarSystem[], int dt);
double norm(double* pointA);
//double * vectorSubtract(double *pointA, double *pointB);
void vectorSubtract(double * result, double *pointA, double *pointB);
int addObject(char* _name, double _mass, double _pos0, double _pos1, double _pos2, double _vel0, double _vel1, double _vel2, int _color); 
void printBodies(body* solarSystem[], int dt, int timestep);


const body initBodies[] = {			//just some test bodies
	{"sun", 1.985e+30, {0,0,0}, {0,-0.0894,0}, {0,0,0}, 0xFFFF0000},
	{"earth", 5.972e24, {149597870700,0,0}, {0,29.78*1000,0}, {0,0,0}, 0x0000FFFF},
	{"moon", 7.3459e22, {149597870700,-0.3844e9,0}, {1022,29.78*1000,0}, {0,0,0}, 0x88888888}
};


void initSystem(body *solarSystem[],const body _initBodies[]){		//fills up solarsystem with the bodies defined in initBodies
	currentBodies = sizeof(initBodies) / sizeof(initBodies[0]);	//i love C this is great
	if(currentBodies > maxBodies){
		printf("it broken you need to increase maxbodies\n");
	}
	for(int i = 0; i < currentBodies; i++){
		body* temp = (body *) malloc(sizeof(body));
		solarSystem[i] = temp;
		*solarSystem[i] = initBodies[i];
	}
}

void freeMem(body* solarSystem[]){	//when we are done, it is good to give resources back to the machine
	for(int i = 0; i < currentBodies; i++){
		free(solarSystem[i]);
	}
}

void calculateAccel(body* solarSystem[]){	//given the solar system of bodies, it will calculate the forces and accelerations of all bodies from each other
	for(int i = 0; i < currentBodies; i++){	
		double pointA[3];
		for(int dim = 0; dim < 3; dim++){		//defines the origin point
			pointA[dim] = solarSystem[i]->pos[dim];
		}
		for(int j = 0; j < currentBodies; j++){
			if(i != j){
				double radius;
				double distVect[3];
				double pointB[3];	//defines secondary point
				for(int dim = 0; dim < 3; dim++){
					pointB[dim] = solarSystem[j]->pos[dim];
				}
				vectorSubtract(&distVect[0],&pointA[0],&pointB[0]);
				radius = norm(&distVect[0]);
				for(int dim = 0; dim < 3; dim++){		//calculates force from F_g = - Gc*m1*m2/r^2 * r_hat
					solarSystem[i]->acc[dim] -= distVect[dim] * (solarSystem[i]->mass) * (solarSystem[j]->mass) * gc / pow(radius,3);
				}
			}
		}
		for(int dim = 0; dim < 3; dim++){	//calculates accel from a = Sigma(F) / m
			solarSystem[i]->acc[dim] = solarSystem[i]->acc[dim] / solarSystem[i]->mass;
		}
	}
}

void calculateVel(body* solarSystem[], int dt){		//integrates velocities of all bodies, v = a*dt + v_0
	for(int i = 0; i < currentBodies; i++){
		for(int dim = 0; dim < 3; dim++){
			solarSystem[i]->vel[dim] += solarSystem[i]->acc[dim] * dt;
		}
	}
}

void calculatePos(body* solarSystem[], int dt){ 	//integrates positions of all bodies, r = v*dt + r_0
	for(int i = 0; i < currentBodies; i++){
		for(int dim = 0; dim < 3; dim++){
			solarSystem[i]->pos[dim] += solarSystem[i]->vel[dim] * dt;
		}
	}
}

double norm(double* pointA){ //takes sqrt(x^2 + y^2 + z^2) of a given vector pointer
	double sum = 0;
	for(int dim = 0; dim < 3; dim++){
		sum += (*(pointA + dim)) * (*(pointA + dim));
	}
	return pow(sum,0.5);
}
void vectorSubtract(double * result, double *pointA, double *pointB){ // given two points to double arrays, will subtract them element wise and return a vector to a new 3-array
	//double* temp = (double *) malloc(3*sizeof(double));	
	for(int dim = 0; dim < 3; dim++){
		*(result + dim) = *(pointA + dim) - *(pointB + dim);
	}
	return;
}

int addObject(char* _name, double _mass, double _pos0, double _pos1, double _pos2, double _vel0, double _vel1, double _vel2, int _color){ // call to add a body to the list 
	if(currentBodies >= maxBodies){
		return 0; //you have too many bodies!!! increase maxbodies
	}	
	body* temp = (body *) malloc(sizeof(body));
	strcpy(temp->name,_name);
	//strcpy(temp->color[],_color[]);
	temp->pos[0] = _pos0;
	temp->pos[1] = _pos1;
	temp->pos[2] = _pos2;
	temp->vel[0] = _vel0;
	temp->vel[1] = _vel1;
	temp->vel[2] = _vel2;
	temp->acc[0] = 0;
	temp->acc[1] = 0;
	temp->acc[2] = 0;
	temp->color = _color;
	solarSystem[currentBodies] = temp;
	currentBodies++;
	return 1; //awesome good job it succeeded
}

int delObject(int index){	//call to remove an object of known index
	body* temp = solarSystem[currentBodies];
	solarSystem[currentBodies] = solarSystem[index];
	free(solarSystem[index]);
	solarSystem[index] = temp;
	
}

void printBodies(body* solarSystem[], int dt, int timestep){ // prints the coordinates and parameters of the bodies that are moving around
	//system("clear"); 
	printf("Timestep %i, day = %f, dt = %i\n", timestep, (float) timestep*dt/(3600*24), dt);
	for(int i = 0; i < currentBodies; i++){
		//printf(i[0] + ":	"" mass: " + str(i[1]) + "kg,	coords: (", end = '')
		printf("body %i: '%s'\t mass = %e kg, coords = {%f, %f, %f} (a.u.)\n", i, solarSystem[i]->name, solarSystem[i]->mass, solarSystem[i]->pos[0]/au, solarSystem[i]->pos[1]/au, solarSystem[i]->pos[2]/au);
	}
	printf("\n");
}


int main(int argc, char *argv[]) { //sets up and drives motion of the planets

	int dt;
	float years;
	if(argc <= 2){
		printf("please run with './nbody [timestep size in hours] [number of years to run]'\n");
		return 0;
	}
	dt = atof(argv[1]) * 3600;	//so pass argv[1] in timesteps of hours, dt is in units of seconds
	years = atof(argv[2]);
	initSystem(solarSystem,initBodies);
  	for(int i = 0; i < years*365.25*24*3600/dt; i++){
		calculateAccel(solarSystem);
		calculateVel(solarSystem,dt);
		calculatePos(solarSystem,dt);
		//printBodies(solarSystem,dt,i);
		//if(addflag){
		//}
	}
	freeMem(solarSystem);
  	printf("Done!\n");
	return 1;
}






