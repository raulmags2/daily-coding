def calculate_gc(sequence):
    gc_count = 0 #Initialize GC counter to zero
    gc_count = sum(1 for bases in sequence if bases in 'gc') #adds 1 to gc count if a base is g or c   
    Total = len(sequence) #calculate the total of bases in the sequence
    GC_percentage = gc_count / Total * 100 #Calculate the GC percentage
    return GC_percentage
Seq = input("Type your Sequence:").lower() #Ask the user for the DNA sequence to analyze
result = calculate_gc(Seq)
print(f"the GC percentage in this sequence is {result:.2f}%")
