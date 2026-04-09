import re #import regex
fname = input("Type the file name:")
fh = open(fname)#Open the file
lines = [] #create an ampty list
final_list = []
for line in fh: #for each line in fh, removes the whitespace in the right and, if the line starts with >, adds to the list
    line = line.rstrip()
    if re.search(r"^>", line):
        lines.append(line)
data = "\n".join(lines)
for i, Id in enumerate(lines):
    Id = (f"\nId {i}\n {Id}")
    final_list.append(Id)
final_data = "".join(final_list)
with open (input("Type the new file name:"), "w") as f:
    f.write(final_data)