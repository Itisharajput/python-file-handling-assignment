# python-file-handling-assignment
Python Assignment 4 - File handling, reading/Writing files, and exception handling with error management.

# Assignment 4 - File Handling and Exception Handling in python

## Overview
This assignment demonstrates file handling operation in python including reading, writing, appending, and handling file-related errors using exception handling.
# Task 1
- Opens a file named 'sample.txt'
- Reads and prints content line by line
- Handles 'FileNOtFoundError' if the file does not exits

## Task 2
- Takes user input and write it to 'output.txt'
- Appends additional user input to the same file
- Reads and displays final content of the file

## Test Plan

### Task 1
- If sample.txt exists: file contents are printed.
- If sample.txt does not exist: appropriate error message is shown.
- Program always prints "File operation completed."

### Task 2
- User input is written to output.txt.
- Additional input is appended successfully.
- File contents are displayed correctly.
- Any file-related error is handled gracefully.

## Concepts Used
- File modes('r','w','a')
- 'with open()' Context manager
- 'try' and 'except'
- Exception handling('FileNotFoundError')

  
## Author
Itisha Rajput
