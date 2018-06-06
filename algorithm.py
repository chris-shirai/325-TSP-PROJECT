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
def calcTotalDist(route):
    var = 0
    for line in range(len(route)):
        if line == 0:
            # distance from last vertex to 0
            var += Distance(route[0],route[len(route)-1])
        else:
            # distance from previous vertex to this
            var += Distance(route[line-1],route[line])
    return var


def nearest_neighbor(arr):
    tmp_city = deepcopy(arr) #copy of the original cities list
    nn_path = [] #append the near neighbor path to empty list, return it
    cities_length = len(arr) #of cities
    #DELETE TO SEE DIST tmp_nearest_dist_arr = []
    for i in range(cities_length):
        print(i)
        curr_city = tmp_city.pop(0) #takes current city aka visited
        nn_path.append(curr_city)
        nearest_dist = sys.maxsize
        #nearest_city = None #our cities[element][element] essentialy, the city itself
        #checks distance from current city to unvisited cities
        for j in range(len(tmp_city)):
            k = 0
            tmp_nearest_dist = Distance(curr_city,tmp_city[j])
            if nearest_dist > tmp_nearest_dist: #compares which city is the smallest from your current city
                nearest_dist = tmp_nearest_dist
                nearest_city = tmp_city[j]
                k = j
                #print(nearest_city)

        # guard against retrieving nonexistent array items
        if i != cities_length-1:
            #swap array items
            tmp_arr_pos = tmp_city[0]
            tmp_city[0] = tmp_city[k]
            tmp_city[k] = tmp_arr_pos
        #DELETE TO SEE DIST tmp_nearest_dist_arr.append(tmp_nearest_dist)
        #DELETE TO SEE DIST print("nearest dist arr")
        #DELETE TO SEE DIST print(tmp_nearest_dist_arr)
    return nn_path


def two_opt(c_arr,totalDist_in):
    improvement = True
    while improvement:

        # initialize to false
        improvement = False

        for i in range(1, len(c_arr) - 1):
            for k in range(i + 1, len(c_arr)):

                currD1 = Distance(c_arr[i - 1], c_arr[i])
                newD1 = Distance(c_arr[i - 1], c_arr[k])

                if k == len(c_arr) - 1:
                    currD2 = Distance(c_arr[k], c_arr[0])
                    newD2 = Distance(c_arr[i], c_arr[0])
                else:
                    currD2 = Distance(c_arr[k], c_arr[k + 1])
                    newD2 = Distance(c_arr[i], c_arr[k + 1])

                totalCurrD = currD1 + currD2
                totalNewD = newD1 + newD2

                # check if swap is an improvement
                if totalNewD < totalCurrD:
                    # create a new route with 2-opt switch
                    newRoute = improve2opt(c_arr, i, k)

                    # calculate distance of new route
                    newDist = calcTotalDist(newRoute)

                    # save the distance and new routes
                    totalDist_in[0] = newDist
                    c_arr = newRoute

                    # we need to loop again
                    improvement = True

                    ### FOR TESTING PURPOSES
                    print(str(totalDist_in[0]) + " improvement: i=" + str(i) + " , k=" + str(k))

                    break  # exit up the chain to repeat the loop

                k += 1
            if improvement:
                break  # exit up the chain to repeat the loop

            i += 1
    return c_arr


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

        # get the initial total distance
        totalDist = [0]
        totalDist[0] = calcTotalDist(cities)
 
        test_nearest = nearest_neighbor(cities)
        cities = test_nearest

        ### FOR TESTING PURPOSES
        print("Greedy algorithm complete.")
        print("Distance: " + str(totalDist[0]))
        print("--- %s seconds ---" % (time.time() - start_time))
        print
        ### END TESTING


        #2opt function
        cities = two_opt(cities,totalDist)

    ### FOR TESTING PURPOSES
    print
    print("Total runtime:")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Distance: " + str(totalDist[0]))
    ### END TESTING

    output_tour(cities,totalDist[0],sys.argv[1] + ".tour")


if __name__ == "__main__":
    Main()