#!/usr/bin/env python3
# count the number of heterozygous modules for each locus
# then a r script is used to make the plot.
f_in = open("sm_only80x.recode.vcf")
f_out = open("number_Het_modules.txt", "w")
f_out.write("CHROM\tPOS\tnoHet\n")
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		hr = 0
		hv = 0
		het = 0
		others = 0
		chrom = columns[0]
		pos = columns[1]
		for i in range(9, len(columns)):
			genotype = columns[i].split(":")[0]
			if genotype == "0/0" or genotype == "0|0":
				hr += 1
			elif genotype == "1/1" or genotype == "1|1":
				hv += 1
			elif genotype == "0/1" or genotype == "0|1":
				het += 1
			else:
				others += 1
		t = others + het

		f_out.write("{}\t{}\t{}\n".format(chrom, pos, t))
f_in.close()
f_out.close()
