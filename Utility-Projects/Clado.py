from Bio import Phylo
from io import StringIO
import matplotlib.pyplot as plt
newick_string = """(((1,2),(30,32),(5,(6,12)),(11,13),(14),(3,4),(7,(12,(8,20),(16,28),(17,19),(15,27)),(25,18),(9,10))),(21,23,(22,24),(26,(29,31))));"""
tree = Phylo.read(StringIO(newick_string), "newick")
fig, ax = plt.subplots(figsize = (14, 10))
Phylo.draw(tree, axes=ax)
plt.tight_layout()
plt.savefig('Clado_besouros.png', dpi = 200, bbox_inches='tight', facecolor='white')