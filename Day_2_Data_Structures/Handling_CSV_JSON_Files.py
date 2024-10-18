import csv  # importing the csv module.
import json

# csv file path
filename = "raffle_mailings_sample_data.csv"
# opening the csvfile in traditional way
csvfile = open(filename, 'r')

# initializing the titles and rows list
fields = []
rows = []

# reading CSV file
# creating a CSV reader object
csvreader = csv.reader(csvfile)
# this object is our go-to for every change in the
# we will just interact with it.
# csvreader is an iterator it has the data in the form of rows
# a next is called on it, then it goes to the next row.
# so the first row will have fields, and correspondingly we can
# go for next.

# extracting field names through first row
fields = next(csvreader)
# next function returns the current row and
# advances the row to the next.


# extracting each data row one by one
# in for loop next is automatically called for
# an iterator.
for row in csvreader:
    rows.append(row)

# get total number of rows
print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print(col, end=" ")
    print('\n')

## writing a csv file
import csv
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "student_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

## JSON Files
import json

data = {
    "Subjects": {
        "Maths": 85,
        "Physics": 90
    }
}

jsonFile = open("example.json", 'w')
json.dump(data, jsonFile)

