'''
 First, amino acid frequencies at each position
are estimated. The conservation index is then calculated
from these frequencies. An optional third step allows the
user to average the conservation indices over a window
covering a selected number of positions.

'''
import math
import matplotlib.pyplot as plt

def fastareader(filename):
    seqDict = {}
    with open(filename, "r") as filein:
        for line in filein:
            if line.startswith(">"):
                header = line[1:].strip()
                seqDict[header] = ""
            else:
                seqDict[header] += line.strip()
    return seqDict

filename = "alignment1000.fas"
MSA_dict = fastareader(filename)

complementary = {
     "A":   "A", "C":   "C", "D":   "D",
    "E":   "E", "F":  "F", "G":  "G",
    "H":   "H", "I":  "I", "K":  "K",
    "L":   "L", "M":  "M", "N":  "N",
    "P":   "P", "Q":  "Q", "R":  "R",
    "S":   "S", "T":  "T", "V":   "V",
    "W":   "W", "Y":  "Y",  "X": "A", 
    "-" : "-"
}

for key,value in MSA_dict.items():
    if "X" in value:
        value = "".join([complementary[c] for c in value])

aa_dict = {
    "A":   0, "C":   0, "D":   0,
    "E":   0, "F":   0, "G":   0,
    "H":   0, "I":   0, "K":   0,
    "L":   0, "M":   0, "N":   0,
    "P":   0, "Q":   0, "R":   0,
    "S":   0, "T":   0, "V":   0,
    "W":   0, "Y":   0,
}

volume_of = {
    "A":   1, "C":   2, "D":   3,
    "E":   4, "F":   5, "G":   6,
    "H":   7, "I":   8, "K":   9,
    "L":  10, "M":  11, "N":  12,
    "P":  13, "Q":  14, "R":  15,
    "S":  16, "T":  17, "V":  18,
    "W":  19, "Y":  20,
}
 
matrixOfFrequencies = [] #there will be 20 columns (for amino acids) and position many rows

lengthOfMSA = len((list(MSA_dict.values()))[0])
dictLen = len(MSA_dict)

eMSA_dict = {}
count = 0
for key,value in MSA_dict.items():
    eMSA_dict[count]= value
    count+=1
    
numberOfiad = []
for pos in range(lengthOfMSA):
    for key, value in aa_dict.items():
        aa_dict[key] = 0
    aaDictForPos = aa_dict
    totalBases = 0
    iadForPos = 0
    frequencyArray = []
    for i in range(dictLen):
        if eMSA_dict[i][pos] != "-":
            aa = eMSA_dict[i][pos]
            if aa == "X":
                aaDictForPos["A"]+=1
            else:
                aaDictForPos[aa]+=1
            totalBases+=1
        else: 
            iadForPos +=1
    for key,value in aaDictForPos.items():
        frequencyArray.append(aaDictForPos[key]/totalBases)
    matrixOfFrequencies.append(frequencyArray)
    numberOfiad.append(iadForPos)
    
#print(matrixOfFrequencies[42])  

    

    
        
 #In this step- to be able to calculate the conservation index of the position, we used 
 #entropy-based measure. 
 
conservationIndex = []  
'''
for pos in range(lengthOfMSA):
    entropyForThisPos = 0
    for row in matrixOfFrequencies:
        freq = row[pos]  
        if freq != 0:
            entropyForThisPos+= freq*(math.log(freq))
    conservationIndex.append(entropyForThisPos)
'''

for pos_row in matrixOfFrequencies:
    entropyForThisPos = 0
    for freq in pos_row:
        if freq != 0:
            entropyForThisPos+= i*(math.log(i))
    conservationIndex.append(entropyForThisPos)


#Now, conservationIndex[pos-1] will give the positional conservation score calculated by entropy based-measure.
        


conservedpos = []
for i in range(len(conservationIndex)):
    if conservationIndex[i]<= 30000 and numberOfiad[i]<100:
        conservedpos.append(i-1)
        #print(i-1)
        
 
#print(conservationIndex)       
"""    
y = conservationIndex
x = range(len(conservationIndex))
plt.title("Line graph")
plt.plot(x, y, color="red")
plt.show()
"""

#from here, check if that position where mutation happened is pathogenic or not. 

poss = ""
while poss != "0":
    poss = input("Please enter the position you want to look as integer: ")
    if int(poss) in conservedpos:
        print("critical")
    else:
        print("not critical")

            
'''
for key,value in MSA_dict.items():
    lengthofseq = 0
    aaDictForThis = aa_dict
    arrayToAdded = []
    for i in range(len(value)):
        if value[i] != "-":
            lengthofseq+=1
            aaDictForThis[value[i]]+=1
    for key,value in aaDictForThis.items():
        arrayToAdded.append(value/lengthofseq)
'''

            