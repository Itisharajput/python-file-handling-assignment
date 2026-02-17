with open('output.txt','w') as fh:
    fh.write(input("Enter text to write to the file: "))
    print("Data successfully written to output.txt.")
with open('output.txt','a') as fh:
    fh.write(input("Enter additional text to append:")+ "\n")
    print("Data successfullt appended.")

with open('output.txt', 'r') as fh:
    for line in fh:
        print(line,end='')
