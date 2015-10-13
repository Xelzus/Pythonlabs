# Course: COP 4930  - Python Programming

# Term:   Fall 2015 - Dr. Clovis Tondo

# Author: Esteban Gomez (egomezvasque2013)
# Assignment #2 - "lab02.py"

# Due: September 2nd, 2015

def main():
    fib = [0, 1 ]
    print ( "Welcome to Fibonacci generator!", "\n" ) 
    n = eval( input( "How many numbers should I generate? " ) )
    first = fib[ 0 ]
    second = fib [ 1 ]
    if (n == 1):
        print(fib[0])
    elif (n == 0):
        return
    else:
        n-=2;
        while ( n!= 0) : 
            nextn= first+ second
            fib.append( nextn ) 
            first = second
            second = nextn
            n-=1; 
        print ("\t".join(map(str, fib[ :6]))) 
        print ("\t".join(map(str, fib[6:12]))) #prints 7th to 12th
        print ("\t".join(map(str, fib[12:18]))) #we apply map to each elm in fib to make them a string, that way we can use join while applying tab to display the list w/out brackets.
        print ("\t".join(map(str, fib[18:])))
main()
        
#python3 Python/egomezvasque2013_lab02.py