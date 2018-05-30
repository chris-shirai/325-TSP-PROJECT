# Oregon State CS 325 Final Project Spring 2018
# Created by B. Chris Loreta, Christopher Ragasa, Derek Yang
#
# Open file in command line with filename argument:
# Example: python algorithm.py tsp_example_1.txt

import sys
import math # for sqrt()

# Distance function takes two of a city argument: list containing ID and coords
def Distance(city1,city2):

	# get the exact distance in a decimal
	dist = math.sqrt((city1[1]-city2[1])**2 + (city1[2]-city2[2])**2)

	# round to nearest int
	nearestInt = int(round(dist))

	return nearestInt

# Output function lists the length first, then path.  Include .tour with f_name
def output_tour(arr,len,f_name):
	f_out = open(f_name,"w+")
	#writes length of walk in the first line
	f_out.write(len+"\n")
	#lists the walk
	for i in arr:
		f_out.write("%s\n" % i)
	f_out.close()

def Main():

	# open file through command line
	with open(sys.argv[1], 'r') as f:

		# split the lines into a list
		cities = f.read().splitlines()

		for line in range(len(cities)):

			cities[line] = list(map(int, cities[line].split()))
			

		# Now we have our info in cities[].
		# cities[line[0]]: City ID
		# cities[line[1]]: x-coord
		# cities[line[2]]: y-coord

		# test Distance function
		print(Distance(cities[1],cities[2])) #should print 1118
		

if __name__ == "__main__":
	Main()