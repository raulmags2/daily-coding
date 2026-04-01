genes = []
lines = []
def sequence_writer (file):
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
while True:
    start_codon = seq.find('ATG', pos)
    if start_codon == -1:
        break
    first_stop = -1
    for stop in stops:
        test_stop = seq.find (stop, start_codon + 3)
        if test_stop != -1 and (test_stop - start_codon) % 3 == 0:
            if first_stop == -1 or test_stop < first_stop:
                first_stop = test_stop
    if first_stop != -1 and first_stop - start_codon >= 1000:
        gene = seq[start_codon : first_stop + 3]
        genes.append(gene)
    pos = start_codon + 1
data = "\n>\n".join(genes)
with open(input("Archive name:"), "w") as f:
    f.write(data)

    