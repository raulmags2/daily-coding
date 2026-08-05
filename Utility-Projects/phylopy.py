#All the imports usage are listed below
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor #An import from Bio library, used to construct the filogeny tree
from Bio import Phylo #An import from bio, to create the filogenetics trees
from Bio.Phylo.TreeConstruction import DistanceMatrix #An import from bio, used to create the tree, using the matrix of distance.
from Bio import SeqIO #An import from bio, used to read fasta files
from Bio.Align import PairwiseAligner #An import from bio, used to align sequences
from itertools import combinations #An import from itertools, used to combine species
import matplotlib.pyplot as plt #library used to create images and graphics
import os #An import from os, used to verify if the file exists
import sys #An import from sys, used to restart the program


def help_menu(): #Create a help menu, explaining how to use the app
    print("=" * 55)
    print("                    HELP MENU")
    print("=" * 55)
    print("This program builds a phylogenetic tree based on")
    print("genetic distances between species.")
    print()
    print("STEPS:")
    print("  1. Enter the species names")
    print("  2. Enter the characters (genes) to compare")
    print("  3. Provide a FASTA file for each (species, gene)")
    print("  4. Choose an outgroup to root the tree")
    print()
    print("COMMANDS (during input):")
    print("  N      -> finish current input")
    print("  DEL    -> remove the last entry")
    print("  CLEAR  -> remove all entries")
    print("=" * 55)


def main_menu(): #Give the option to the user, to start or acess help_menu
    print("=" * 55)
    print("              PhyloPy")
    print("=" * 55)
    while True: #Create a loop, who will ask the user to start or access the help menu
        choice = input("Type [S] to start or [H] for help:").upper()
        if choice == "S":
            break
        if choice == "H":
            help_menu()


def get_species_name(): #this function asks for the species_name
    species_name = []
    while True: #Create a loop, who will add species name until the user types 'N'
        specie = input("type the specie name: type N to finish and Del to delete the last specie")
        command_s = specie.upper()
        if command_s == "N":
            if len(species_name) >= 3:
                break
            else:
                print("You need 3 or more species to continue. Try again:")
                continue
        if command_s == "DEL":
            if len(species_name) == 0:
                print("No specie to delete, try again:")
                continue
            else:
                del species_name[-1]
        elif command_s == "CLEAR":
            species_name.clear()
        else:
            species_name.append(specie)
    return species_name


def get_characters_name(): #this function asks for the character names
    characters_name = []
    while True: #Create the same loop, but, with the characters.
        character = input("type the character name: type N to finish and Del to delete the last character ")
        command_c = character.upper()
        if command_c == "N":
            if len(characters_name) >= 1:
                break
            else:
                print("You need 1 or more genes to continue. Try again: ")
                continue
        if command_c == "DEL":
            if len(characters_name) == 0:
                print("No gene to delete, try again:")
                continue
            else:
                del characters_name[-1]
        elif command_c == "CLEAR":
            characters_name.clear()
        else:
            characters_name.append(character)
    return characters_name


def get_genes_fasta(species_list, character_list): #create a loop, who pass for each species and character
    data = {} #this dict will store the sequences for each species and character
    for specie in species_list:
        data[specie] = {}
        for character in character_list: #another loop, who passes for each character of each especie
            while True:
                fname = input(f"FASTA file for {character}:" "SKIP if the species doesn't have this gene").strip()
                test = fname.upper()
                if test == "SKIP":
                    data[specie][character] = None
                    break
                if fname.endswith(".fasta"):
                    path = fname
                else:
                    path = fname + ".fasta"
                if not os.path.isfile(path):
                    print("Inexistent file, try again:")
                    continue
                try:
                    record = SeqIO.read(f"{path}", "fasta")
                except Exception as e:
                    print(f"invalid fasta file:{e}")
                    continue
                data[specie][character] = record.seq
                break
    return data


def less_3(species_list, character_list): #this function is called when the user has less than 3 species
    less_sp = 3 - (len(species_list))
    print(f"Now, you have less than 3 species. Type more {less_sp} or more species")
    more_species = []
    while True: #Create a loop, who will add species name until the user types 'N'
        specie = input("type the specie name: type N to finish and Del to delete the last specie")
        command_s = specie.upper()
        if command_s == "N":
            if len(more_species) >= less_sp:
                break
            else:
                print("You need 3 or more species to continue. Try again:")
                continue
        if command_s == "DEL":
            if len(more_species) == 0:
                print("No specie to delete, try again:")
                continue
            else:
                del more_species[-1]
        elif command_s == "CLEAR":
            more_species.clear()
        else:
            more_species.append(specie)
    more_data = get_genes_fasta(more_species, character_list)
    return more_data, more_species


