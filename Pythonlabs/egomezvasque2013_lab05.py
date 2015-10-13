# Course: COP 4930  - Python Programming

# Term:   Fall 2015 - Dr. Clovis Tondo

# Author: Esteban Gomez (egomezvasque2013)
# Assignment #5- "lab05.py"

# Due: September 30th, 2015
myDict={"\\A": "author", "\\B": "book", "\\J": "journal", "\\R": "article", "\\P": "publisher", "\\Y": "year" } #hardcoded keys that we need

def main():
    myfile=open("bib.txt","r")
    for line in myfile:
        line=line.lstrip(' \t') #this strips spaces and tabs that we don't need
        if line.find("\\bibitem") != -1: #find() method returns a -1 if substring isn't found
			#line.split()
            print("<doi>")
        elif len(line.strip()) == 0: #finding a blankline
            
            print("</doi>")
        else:
            commands(line)#commands strips ,. and '' and prints the final output
    myfile.close()
    
def commands(line):
    
    key = line[0:2] #we use slice to cut out the key from the line
    value = line[2:] #strings in python are immutable!
    newValue = value.rstrip(".,\n ") #stripping out extra commas and periods
    if key in myDict:
        output = "<" + myDict[key] + ">" + newValue + "</" + myDict[key] + ">"
        print(output)
    else: #if an invalid command is entered
        print("+++ unknown: " + line.strip("\n"))
main()