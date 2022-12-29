#!/usr/bin/env python3

# Return other pair of DNA

# My Solution
def DNA_strand_1(dna:str):
    new_dna = []
    for i in range(len(dna)):
        if dna[i] == 'A':
            new_dna.append('T')
        elif dna[i] == 'T':
            new_dna.append('A')
        elif dna[i] == 'C':
            new_dna.append('G')
        elif dna[i] == 'G':
            new_dna.append('C')
    return ''.join(new_dna)

# CodeWars Solution 1
def DNA_strand_2(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

# CodeWars Solution 2
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand_3(dna):
    return ''.join([pairs[x] for x in dna])
