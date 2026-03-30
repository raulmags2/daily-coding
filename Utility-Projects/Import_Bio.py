from Bio import Entrez
Entrez.email = input("Type yout email:")
handle = Entrez.efetch(db = input("type of data:"), id = input("id:"), rettype = input("Data format:"), retmode = "text") 
print("Searching for NBCI data...")
data = handle.read()
handle.close()
print("download completed")
with open(input("Archive name:"), "w") as f:
    f.write(data)