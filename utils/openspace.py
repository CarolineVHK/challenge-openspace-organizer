#adding the selfmademodule table.py because we need the Class Table in that file
from .table import Table
#adding the module csv to be able to acces the functions to store the data back into the file
import csv

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
                
    #store the repartition in an excel file
    def store(self,filename):
        file = open(filename,"a",newline="")
        writer = csv.writer(file)
        for table_index, table in enumerate(self.tables, start=1):
            for seat in table.seats:
                if seat.free == False:
                    writer.writerow([seat.occupant, table_index])
    
    #display the different tables and there occupants in a nice and readable way
    def display(self): 
        print("Displaying table organization:")
        #Iterate throught each table in the list  of table and so with the index of each table
        for index_table, table in enumerate(self.tables, start = 1):
            table_info = f'Table {index_table}: ' #gives the number of the table
            #iteration throught each seat from table
            for index_seat, seat in enumerate(table.seats, start=1):
                #check if seat is empty and display it
                if self.occupant == self.name:
                    if seat.free == False:
                        table_info += f'Seat {index_seat}: {self.seat_occupant}\n'
                    else:
                        table_info += f'Seat {index_seat}: Empty\n'
            print(table_info)
            
