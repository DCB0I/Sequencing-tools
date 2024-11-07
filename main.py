from DNAtoolkit import *
from utilities import *
import random


rndDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(20)])

DNAstr = validateSeq(rndDNAStr)
print(f'[1]\nSequence (Non coding strand): {color(DNAstr)}\n')
print(color(f'[2]\nNucleotide Frequency : {countNucFrequency((DNAstr))}\n'))
print(f"[3]\nDNA/RNA transcription: {transcription(color(DNAstr))}\n")

print(f"[4] + DNA String + Reverse Complement: \n5' {color(DNAstr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAstr))])}")
print(f"3' {color(reverse_complement(DNAstr))} 5'\n")
print(f"[5] + GC Content : {gc_content(DNAstr)}%\n")
print(f"[6] + GC Content subseq : {gc_content_subsec(DNAstr, k=20)}%\n")
print(f'[7] + Amino acids Sequence from DNA: {translate_seq(DNAstr, 0)}\n')
print(f'[8] + Codon frequency (L) : {codon_usage(DNAstr, "L")}\n')
print(f'[9] + Reading Frames : ')
for frame in gen_reading_frames(DNAstr):
    print(frame)

test_rf = frame
print(protein_from_rf(test_rf))

print('\n[10] + All proteins in 6 open reading frames: ')
for prot in all_proteins_from_orfs(AA, 0, 0, True):
    print(f'{prot}')
