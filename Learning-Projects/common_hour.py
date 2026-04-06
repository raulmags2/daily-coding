fname = input("Enter file:")
fh = open(fname)
final_list = []
count = dict()
listt = []
for line in fh:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        initial_list = []
        initial_list = line.split()
        final_list.append(initial_list[5])
for word in final_list:
    listt.append(word[0 : 2])
for number in listt:
    count[number] = count.get(number, 0) + 1
for key in sorted(count):
    print(key, count[key])
    