fname = input("Enter file name: ")
fh = open(fname)
final_list = []
for line in fh:
    for word in line.split():
        if word not in final_list:
            final_list.append(word)
final_list.sort()
print(final_list)
