def calculate_gc(sequence):
    gc_count = 0 #Initialize GC counter to zero
    gc_count = sum(1 for bases in sequence if bases in 'GC') #adds 1 to gc count if a base is g or c   
    Total = len(sequence) #calculate the total of bases in the sequence
    GC_percentage = gc_count / Total * 100 #Calculate the GC percentage
    return GC_percentage
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
GC = calculate_gc(full_sequence)
print(f"The GC percentage is {GC:.2f}%")
