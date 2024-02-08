class Seat:
    '''This class is created to give a seat to a costumer.
    Afterwards to remove the costumer from a seat when you want to re-use the program.'''
    def __init__(self):
        self.free = True 
        self.occupant = None

    def set_occupant(self): # allows the program to assign someone a seat if it's free
        if self.free == True:
            self.occupant = self.name
            self.free = False
            return f'{self.name} is now seated'
        else:
            return f'Seat is already occupied by {self.occupant}'
    
    #remove someone from a seat and return the name of the person occupying the seat before
    #def remove_occupant(self): 
            #print(self.name, " is already seated here")


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

    #check for free seat in the list of seats created (True if a spot is available)
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free == True:
                return True
            else:
                return False
            
    #finding a free seat and place someone at that table
    def assign_seat(self): 
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(self.name)
                return f'{self.name} " is now seated'
            else:
                return "No free seats at this table!"   #how to go to a new table?
#!!! Go to a new table

    #returns how many places available (free) on a table
    def left_capacity(self): 
        count_free_seats = 4
        for seat in self.seats:
            if seat.free == False:
                count_free_seats -= 1
        print("There is/are ", count_free_seats, " seat(s) available.")

