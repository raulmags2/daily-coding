def find_sequence(seq):
    start_codon = seq.find('ATG')
    stops = ["TAA", "TAG", "TGA"]
    first_stop = -1
    for stop in stops:
        test_stop = seq.find(stop, start_codon + 3)
        if test_stop != -1 and (test_stop - start_codon) % 3 == 0:
            if first_stop == -1 or test_stop < first_stop:
                first_stop = test_stop
    gene = seq[start_codon : first_stop + 3]
    return(gene)
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
complete_gene = find_sequence(full_sequence)
print(complete_gene)