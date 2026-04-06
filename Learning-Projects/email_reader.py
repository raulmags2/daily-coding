fname = input("Enter file name: ") #ask to the user the file name
fh = open(fname) #open the file
count = 0
for line in fh:
    if line.startswith('From:'): #avoid from:
        continue
    elif line.startswith('From'): #for each line starts with from, print the second word and adds one to count
        list = line.split()
        print(list[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word") #print the number of lines start with from
