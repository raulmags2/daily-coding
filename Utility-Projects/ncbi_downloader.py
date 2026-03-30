from Bio import Entrez #Import the library
Entrez.email = input("Type yout email:") #Asks the user email, used to enter in NCBI
handle = Entrez.efetch(db = input("type of data:"), id = input("id:"), rettype = input("Data format:"), retmode = "text") #Search in the ncbi for the sequence 
print("Searching for NBCI data...")
data = handle.read() #Read the sequence
handle.close() #close the connection
print("download completed")
with open(input("Archive name:"), "w") as f: #Save the sequence
    f.write(data)