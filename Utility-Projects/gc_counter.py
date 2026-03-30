def calculate_gc(sequence):
    gc_count = 0 #Initialize GC counter to zero
    gc_count = sum(1 for bases in sequence if bases in 'GC') #Adds 1 to gc count if a base is g or c   
    total = len(sequence) #Calculate the total number of bases in the sequence
    gc_percentage = gc_count / total * 100 #Calculate the GC percentage
    return gc_percentage
fname = input("Type the file name:")
full_sequence = ("")
fh = open(fname)
lines = []
for line in fh:
    line = line.rstrip()
    if line.startswith(">"):
        continue
    lines.append(line)
full_sequence =  "".join(lines)
gc = calculate_gc(full_sequence)
print(f"The GC percentage is {gc:.2f}%")
