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

def improve2opt(route,i,k):
    new_route = []
    new_route.extend(route[:i])
    new_route.extend(reversed(route[i:k+1]))
    new_route.extend(route[k+1:])

    return new_route

def calcTotalDist(route):
    var = 0
    for line in range(len(route)):
        if line == 0:
            var += Distance(route[0],route[len(route)-1])
        else:
            var += Distance(route[line-1],route[line])
    return var



def Main():
    # open file through command line
    with open(sys.argv[1], 'r') as f:

        # split the lines into a list
        cities = f.read().splitlines()

        for line in range(len(cities)):

            cities[line] = list(map(int, cities[line].split()))
            print(cities[line])

    
        # Now we have our info in cities[].
        # cities[line[0]]: City ID
        # cities[line[1]]: x-coord
        # cities[line[2]]: y-coord

        totalDist = calcTotalDist(cities)
        #print(totalDist)

        #bestDist = totalDist
        improvement = True
        while improvement:
            print(totalDist)
            improvement = False
            for i in range(1, len(cities)-1):
                for k in range(i+1, len(cities)):
                    newRoute = improve2opt(cities,i,k)
                    #print(newRoute)
                    newDist = calcTotalDist(newRoute)
                    if newDist < totalDist:
                        totalDist = newDist
                        cities = newRoute
                        improvement = True
                        print("Found improvement. i=" + str(i) + " , k=" + str(k))
                        break
                    #print("increasing k")
                    k += 1
                if improvement:
                    break
                #print("increasing i")
                i += 1




        # Note: the distance of each city is the distance to get to the next city.

        # test Distance function
        # print(Distance(cities[1],cities[2])) #should print 1118

if __name__ == "__main__":
    Main()