def test_sp(data, species_list, character_list): #this function tests if the species have common genes
    stop = True
    resolved_with_d = set()
    while stop == True:
        for sp1, sp2 in combinations(data, 2):
            if frozenset((sp1, sp2)) in resolved_with_d:
                continue
            commum_genes = 0
            for gene in data[sp1]:
                if gene not in data[sp2]:
                    continue
                seq_1 = data[sp1][gene]
                seq_2 = data[sp2][gene]
                if seq_1 is None or seq_2 is None:
                    continue
                else:
                    commum_genes = commum_genes + 1
            if commum_genes == 0:
                x = no_genes(sp1, sp2)
                if x == 0:
                    del data[sp1]
                    species_list.remove(sp1)
                    print(f"{sp1} deleted from data")
                    stop = True
                    if len(species_list) >= 3:
                        break
                    else:
                        more_data, more_species = less_3(species_list, character_list)
                        species_list.extend(more_species)
                        data.update(more_data)
                        break
                if x == 1:
                    stop = True
                    del data[sp2]
                    species_list.remove(sp2)
                    print(f"{sp2} deleted from data")
                    if len(species_list) >= 3:
                        break
                    else:
                        more_data, more_species = less_3(species_list, character_list)
                        species_list.extend(more_species)
                        data.update(more_data)
                        break
                if x == 2:
                    del data[sp1]
                    stop = True
                    del data[sp2]
                    species_list.remove(sp1)
                    species_list.remove(sp2)
                    print(f"{sp1} and {sp2} deleted from data")
                    if len(species_list) >= 3:
                        break
                    else:
                        more_data, more_species = less_3(species_list, character_list)
                        species_list.extend(more_species)
                        data.update(more_data)
                        break
                if x == 3:
                    resolved_with_d.add(frozenset((sp1, sp2)))
                    stop = False
                    continue
                if x == 4:
                    print("restarting the programm...")
                    python = sys.executable
                    os.execv(python, [python] + sys.argv)
            else:
                stop = False

    # sanity check: a distance tree needs at least 3 species
    if len(species_list) < 3:
        print("=" * 55)
        print(f"Only {len(species_list)} species left in the analysis.")
        print("A phylogenetic tree needs 3 or more species.")
        print("script closed!")
        sys.exit(0)

    return data, species_list


def no_genes(sp1, sp2): #this function is called when two species don't have common genes
    print(f"the species {sp1} and {sp2} doesn't have any commum genes, the comparison isn't possible ")
    print("=" * 55)
    print("           Options:")
    print(f"'SP1' to remove {sp1} from the tree")
    print(f"'SP2' to remove {sp2} from the tree")
    print("'SP' to remove both species from the tree")
    print("'D' to assume the maximum distance from the two species")
    print("'R' to restart the script")
    while True:
        test = input("Type:").upper()
        if test == "SP1":
            x = 0
            break
        if test == "SP2":
            x = 1
            break
        if test == "SP":
            x = 2
            break
        if test == "D":
            x = 3
            break
        if test == "R":
            x = 4
            break
        else:
            print("Error. Insert a valid input")
            continue
    return x


def distances(data): #this function calculates the distances between species
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -1
    distances_dict = {}
    for sp1, sp2 in combinations(data, 2):
        distances_sum = 0
        commum_genes = 0
        for gene in data[sp1]:
            if gene not in data[sp2]:
                continue
            seq_1 = data[sp1][gene]
            seq_2 = data[sp2][gene]
            if seq_1 is None or seq_2 is None:
                continue
            else:
                commum_genes = commum_genes + 1
            score = aligner.score(seq_1, seq_2)
            score_max = max(
                aligner.score(seq_1, seq_1),
                aligner.score(seq_2, seq_2)
            )
            distance = 1 - (score / score_max)
            distances_sum = distances_sum + distance
        if commum_genes == 0:
            distances_dict[sp1, sp2] = 1.0
            distances_dict[sp2, sp1] = 1.0
        else:
            average_distances = distances_sum / commum_genes
            distances_dict[sp1, sp2] = average_distances
            distances_dict[sp2, sp1] = average_distances
    return distances_dict


def matrix(species_list, n_dict): #this function creates the distance matrix
    matrix_d = []
    for i, sp1 in enumerate(species_list):
        row = []
        for j in range(i + 1):
            sp2 = species_list[j]
            if sp1 == sp2:
                row.append(0.0)
            else:
                row.append(n_dict[(sp1, sp2)])
        matrix_d.append(row)
    return DistanceMatrix(names=species_list, matrix=matrix_d)


def constructor(bio_matrix, species_list): #this function constructs the tree and roots it
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(bio_matrix)
    while True: #Create a loop to ask to the user the external group name, if the name isn't in the species list, ask again
        external_group = input("Type the external_group name:")
        if external_group not in species_list:
            print(f"{external_group} is not in the species list, try again:")
            print("=" * 55)
            continue
        try:
            tree.root_with_outgroup(external_group) #root with the external group
            break
        except Exception as error:
            print(f"Error: {error}, try again:")

    figure_tree = plt.figure()
    tree_axis = figure_tree.add_subplot(1, 1, 1)
    for clade in tree.get_nonterminals():
        clade.name = None
    Phylo.draw(tree, axes=tree_axis, do_show=False)
    tree_axis.set_xlabel('')
    tree_axis.set_ylabel('')
    tree_axis.set_yticks([])
    tree_axis.set_xticks([])
    plt.savefig("arvore.png") #save the final tree as a png image


def main():
    main_menu()
    species_list = get_species_name()
    character_list = get_characters_name()
    data = get_genes_fasta(species_list, character_list)
    new_data, new_species_list = test_sp(data, species_list, character_list)
    distances_dict = distances(new_data)
    bio_matrix = matrix(new_species_list, distances_dict)
    constructor(bio_matrix, new_species_list)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Programa interrompido pelo usuario.")
        sys.exit(0)
