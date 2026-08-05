#All the imports usage are listed below
import numpy as np #Important library to create matrices
import matplotlib.pyplot as plt #library used to create images and graphics
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor #An import from Bio library, used to construct the filogeny tree
from scipy.spatial.distance import pdist, squareform #An import from scipy, used to calculate distances belong the matrice
from Bio import Phylo #An import from bio, to create the filogenetics trees
from Bio.Phylo.TreeConstruction import DistanceMatrix #An import from bio, used to create the tree, using the matrix of distance.
import sys


def help_menu(): #Create a help menu, explaining how to use the app
    print("=" * 55)
    print("                    HELP MENU")
    print("=" * 55)
    print("This program builds a phylogenetic tree based on")
    print("character states for each species.")
    print()
    print("STEPS:")
    print("  1. Enter the species names")
    print("  2. Enter the characters to compare")
    print("  3. For each species, type the state of each character")
    print("  4. Choose an outgroup to root the tree")
    print()
    print("COMMANDS (during input):")
    print("  N      -> finish current input")
    print("  DEL    -> remove the last entry")
    print("=" * 55)


def main_menu(): #Give the option to the user, to start or acess help_menu
    print("=" * 55)
    print("              Filogenia")
    print("=" * 55)
    while True:
        choice = input("Type [S] to start or [H] for help:").upper()
        if choice == "S":
            break
        if choice == "H":
            help_menu()


def get_species_name(): #this function asks for the species_name
    species_name = []
    while True: #Create a loop, who will add species name until the user types 'N'
        specie = input("Type the species name, when finished, type N \n if you want to delete the last specie, type del  ")
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
    character_list = []
    while True: #Create the same loop, but, with the caraters.
        character = input("type the caraters name, when finished, type N \n if you want to delete the last carater, type del  ")
        command_c = character.upper()
        if command_c == "N":
            if len(character_list) >= 1:
                break
            else:
                print("You need 1 or more characters to continue. Try again: ")
                continue
        if command_c == "DEL":
            if len(character_list) == 0:
                print("No character to delete, try again:")
                continue
            else:
                del character_list[-1]
        elif command_c == "CLEAR":
            character_list.clear()
        else:
            character_list.append(character)
    return character_list


def get_character_states(species_name, character_list): #create a loop, who pass for each species
    data = [] #this list will become the final matrix
    for specie in species_name:
        state = [] #it's a temporary list, will be deleted each time the loop occurs
        for character in character_list: #another loop, who passes for each character of each especie
            while True:
                try:
                    states = int(input(f"type the state of {character} in {specie}: "))
                    state.append(states)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
        data.append(state)
    return data


def save_table(data, species_name, character_list): #Create an table, who will be created with the matematics matrix
    numpy_matriz = np.array(data) #will convert the [data], a list of lists in a matrix
    plt.axis('off')  #turn the axes off
    table = plt.table(
        cellText=data,
        rowLabels=species_name,
        colLabels=character_list,
        loc='center'
    )
    plt.savefig("matriz.png") #save the table in png format
    return numpy_matriz


def build_tree(numpy_matriz, species_name): #transform the created matrix in one distance matrix and build the tree
    distances = pdist(numpy_matriz) #transform the created matrix in one distance matrix
    distance_matrix = squareform(distances) #turn the matrix in one squareform matrix
    triangular_matrix = [] #create an empty list, who will become one triangular matrix
    for i in range(len(distance_matrix)):
        line = []
        for j in range(1 + i):
            line.append(distance_matrix[i][j])
        triangular_matrix.append(line)
    bio_matrix = DistanceMatrix(names=species_name, matrix=triangular_matrix) #transform this matrix in a Bio format
    constructor = DistanceTreeConstructor() #create an empty tree
    tree = constructor.upgma(bio_matrix) #create the tree, using the matrix as base
    return tree


def root_tree(tree, species_name): #Create a loop to ask to the user the external group name, if the name isn't in the species list, ask again
    while True:
        external_group = input("type the external group name:")
        if external_group not in species_name:
            print("Error: the external group is not a valid specie, try again:")
            continue
        try:
            total_length = tree.distance(external_group)
            tree.root_with_outgroup({"name": external_group}, outgroup_branch_length=total_length / 2) #root with the external group
            break
        except Exception as error:
            print(f"Error: {error}, try again:")
    return tree


def save_tree(tree): #save the final tree as a png image
    figure_tree = plt.figure()
    tree_axis = figure_tree.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=tree_axis, label_func=lambda clade: clade.name if clade.is_terminal() else "")
    tree_axis.set_xlabel('')
    tree_axis.set_ylabel('')
    tree_axis.set_yticks([])
    tree_axis.set_xticks([])
    tree_axis.axis('off') #turn the axis off
    plt.savefig("arvore.png") #save the final tree as a png image


def main():
    main_menu()
    species_name = get_species_name()
    character_list = get_characters_name()
    data = get_character_states(species_name, character_list)
    numpy_matriz = save_table(data, species_name, character_list)
    tree = build_tree(numpy_matriz, species_name)
    tree = root_tree(tree, species_name)
    save_tree(tree)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Programa interrompido pelo usuario.")
        sys.exit(0)
