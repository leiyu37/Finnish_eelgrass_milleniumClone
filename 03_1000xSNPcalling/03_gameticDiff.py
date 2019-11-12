#!/usr/bin/env python3
# identify the genetic differences between control sample and the ancestral zygote, based on 80x data results.
f_in = open("sm_add1000x_snp.vcf")
f_pos = open("gametic.pos", "w")
allHet = 0
allHomo = 0
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		if len(columns[3]) == 1 and len(columns[4]) == 1:
			chrom = columns[0]
			pos = columns[1]
			hr = 0
			hv = 0
			het = 0
			others = 0
			for i in range(9, len(columns)):
				genotype = columns[i].split(":")[0]
				if genotype == "0/0" or genotype == "0|0":
					hr += 1
				elif genotype == "1/1" or genotype == "1|1":
					hv += 1
				elif genotype == "0/1" or genotype == "0|1":
					het += 1
				elif genotype == "./.":
					others += 1
			n = hr + hv + het + others
			nhet = others + het
			nhomo = others + hv
			if others <13 and (nhet == n or nhomo == n):
				f_pos.write("{}\t{}\n".format(chrom, pos))
			if others <13 and (nhet == n):
				allHet += 1
			if others <13 and (nhomo == n):
				allHomo += 1
f_in.close()
f_pos.close()
f_out = open("oneGenotype.txt", "w")
f_out.write("Heterozygote:\t{}\nHomozygote\t{}\n".format(allHet, allHomo))
f_out.close()
