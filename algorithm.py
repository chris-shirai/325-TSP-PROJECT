# Oregon State CS 325 Final Project Spring 2018
# Created by B. Chris Loreta, Christopher Ragasa, Derek Yang
#
# Open file in command line with filename argument:
# Example: python algorithm.py tsp_example_1.txt

import sys
import math # for sqrt()
from copy import deepcopy

### FOR TESTING PURPOSES
import time 
start_time = time.time()
### END TESTING

# Distance function takes two of a city argument: list containing ID and coords
def Distance(city1,city2, distMemos):
    
    # get the exact distance in a decimal
    dist = math.sqrt((city1[1]-city2[1])**2 + (city1[2]-city2[2])**2)

    # round to nearest int
    nearestInt = int(round(dist))

    distMemos[city1[0]][city2[0]] = nearestInt
    distMemos[city2[0]][city1[0]] = nearestInt

    return nearestInt

# Output function lists the length first, then path.  Include .tour with f_name
def output_tour(arr,len,f_name):
    f_out = open(f_name,"w+")
    #writes length of walk in the first line
    f_out.write(str(len)+"\n")
    #lists the walk
    for i in arr:
        f_out.write("%s\n" % i[0])
    f_out.close()

# This function takes a route with the starting vertex of 2 edges
# and returns a modified array with the routes swapped
def improve2opt(route,i,k):
    new_route = []
    new_route.extend(route[:i])
    new_route.extend(reversed(route[i:k+1]))
    new_route.extend(route[k+1:])

    return new_route

# calculates the total distance of a route
def calcTotalDist(route, distMemos):
    var = 0
    for line in range(len(route)):
        if line == 0:
            # distance from last vertex to 0
            var += Distance(route[0],route[len(route)-1], distMemos)
        else:
            # distance from previous vertex to this
            var += Distance(route[line-1],route[line], distMemos)
    return var

#limits the rate to 3 minutes if the number of cities is < 5050
def rate_limit(len_c):
    if len_c > 5050:
        return 1200.00
    else:
        return 179.95

def Main():
    # open file through command line
    with open(sys.argv[1], 'r') as f:

        # split the lines into a list
        cities = f.read().splitlines()

        for line in range(len(cities)):
            # split the line into separate elements
            cities[line] = list(map(int, cities[line].split()))

        # Now we have our info in cities[].
        # cities[line[0]]: City ID
        # cities[line[1]]: x-coord
        # cities[line[2]]: y-coord
        distMemos = [[None for x in range(len(cities))] for y in range(len(cities))]

        # get the initial total distance
        totalDist = calcTotalDist(cities, distMemos)
        #rate limiter
        rate = rate_limit(len(cities))
        # create a memos list
        distMemos = [[None for x in range(len(cities))] for y in range(len(cities))]

        timeRemaining = True

        # if an entire loop completes without an improvement,
        # currLoopImprov finishes True; end program.
        currLoopImprov = False

        while 1 and timeRemaining and not currLoopImprov:
            loopStart=1

            currLoopImprov = True

            improvement = True
            timeRemaining = True

            while timeRemaining and improvement:

                improvement = False

                for i in range(loopStart, len(cities)-1):
                    for k in range(i+1, len(cities)):

                        if distMemos[cities[i-1][0]][cities[i][0]] == None:
                            currD1 = Distance(cities[i-1],cities[i], distMemos)
                        else:
                            currD1 = distMemos[cities[i-1][0]][cities[i][0]]

                        if distMemos[cities[i-1][0]][cities[k][0]] == None:
                            newD1 = Distance(cities[i-1],cities[k], distMemos)
                        else:
                            newD1 = distMemos[cities[i-1][0]][cities[k][0]]


                        if k == len(cities)-1:
                            if distMemos[cities[k][0]][cities[0][0]] == None:
                                currD2 = Distance(cities[k],cities[0], distMemos)
                            else:
                                currD2 = distMemos[cities[k][0]][cities[0][0]]
                        else:
                            if distMemos[cities[k][0]][cities[k+1][0]] == None:
                                currD2 = Distance(cities[k],cities[k+1], distMemos)
                            else:
                                currD2 = distMemos[cities[k][0]][cities[k+1][0]]

                        if k == len(cities)-1:
                            if distMemos[cities[i][0]][cities[0][0]] == None:
                                newD2 = Distance(cities[i],cities[0], distMemos)
                            else:
                                newD2 = distMemos[cities[i][0]][cities[0][0]]
                        else:
                            if distMemos[cities[i][0]][cities[k+1][0]] == None:
                                newD2 = Distance(cities[i],cities[k+1], distMemos)
                            else:
                                newD2 = distMemos[cities[i][0]][cities[k+1][0]]
                        
                        totalCurrD = currD1 + currD2
                        totalNewD = newD1 + newD2

                        # check if swap is an improvement
                        if totalNewD < totalCurrD: # - difference:

                            # create a new route with 2-opt switch
                            newRoute = improve2opt(cities,i,k)

                            # save the distance and new routes
                            totalDist = totalDist + totalNewD - totalCurrD
                            cities = newRoute

                            # we need to loop again
                            improvement = True

                            # after exiting loop, resume at i
                            loopStart=i

                            currLoopImprov = False

                            ### FOR TESTING PURPOSES
                            print(str(totalDist) + " " + str((time.time() - start_time)) + " improvement: i=" + str(i) + " , k=" + str(k))

                            if (time.time() - start_time) > rate:
                                timeRemaining = False
                            break # exit up the chain to repeat the loop

                        if (time.time() - start_time) > rate:
                            timeRemaining = False
                            break
                        k += 1
                    if improvement:
                        break # exit up the chain to repeat the loop
                    
                    i += 1

    ### FOR TESTING PURPOSES
    print
    print("Total runtime:")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Distance: " + str(totalDist))
    ### END TESTING

    output_tour(cities,totalDist,sys.argv[1] + ".tour")


if __name__ == "__main__":
    Main()
