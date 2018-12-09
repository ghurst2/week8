#!/usr/bin/env python

#imports library
import random
#prompts user to determine what they want to do
#t= translate into amino acids
#r= randomly select codon
print("Press the key T to translate a protein-coding nucleotide sequence to amino acids or press the R key to randomly draw a codon from the sequence")
key = input()
#doesn't contiune until user selects "t" or "r"
while  key not in  ( "t","r"):
	print("Please ensure you have selected ethier key T or R")
	key = input()
#if user selects t prompts the user to enter a sequence
if key == "t":
	print("You have selected to translate a protein-coding nucleotide into amio acids")
	print("Please enter your protein-coding sequence:")
	CodeSeq = input()
#convert the input into all upper
	CodeSeq.upper()
#Dictonary for rna codon and animo acids
	rna_codon = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Ile", "GUU" : "Val",
           "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Ile", "GUC" : "Val",
           "UUA" : "Leu", "CUA" : "Leu", "AUA" : "Ile", "GUA" : "Val",
           "UUG" : "Leu", "CUG" : "Leu", "AUG" : "Met", "GUG" : "Val",
           "UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala",
           "UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala",
           "UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala",
           "UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala",
           "UAU" : "Tyr", "CAU" : "His", "AAU" : "Asn", "GAU" : "Asp",
           "UAC" : "Tyr", "CAC" : "His", "AAC" : "Asn", "GAC" : "Asp",
           "UAA" : "STOP", "CAA" : "Gln", "AAA" : "Lys", "GAA" : "Glu",
           "UAG" : "STOP", "CAG" : "Gln", "AAG" : "Lys", "GAG" : "Glu",
           "UGU" : "Cys", "CGU" : "Arg", "AGU" : "Ser", "GGU" : "Gly",
           "UGC" : "Cys", "CGC" : "Arg", "AGC" : "Ser", "GGC" : "Gly",
           "UGA" : "STOP", "CGA" : "Arg", "AGA" : "Arg", "GGA" : "Gly",
           "UGG" : "Trp", "CGG" : "Arg", "AGG" : "Arg", "GGG" : "Gly"
           }
	protein_string = ""
#Determine if sequence can be divided by 3
	for i in range(0, len(CodeSeq)-(3+len(CodeSeq)%3), 3):
		if rna_codon[CodeSeq[i:i+3]] == "STOP":
			break
#Translates the sequence to amino acids
		protein_string += rna_codon[CodeSeq[i:i+3]]
	print("Amino Acid sequence:")
	print( "Protein String: ", protein_string)
#if they have chosen r
else:
	print("You have selected to randomly draw a codon from the sequence")
	print("Please eneter a protein-coding sequence:")
	RandomSeq = input()
#breaks the input sequence up by 3
	RandSeq = [RandomSeq[i:i+3] for i in range(0, len(RandomSeq), 3)]
	print("Random codon from the sequence:")
	print(random.choice(RandSeq))

