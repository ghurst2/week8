#!/usr/bin/env python

#reads the users DNAseq
DNASeq = input("Provide a DNA sequence:")

#Convert the imput sequence to be all uppercase letters
DNASeq = DNASeq.upper()

#Creates the complement of the nucleotides (A=T)
print("The complement sequence:")
DNAComp = (DNASeq.replace("A","t").replace("T","A").replace("G","c").replace("C","G").upper()) # DB: Creative!
print(DNAComp)

#Reverse the sequence
print("The reverse complement sequence:")
reversedDNAComp = DNAComp [::-1]
print(reversedDNAComp)

# DB: Nicely done!