## Description
This folder contains small Python scripts created during my learning journey. These projects were developed purely for training purposes and have limited practical utility. They serve as stepping stones in my Python education.

## Projects

### 1. GC Counter (DNA Sequence Analysis)
- **Description:** Calculates the GC content (percentage of Guanine and Cytosine) in a DNA sequence.
- **Purpose:** Training string manipulation and basic sequence analysis.
- **Note:** This implementation uses manual input for training purposes. Real DNA sequences are typically analyzed using FASTA files, not user input.
- **Technologies:** Python (string methods)

### 2. Sequence Finder (DNA Sequence Analysis)
- **Description:** Finds one gene between the start and stop codon.
- **Purpose:** Training string manipulation and basic sequence analysis.
- **Note:** This implementation uses manual input for training purposes. Real DNA sequences are typically analyzed using FASTA files, not user input.
- **Technologies:** Python (string manipulation, Biopython)

### 3. Email Reader (File Parsing)
- **Description:** Reads a text file containing email logs and extracts the sender address from each line that starts with `From` (excluding `From:` headers). Prints each sender address and a final count of matching lines.
- **Purpose:** Training file I/O, string methods (`startswith`, `split`), and conditional filtering.
- **Technologies:** Python (file handling, string methods)

### 4. Sorter (Unique Word List)
- **Description:** Reads a text file, splits every line into individual words, and builds a sorted list of unique words — skipping duplicates. Prints the final alphabetically sorted list.
- **Purpose:** Training file I/O, list operations (`append`, `sort`), and membership testing with `not in`.
- **Technologies:** Python (file handling, lists, string methods)

### 5. Common Hour (Email Log Analysis)
- **Description:** Reads an email log file (`mbox-short.txt`), extracts the hour from each `From ` line, and counts how many messages were sent in each hour of the day. Prints the results sorted by hour in ascending order.
- **Purpose:** Training file I/O, string slicing, dictionaries (`get`), and sorting with `sorted()`.
- **Technologies:** Python (file handling, string methods, dictionaries)

### 6. Big Email (Most Prolific Sender)
- **Description:** Reads an email log file (`mbox-short.txt`), counts how many times each sender address appears in `From ` lines, and prints the address with the highest message count along with that count.
- **Purpose:** Training file I/O, dictionaries, and maximum-value tracking with a loop.
- **Technologies:** Python (file handling, string methods, dictionaries)
