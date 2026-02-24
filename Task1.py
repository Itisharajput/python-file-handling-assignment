# Task 1: Demonstrates file reading using with statement and exception handling

# Try block to handle file operations safely
try:
# Opening the file in read mode using with statement
    with open('sample.txt', 'r') as fh:
        for line in fh:
            print(line.strip())
            # print(line , end="")
# Haandling the case where the file does not exist       
except FileNotFoundError:
    print("The file 'sample.txt' was not found.") 
finally:
    print("File operation completed.")
