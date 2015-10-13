# Course: COP 4930  - Python Programming

# Term:   Fall 2015 - Dr. Clovis Tondo

# Author: Esteban Gomez (egomezvasque2013)
# Assignment #4- "lab04.py"

# Due: September 16th, 2015

dict = { }

def make_dict( ) :
    ifile = open( "fl_cities.txt", "r" )

    for line in ifile :
        line = line.rstrip( )
        ( v, k ) = line.split( ":" )
        dict[ k ] = v

    ifile.close( )
    test_dict( )

def test_dict( ):
    myfile = open( "fl_maint.txt", "r" )
    for word in myfile :
        word = word.rstrip()
        (lttr, value) = word.split('-')
        print()
        print(lttr)
        if lttr == 'p':
            new = list(dict.keys())
            new.sort()
            for x in new:
                print( "%-20s\t%-20s" % ( x, dict[x] ) )
        elif lttr == 'f':
            if value in dict:
                
                print("%-20s\t%-20s" % (value, dict[value]))
            else:
                print("city unknown")
        elif lttr == 'c':               
            (part1, part2 ) = value.split(':')
            if part2 in dict:
                dict[part2] = part1
                print ("%-20s\t%-20s" % (part2, dict[part2]))
            elif part1 not in dict:
                print(part2, "city unknown")
               
        else:
             print("Unknown command")
    
        #print( value)
    myfile.close( )
                  

make_dict( )
