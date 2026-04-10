count = 0
total_t = 0
total_gc = 0

def calculate_gc(sequence):
    gc_count = 0 #Initialize GC counter to zero
    gc_count = sum(1 for bases in sequence if bases in 'GC') #Adds 1 to gc count if a base is g or c
    total = len(sequence) #Calculate the total number of bases in the sequence
    gc_percentage = gc_count / total * 100 #Calculate the GC percentage
    return gc_percentage

while True:
    n_count = 0
    fname = input("File name:")
    if fname == "stop":
        break
    fh = open(fname)
    for line in fh:
        if line.startswith(">"):
            continue
        for base in line:
            count = count + 1
            n_count = n_count + 1
    gc = calculate_gc(fh)
    total = gc * n_count
    total_t = total_t + total
average_gc = total_t / count
print(f"the ")
