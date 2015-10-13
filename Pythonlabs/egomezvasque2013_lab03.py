# Course: COP 4930  - Python Programming

# Term:   Fall 2015 - Dr. Clovis Tondo

# Author: Esteban Gomez (egomezvasque2013)
# Assignment #3 - "lab03.py"

# Due: September 9th, 2015



def start():
    print ("Welcome to Prime-list generator!\n")
    n = eval(input("What is your upper range? "))
    if ( 1 < n < 301):
        li = eratos(n) #li is receiving the value that eratos returns
        print_primes(li)
    else: 
        print ("Sorry, you need to enter a number greater than 2 and less than 300")
def eratos(n):
    li=[]
    for x in range (2, n+1):
        li.append(x) #adding our values to the list
    for x in li: #this for loop iterates through the list,
        for a in li: #this one looks for 
            if( a % x == 0 and a!=x):
                li.remove(a) #removes the numbers that are not prime
    return li

def print_primes(primes):
    n = len(primes)
    for i in range( 0, n ):
        print( "%5d" % primes[ i ], end = "" )
        if( (i + 1) % 10 ==0): #if we get to 10 chars, move to next line
            print( )
    
start() #
#python3 Python/my_assignments/egomezvasque2013_lab03.py
           
    
    