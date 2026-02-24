# Task 2: demonstrates writing, appending, and reading a file with exception handling
try:
# writing user input to the file
    with open('output.txt','w') as fh:
        fh.write(input("Enter text to write to the file: "))
        print("Data successfully written to output.txt.")
# Appending additional input to the same file        
    with open('output.txt','a') as fh:
        fh.write(input("Enter additional text to append:")+ "\n")
        print("Data successfullt appended.")
# Reading and displaying file contents    
    with open('output.txt', 'r') as fh:
        for line in fh:
            print(line,end='')
except IOError:
# Handling gerneral input/output errors
    print("An I/O error occurred while working with the file.")
finally:
# This block always executes
    print("File operation completed.")
