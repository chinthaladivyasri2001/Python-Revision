
# README: Python File Handling

## Introduction
File handling in Python is a powerful and versatile tool that allows users to perform a wide range of operations on files. Python provides an easy and efficient way to read, write, and manipulate files, making it accessible for both beginners and experienced programmers.

## Key Concepts
- **Text vs. Binary**: Python treats files differently based on their type.
- **End of Line (EOL)**: Each line of a text file is terminated by a special character (e.g., newline).

## Advantages of File Handling in Python
- **Versatility**: Perform various operations (creating, reading, writing, appending, renaming, deleting).
- **Flexibility**: Supports different file types (text, binary, CSV) and operations.
- **User-Friendly**: Straightforward interface for file operations.
- **Cross-Platform**: Compatible with Windows, Mac, and Linux.

## Disadvantages of File Handling in Python
- **Error-Prone**: Susceptible to errors if not carefully coded or if file system issues arise (e.g., permissions).
- **Security Risks**: User input can compromise sensitive files.
- **Complexity**: Advanced file formats may complicate operations.
- **Performance**: File operations may be slower than in other languages, especially with large files.

## File Operations
To perform operations on a file, it must first be opened using Python's built-in `open()` function. The mode of the file must be specified to indicate the purpose of opening it.

```python
f = open(filename, mode)
```

### Supported Modes
- **`r`**: Open an existing file for reading.
- **`w`**: Open an existing file for writing (overrides existing data or creates a new file).
- **`a`**: Open an existing file for appending (adds data without overriding).
- **`r+`**: Open a file for reading and writing (modifies data starting from the beginning).
- **`w+`**: Open a file for writing and reading (overrides existing data or creates a new file).
- **`a+`**: Open a file for appending and reading (adds data without overriding).

### Writing to a File
- Creating and Opening a File: To write data to a file, you first need to create it or open an existing one. Use the open() function, specifying the mode in which to open the file.

- Mode 'w': Opens a file for writing. If the file already exists, it truncates (clears) the file to zero length; if it does not exist, it creates a new file.
- Using Context Managers: It’s a good practice to use a with statement when opening a file. This ensures that the file is properly closed after its suite finishes, even if an error occurs.

- Writing Data: You can write strings to the file using the write() method. To write multiple lines, you can use the writelines() method, which takes a list of strings as an argument.

### Reading from a File
- Opening a File for Reading: To read data from a file, you need to open it in read mode ('r').

- Reading Methods:

- * read(): Reads the entire content of the file as a single string. You can also specify the number of characters to read.
- * readline(): Reads the next line from the file. This method is useful when you want to process the file line by line.
- * readlines(): Reads all lines from the file and returns them as a list of strings. Each line in the file becomes an element in the list.

### File Closure
- Closing the File: It’s essential to close the file after finishing your operations. Closing a file releases the system resources associated with it. You can use the close() method for this purpose, or simply rely on the context manager (with statement) to handle it automatically.
## Conclusion
Python's file handling capabilities are essential for managing data effectively in various applications. Understanding the advantages, disadvantages, and operations ensures secure, reliable, and efficient code.

#  HANDLING CSV AND JSON Files
- The CSV (Comma Separated Values) file format is a simple way to save tabular data in spreadsheets and databases.
- plain text file with tabular data (numbers and text). Each line in the file represents a data record. There are one or more fields in each entry separated by commas. Using a comma as a field separator gives this file format its name.
- JSON stands for JavaScript Object Notation in its entire form. The data is stored and transferred using a script (executable) file written in a computer language. In JSON, the text is represented as a quoted string containing the value in a key-value mapping.- There is an inbuilt module in Python that is used to specially handle CSV files in Python, the module is CSV
## Handling csv files
- There is an inbuilt module in Python that is used to specially handle CSV files in Python, the module is CSV

Working with CSV Files in Python

This script demonstrates how to read from and write to CSV files using Python's built-in csv module.

Reading a CSV File
1. The script starts by importing the csv module.
   ```python
   import csv
   ```
2. We specify the file path of the CSV file (raffle_mailings_sample_data.csv) and open it in read mode.
   ```python
   csvfile = open(filename, 'r')
   ```
3. A csv.reader object is created to iterate over the rows.
   ```python
   csvreader = csv.reader(csvfile)
   ```
4. The first row (headers) is extracted using the next() function and stored in fields.
   ```python
   fields = next(csvreader)
   ```
5. Each subsequent row is appended to the rows list using a loop.
   ```python
   for row in csvreader:
       rows.append(row)
   ```
6. The script prints the total number of rows, field names, and the first five rows of data.

Writing to a CSV File
1. The csv.writer is used to write new data into a CSV file (student_records.csv).
2. Field names are defined as a list, and rows are added as a list of lists.
   ```python
   fields = ['Name', 'Branch', 'Year', 'CGPA']
   rows = [['Nikhil', 'COE', '2', '9.0'], ... ]
   ```
3. The script writes field names and data rows to the CSV file using csvwriter.writerow() and csvwriter.writerows().

This is a simple and efficient way to handle CSV data in Python.

## Handling JSON Files
- we have a JSON module that can handle all things related to file handing in JSON. 
- If we closely look at the JSON format, it just looks like a list of dictionaries. The difference is in JSON; it's a string of text, so we need to convert our python objects to text before writing to a file and those functionalities are offered by json library. 
- JSON not only supports dictionaries but also various otter primitive data types like list, tuples, str, int, long, float and boolean values.

# Writing Data to JSON in Python

### Importing the json module:
```python
import json
```
The json module is imported to handle the JSON (JavaScript Object Notation) operations like dumping and loading data.

### Defining a dictionary (data):
```python
data = {
    "Subjects": {
        "Maths": 85,
        "Physics": 90
    }
}
```
A Python dictionary named `data` is created, which contains nested key-value pairs. In this example, `Subjects` is a key, with a value being another dictionary that holds the scores for "Maths" and "Physics".

### Opening a JSON file for writing:
```python
jsonFile = open("example.json", 'w')
```
The file "example.json" is opened in write mode ('w'). This is where the data will be written.

### Writing (dumping) the data to the JSON file:
```python
json.dump(data, jsonFile)
```
The `json.dump()` function is used to write (dump) the contents of the `data` dictionary into the `jsonFile`. This converts the Python dictionary into a valid JSON format and writes it to the file.

### Result:
After execution, the file "example.json" will contain:
```json
{
  "Subjects": {
    "Maths": 85,
    "Physics": 90
  }
}
```
