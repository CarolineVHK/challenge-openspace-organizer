#import the Classes made in the other Python files (table.py and openspace.py):
#table is not imported here, because it's already imported in openspace.py
from utils.openspace import Openspace
#import the module csv to be able to open, write and add information
import csv

#open the csv file and read the file
file = open('new_colleagues.csv') 
csvreader = csv.reader(file)
#create a new list to add the names from the files
names = []
for name in file:
    names.append(name.strip())


openspace = Openspace(names)
openspace.organize()
openspace.store('new_colleagues.csv')
openspace.display()