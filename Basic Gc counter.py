
Sequence = input("Type your Sequence:").lower() #Ask the user for the DNA sequence to analyze
gc = 0 #Initialize GC counter to zero
for content in Sequence: # Iterate through the sequence and count 'g' or 'c' bases
    if content == 'g' or content == 'c':
        gc = gc + 1
print(f"the gc count is: {gc}")    
Total = len(Sequence) #calculate the total of bases in the sequence
GC_percentage = gc / Total * 100 #Calculate the GC percentage
print(f"your percentage of GC content is: {GC_percentage:.2f}%")