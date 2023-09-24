

In this code file named "pos_conserv.py", fasta_Reader function takes a fasta file as an input and returns a dictionary of sequences where keys hold the information about the sequence and value stores the actual sequence. 

Since there are also 'X' symbols in the sequences which stands for any amino acid, they are all changed to Alanine amino acid. 

aa_dict is the template amino acid dictionary to be able to count every aminoacid that is seen in the sequences so that the frequency can easily found.

matrixOfFrequencies is composed of 20 columns where every column is an amino acid by itself. Furthermore there will be position many rows. This position phrase is used to represent the length of the MSA. Thus, the matrix will collect every aminoacid's frequency in every position. For example, first column of first row will stand for the frequency of Alanine aminoacid. Aminoacids will be in alphebetical order in the columns and their column values can be reached with the dictionary named volume_of.

numberOfiad variable is a list that will keep the total number of dashes for every position. This will be useful since we won't be considering the positions in the alignment with more than 100 gaps. 

After calculationg all the frequency values and store them in a matrix, we have to find a way to represent positional conservation score for each index/position. For this purpose, entropy of that specific position is calculated. conservationIndex variable keeps the entropy score for each position. 

By looking at the MEGA alignment and comparing it with the entropy scores, we came up with a cutoff score of 30000. Positions with Entropy value bigger than 30000 showed too much variance while positions with entropy value smaller than the cutoff show little fluctuations from the referenced amino acid. 

Thus, in the continuation of the code, positions with entropy value smaller than 1000 are appended to the conservedpos list if their total dash count is also smaller than 100.

In conclusion, for any variant with unknown significance, code will take an input of aligned location (with gaps) of the mutation and output if the change on that position is critical or not. Critical means that the position is a highly conserved region and mutation on that region is not seen in the phylogenetic tree mostly. 


Furhtermore, code also visualizes the entropy scores so that the conserved regions can easily be seen. 

Lastly, below code draws the graph of Entropies of the positions as a graph.

![codeForGraph](/codeForGraph.JPG) <font size="5">__Fig.1__ : Code of Entropy Scores per Position </font>

