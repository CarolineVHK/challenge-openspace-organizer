list = [["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]

list [0][0] = "name"

print(list)

class Seat:
    '''This class is created to give a seat to a costumer.
    Afterwards to remove the costumer from a seat when you want to re-use the program.'''
    def __init__(self):
        self.free = True 
        self.occupant = None

    def set_occupant(self, name): # allows the program to assign someone a seat if it's free
        #self.name = name
        if self.free == True:
            self.occupant = name
            self.free = False
            #return f'{self.name} " is now seated'
        #else: 
            #Seat.remove_occupant()
    
    #def remove_occupant(self): #remove someone from a seat and return the name of the person occupying the seat before
            #print(self.name, " is already seated here")
# some_seat = Seat()
# some_seat.set_occupant('Gerrit')
some_seat = Seat()
print(some_seat.free)
print(some_seat.occupant)
some_seat.set_occupant('Caro')
print(some_seat.free)
print(some_seat.occupant)

class Table:
    '''this class is created to see if a seat is taken or not and to see if there is any seats left on 
    the table to place a costumer'''
    def __init__(self, capacity: int=4):
        self.capacity = capacity
        self.seats= [] #list of Seats 
        #create a seat
        for _ in range(capacity):
            self.seats.append(Seat())
            print(self.seats)

    def has_free_spot(self): #returns a boolean (True if a spot is available)
        #check for free seat in the list of seats created
        for seat in self.seats:
            if seat.free ==True:
                return True
            else:
                return False

    def assign_seat(self): #that places someone at the table
        #finding a free seat and place someone into it
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(self.name)
                return f'{self.name} " is now seated'
            else:
                return "No free seats at this table!"   #how to go to a new table?
#!!! Go to a new table

    def left_capacity(self): #returns how many places left (per table?)
        #returns available seats on table
        count_free_seats=4
        for seat in self.seats:
            if seat.free == False:
                count_free_seats-=1
        print("There is/are ",count_free_seats, "seat(s) available.")



#me= Seat("Caroline")
#me.set_occupant("")
#print(me.set_occupant)

some_table_obj = Table()
print(some_table_obj.seats)
print(some_table_obj.capacity)
for seat in some_table_obj.seats:
    print(seat.free)
    seat.set_occupant('Gerrit')

some_table_obj = Table(capacity=4)
some_table_obj.capacity
some_table_obj.has_free_spot()
some_table_obj
