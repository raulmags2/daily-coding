import re #import regex
fname = input("Type the file name:")
fh = open(fname)#Open the file
lines = [] #create an ampty list
final_list = []
for line in fh: #for each line in fh, removes the whitespace in the right and, if the line starts with >, adds to the list
    line = line.rstrip() 
    if re.search(r"^>", line):
        lines.append(line)
for i, Id in enumerate(lines): #Loops the enumerate list and adds Id and the number of the id and a new line
    Id = (f"\nId {i}\n {Id}")
    final_list.append(Id)
final_data = "".join(final_list) #adds the final_list to a string
with open (input("Type the new file name:"), "w") as f:#write the string to a data file
    f.write(final_data)