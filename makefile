# target: dependencies
# <tab> rule

# make (without arguments) executes first rule in file
# Ideally, one target for every object file and a target for final binary. 

nbody: nbody_driver.c
	gcc -o nbody nbody_driver.c -lm
#	c99 -o nbody nbody_driver.o
#
#nbody_driver.o: nbody_driver.c
#	c99 -c nbody_driver.c -lm






