# Course: COP 4930  - Python Programming

# Term:   Fall 2015 - Dr. Clovis Tondo

# Author: Esteban Gomez (egomezvasque2013)
# Assignment #6- "lab06.py"

# Due: October 7th, 2015
class Node :

    def __init__( self, data = None, next_node = None ) :
        self.data = data
        self.next_node = next_node

    def get_data( self ) :
        return self.data

    def get_next( self ) :
        return self.next_node

    def set_next( self, new_next ) :
        self.next_node = new_next


class List :

    def __init__( self, head = None ) :
        self.head = head

    def insert( self, data ) :                          #three main cases, when inserting when the llist is empty,
        print("insert( '" + data.strip() + "')" + "\n") #when the element comes before and when the element comes after
        new_node = Node( data.strip() )                 #if it comes after we need the after pointer to join the 'self' node

        if (self.head is None):
            new_node.set_next(self.head)
            self.head = new_node
        else:
            if (data < self.head.get_data()):
                new_node.set_next(self.head)
                self.head = new_node
            else:
                cur = self.head
                while cur.get_next() != None:
                    if (new_node.get_data() < cur.get_next().get_data()):  #current node is less than next nodes data  => CHAINING
                        after = cur.get_next()
                        cur.set_next(new_node)   # sets next = new_node
                        new_node.set_next(after) # sets new nodes next to after "see pic"
                        break
                    cur = cur.get_next()
                if (cur.get_next() is None):
                    cur.set_next( new_node)

    def printList( self ) :
        print("print( )")
        cur = self.head
        while (cur) :
            print(str(id(cur)) + "  " + cur.get_data( ) + " " + str(id(cur.get_next( ))))
            cur = cur.get_next( )
            if cur == None:
                print()

    def remove(self, data):
        print("remove('{}')\n".format(data))
        cur = self.head
        if data == cur.get_data():
            self.head = cur.get_next()
            cur = None
        else:
            while cur.get_next() and data != cur.get_next().get_data(): #while there is a next element and our self isn't = to the next obj, data
                cur = cur.get_next()
            if cur.get_next():
                to_del = cur.get_next()
                after = to_del.get_next()
                cur.set_next(after)
                to_del = None
            else:
                return False  # NO SUCH ELEMENT IS FOUND
        return True

def main( ) :
    ifile=open("llist.txt","r")
    myList = List()
    for line in ifile:
        line = line.strip()
        command = line[0:1] #slice it to get our commands
        if (command == 'i') :
            myList.insert(line[2:])
        elif (command == 'p') :
            myList.printList()
        elif(command == 'r') :
            myList.remove(line[2:])
    ifile.close()

main( )