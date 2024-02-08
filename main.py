#import the Classes made in the othe Python files:
from utils.table import Table
from utils.openspace import Openspace
import csv
#open the csv file and read the file
file = open('new_colleagues.csv') 
csvreader = csv.reader(file)
#create a new list to add the names from the files
names = []
for name in file:
    names.append(name.strip())
print("List of names from the CSV: ",names)

openspace = Openspace(names)
openspace.organize()
openspace.display()
openspace.store("new_colleagues.csv")