#All the imports usage are listed below
import numpy as np #Important library to create matrices
import matplotlib.pyplot as plt #library used to create images and graphics
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor #An import from Bio library, used to construct the filogeny tree
from scipy.spatial.distance import pdist, squareform #An import from scipy, used to calculate distances belong the matrice
from Bio import Phylo #An import from bio, to create the filogenetics trees
from Bio.Phylo.TreeConstruction import DistanceMatrix #An import from bio, used to create the tree, using the matrix of distance.
#Here the code starts
#Create two empty lists. One of them will be used to list the caraters, and the other are used to list the especies.
character_list = [] 
species_name = []
data = [] #this list will become the final matrix
while True: #Create a loop, who will add spécies name until the user types 'N'
    specie = input("Type the species name, when finished, type N \n if you want to delete the last specie, type del")
    if specie == "N" or specie =="n":
        break
    elif specie == "del" or specie == "DEL": #if the users type 'del' or 'DEL', the last item will be deleted
        del species_name[-1]
    else:
        species_name.append(specie)
while True: #Create the same loop, but, with the caraters.
    character = input("type the caraters name, when finished, type N \n if you want to delete the last carater, type del")
    if character == "N" or character == "n":
        break
    elif character == "del" or character == "DEL":
        del character_list[-1]
    else:
        character_list.append(character)
for specie in species_name: #create a loop, who pass for each species
    state = [] #it´s a temporary list, will be deleted each time the loop occurs
    for character in character_list: #another loop, who passes for each character of each especie
        states = int(input(f"type the state of {character} in {specie}: "))
        state.append(states)
    data.append(state)
numpy_matriz = np.array(data) #will convert the [data], a list of lists in a matrix
plt.axis('off')  #turn the axes off
table = plt.table( #Create an table, who will be created with the matematics matrix
    cellText=data,
    rowLabels=species_name,
    colLabels=character_list,
    loc='center'
)
plt.savefig("matriz.png") #save the table in png format
distances = pdist(numpy_matriz) #transform the created matrix in one distance matrix
distance_matrix = squareform(distances) #turn the matrix in one squareform matrix
triangular_matrix = [] #create an empty list, who will become one triangular matrix
for i in range(len(distance_matrix)):
    line = []
    for j in range(1+ i):
        line.append(distance_matrix[i][j])
    triangular_matrix.append(line)
bio_matrix = DistanceMatrix(names=species_name, matrix = triangular_matrix) #transform this matrix in a Bio format
constructor = DistanceTreeConstructor() #create an empty tree
tree = constructor.upgma(bio_matrix) #create the tree, using the matrix as base
while True: #Create a loop to ask to the user the external group name, if the name isn´t in the species list, ask again
    external_group = input("type the external group name:")
    if external_group not in species_name:
        print("Error: the external group is not a valid specie, try again:")
        continue
    try:    
        total_length = tree.distance(external_group)
        tree.root_with_outgroup({"name": external_group}, outgroup_branch_length = total_length/2) #root with the external group
        break
    except Exception as error:
        print(f"Error: {error}, try again:")
figure_tree = plt.figure()
tree_axis = figure_tree.add_subplot(1,1,1)
Phylo.draw(tree, axes=figure_tree, label_func=lambda clade: clade.name if clade.is_terminal() else "")
figure_tree.set_xlabel('')
figure_tree.set_ylabel('')
figure_tree.set_yticks('')
figure_tree.set_xticks('')


Phylo.draw(tree) #draw the tree
plt.axis('off') #turn the axis off
plt.savefig("arvore.png") #save the final tree as a png image
