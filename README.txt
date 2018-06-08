Oregon State CS 325 Final Project Spring 2018
Created by B. Chris Loreta, Christopher Ragasa, Derek Yang

To run this program, open file in command line with filename argument.
Example: python algorithm.py tsp_example_1.txt

-----------------

    The text input file must be formatted as follows:

    - Each line defines a city and each line has three numbers separated 
by white space.
    - The first number is the city identifier
    - The second number is the city’s x-coordinate 
    - The third number is the city’s y-coordinate.

For example:

0 438  75
1 381  53
2 765 530
3 795 779

etc.

-----------------

    The text output file created by the program will have the same name as
the input file, with .tour appended to the end. For example, if 
the input file was "inputfile.txt", the program will produce an 
output file named "inputfile.txt.tour".

    The output file will be formatted as follows:

    - The file contains n+1 lines, where n is the number of cities.
    - The first line is the length of the tour the program computes.
    - The next n lines contain the city identifiers in the order they
are visited by the tour.
    - Each city is listed exactly once in this list.
