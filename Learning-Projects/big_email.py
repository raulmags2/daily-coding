fname = input("Enter file:")
count = dict()
fh = open(fname)
final_list = []
big_email = -1
for line in fh:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        final_list.append(line.split()[1])
for word in final_list:
    count[word] = count.get(word, 0) + 1
for key in count:
    if count[key] > big_email or big_email == -1:
        big_email = count[key]
        big_key = key
print(big_key, big_email)