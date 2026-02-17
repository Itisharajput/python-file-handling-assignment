try:
    with open('sample.txt', 'r') as fh:
        for line in fh:
            print(line.strip())
            # print(line , end="")
       
except FileNotFoundError:
    print("The file 'sample.txt' was not found.") 
