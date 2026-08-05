# Utility Projects

This folder contains Python projects developed during my learning journey that have practical utility. These projects are slightly more complex than learning projects and can be used for real-world applications.

## Projects

### 1. Second-Degree Polynomial Calculator
- **Description:** Solves quadratic equations and calculates corresponding y-values.
- **Features:**
  - Finds roots of second-degree polynomials
  - Calculates y-values for all integer x-values between the roots

### 2. Third-Degree Polynomial Reducer
- **Description:** Analyzes and simplifies third-degree polynomials.
- **Features:**
  - Finds polynomial roots
  - Reduces polynomial expressions

### 3. Fasta_GC_Counter
- **Description:** Reads a DNA sequence and calculates the percentage of GC content.
- **Features:**
  - Reads a DNA sequence
  - Counts the total number of bases and the number of GC bases
  - Calculates the GC percentage

### 4. ncbi_downloader
- **Description:** Downloads a DNA sequence from NCBI using its accession ID.
- **Features:**
  - Searches the NCBI database for a sequence by accession ID
  - Saves the sequence to a `.fasta` file

### 5. sequence_finder
- **Description:** Reads a DNA sequence and searches for the start and stop codons, then prints the gene between them.
- **Features:**
  - Reads a `.fasta` file and finds the start and stop codons
  - Prints the found gene

### 6. orf_finder
- **Description:** Reads a DNA sequence, finds the possible relevant genes, and saves them to a new `.fasta` file.
- **Features:**
  - Reads a `.fasta` file and finds the start codon
  - Finds the next valid stop codon and saves the sequence between the start and stop into a list
  - Writes a new file with the found genes

### 7. automatic_tree_constructor
- **Description:** Creates an automatic phylogenetic tree using different states from characters in different species.
- **Features:**
  - Uses inputs to collect different states from characters
  - Creates a matrix using the states from characters
  - Creates a phylogenetic tree using this matrix

### 8. phylopy
- **Description:** Reads FASTA files from different species and creates a phylogenetic tree.
- **Features:**
  - Uses inputs to collect different species names
  - Uses inputs to collect the names of the FASTA files for each species
  - Reads each FASTA file, creating a distance score between species
  - Uses the distance score to create a triangular matrix
  - Uses the matrix to create a phylogenetic tree
