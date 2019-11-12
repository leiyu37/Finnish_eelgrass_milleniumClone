#!/usr/bin/env python3
#the snp file and reference genome should be in the same folder
#output the SNP that change the reference sequence to a "GGCC"
from Bio import SeqIO
snp_name = "target.snp" #the positions for all SNPs in our dataset
f_out = open("01_mutationRE.pos", "w")
f_out.write("CHROM\tPOS\tREF\tVAR\tSEQ4-4\n")
i = 0
for record in SeqIO.parse("GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna", "fasta"):
	i += 1
	print("processing contig {}".format(i))
	f_in = open(snp_name)
	for line in f_in.readlines():
		if line.startswith("LFYR"):
			columns = line.split()
			chrom = columns[0]
			pos = int(columns[1])
			ref = columns[2]
			var = columns[3]
			if record.id == chrom and var.upper() == "G" and len(ref) == 1:
				pos_0b = pos - 1
				if pos_0b > 100:
					case_1 = "G"+record.seq[pos_0b+1:pos_0b+4]
					case_2 = record.seq[pos_0b-1] + "G" + record.seq[pos_0b+1:pos_0b+3]
					if case_1.upper() == "GGCC" or case_2.upper() == "GGCC":
						ref_seq = record.seq[pos_0b-4:pos_0b+5].upper()
						f_out.write("{}\t{}\t{}\t{}\t{}\n".format(chrom, pos, ref, var,ref_seq))
			elif record.id == chrom and var.upper() == "C" and len(ref) == 1:
				pos_0b = pos - 1
				if pos_0b > 100:
					case_1 = record.seq[pos_0b-2:pos_0b] + "C" + record.seq[pos_0b +1]
					case_2 = record.seq[pos_0b-3:pos_0b] + "C"
					if case_1.upper() == "GGCC" or case_2.upper() == "GGCC":
						ref_seq = record.seq[pos_0b-4:pos_0b+5].upper()
						f_out.write("{}\t{}\t{}\t{}\t{}\n".format(chrom, pos, ref, var,ref_seq))
	f_in.close()
f_out.close()

#make sure the target RE sequence is the only one in the amplified fragment, or the other RE sequence is at the downstream of the target one
f_out = open("02_primer_design.txt", "w")
f_out.write("CHROM\tPOS\tREF\tVAR\tREF_SEQ4-4\t1stGGCC\n")
for record in SeqIO.parse("GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna", "fasta"):
	f_in = open("01_mutationRE.pos")
	for line in f_in.readlines():
		if not line.startswith("CHROM"):
			columns = line.split()
			chrom = columns[0]
			pos = columns[1]
			if record.id == chrom:
				flank = record.seq[int(pos)-301 : int(pos)+300].upper()
				if flank.count("GGCC") == 0 or flank.find("GGCC") > 310:
					f_out.write(line.rstrip() + "\t" + str(flank.find("GGCC") + 1) + "\n")
	f_in.close()
f_out.close()
