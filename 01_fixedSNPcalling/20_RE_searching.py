#!/usr/bin/env python3
# to obtain all the restriction enzyme related loci in the reference genome.
# then use bash command line to find the overlap between these loci and the SNP positions. select the target ones and design primers.
from Bio import SeqIO
from Bio.Restriction import *
rb_supp = RestrictionBatch(first=[], suppliers=['N'])
resite = open("REcut_x.txt","w")
for record in SeqIO.parse("GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna","fasta"):
	output_dic = rb_supp.search(record.seq)
	for enzyme in output_dic.keys():
		pattern_str = enzyme.elucidate()
		number_nucs = pattern_str.upper().count("A") + pattern_str.upper().count("T") + pattern_str.upper().count("G") + pattern_str.upper().count("C") + 2
		if number_nucs == len(pattern_str) and pattern_str.startswith("^") == False and pattern_str.startswith("_") == False:
			pos = pattern_str.replace("_", "").find("^")
			for cut in output_dic[enzyme]:
				for j in range(1, pos+1):
					cut_x = cut - j
					resite.write("{}\t{}\t{}\t{}\n".format(record.id, cut_x, enzyme, pattern_str))
				for k in range(0, len(pattern_str.replace("_", "").replace("^", "")) - pos):
					cut_y = cut + k
					resite.write("{}\t{}\t{}\t{}\n".format(record.id, cut_y, enzyme, pattern_str))
resite.close()
