seq = input("Type your sequence:")  
start_codon = seq.find('ATG')
stops = ["TAA", "TAG", "TGA"]
first_stop = -1
for stop in stops:
    test_stop = seq.find(stop, start_codon + 3)
    if test_stop != -1 and (first_stop - start_codon) % 3 == 0:
        if first_stop == -1 or test_stop < first_stop:
            first_stop = test_stop
print(f"The start codon starts in {start_codon}")
print(f"The stop codon starts in {first_stop}") 
print(f"The sequence is: {seq[start_codon : first_stop + 3]}")

