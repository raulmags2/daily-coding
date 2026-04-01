genes = []
lines = []
def sequence_writer (file): #turn the fasta file into an string
    for line in file:
        line = line.rstrip()
        if line.startswith(">"):
            continue
        lines.append(line)
    full_sequence = "".join(lines)
    return full_sequence
pos = 0
stops = ["TAA", "TAG", "TGA"]
first_stop = -1
fname = input("type the file name:")
fh = open(fname)
seq = sequence_writer(fh)
number_filter = int(input("type the number of minimum bases the orf will have:")) #create a variable number, which will filter the minimum gene size
while True: #create a loop, which will be breaked when the sequence ends
    start_codon = seq.find('ATG', pos) #finds the next start codon 
    if start_codon == -1: #break the loop when the sequence ends
        break
    first_stop = -1
    for stop in stops:#tests all the possible stop codons after the start codon
        test_stop = seq.find (stop, start_codon + 3)
        if test_stop != -1 and (test_stop - start_codon) % 3 == 0: #tests if the stop codon is valid
            if first_stop == -1 or test_stop < first_stop: 
                first_stop = test_stop
    if first_stop != -1 and first_stop - start_codon >= number_filter: #if the stop codon exist and the gene size is valid, add the gene to the genes list
        gene = seq[start_codon : first_stop + 3]
        genes.append(gene)
    pos = start_codon + 1
data = "\n>\n".join(genes) #adds all the genes in the list to one string
with open(input("Archive name:"), "w") as f:
    f.write(data) #write that string into one .fasta file

    
