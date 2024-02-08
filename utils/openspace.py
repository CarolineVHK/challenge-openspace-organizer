from table import Table

class Openspace:
    '''This is a class to create a room full of tables (here in example 6 tables), 
    afterwards assigne a person at an empty seat'''
    def __init__(self, names, number_of_tables: int=6):
        self.tables = []   #a list of Table
        self.number_of_tables = number_of_tables
        self.names = names
    
    #randomly assigning people to a seat in the different table.
    def organize(self):
        #iteration troughout names and tables: to see if table is available
        for name in self.names:
            for table in self.tables:
                if table.has_free_spot() == True:
                    table.assign_seat(self.name)
                    break
                
    #display the different tables and there occupants in a nice and readable way
    def display(self): 
        #Iterate throught each table in the list  of table and so with the index of each table
        for index_table, table in enumerate(self.tables, start = 1):
            return f'Table {index_table}: ' #gives the number of the table
            #iteration throught each seat from table
            for index_seat, seat in enumerate(table.seats, start=1):
                #check if seat is empty and display it
                if self.occupant == self.name:
                    if seat.free == False:
                        return f'Seat {index_seat}: '
                    else:
                        return "Empty"
            
    #store the repartition in an excel file
    def store(self, file): 
        self.file = file
        pass



