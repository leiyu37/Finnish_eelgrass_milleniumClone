#!/usr/bin/env python3
# the 1000x dataset was used to check how many heterozygous genotypes were truely fixed, instead of being present in only in part of the module.
# for a truely fixed heterozygous genotype, there will be equal number of two different alleles.
# the variant read frequency will follow a binomial distribution withe mean=0.5, sd = sqrt(0.5*0.5/n), n indicates the coverage.
# Noorbakhsh, Javad, and Jeffrey H. Chuang. "Uncertainties in tumor allele frequencies limit power to infer evolutionary pressures." Nature genetics 49.9 (2017): 1288.
import math
f_in = open("sm_add1000x_good.recode.vcf")
n = 0
t = 0
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		# the genotypes of m08, m10, and m12 called in 80x data, respectively.
		s08_geno = columns[16].split(":")[0]
		s10_geno = columns[18].split(":")[0]
		s12_geno = columns[20].split(":")[0]
		# number of rererence and variant reads for m08 in 1000x data, respectively.
		s08x_ref = int(columns[35].split(":")[1].split(",")[0])
		s08x_var = int(columns[35].split(":")[1].split(",")[1])
		# number of rererence and variant reads for m10 in 1000x data, respectively.
		s10x_ref = int(columns[33].split(":")[1].split(",")[0])
		s10x_var = int(columns[33].split(":")[1].split(",")[1])
		# number of rererence and variant reads for m12 in 1000x data, respectively.
		s12x_ref = int(columns[34].split(":")[1].split(",")[0])
		s12x_var = int(columns[34].split(":")[1].split(",")[1])
		# if the genotype in 80x data is heterozygous, first check if the coverage in 1000x data is >500.
		# if so, calculate the confidence interval based on the coverage, and check if the variant read frequency lies in 95% confidence interval.
		if (s08_geno == "0/1" or s08_geno == "0|1") and (s08x_ref + s08x_var > 500):
			n+=1
			sd = round(math.sqrt(0.5*0.5/(s08x_ref + s08x_var)), 6)
			if round(s08x_var/(s08x_ref + s08x_var), 6) > (0.5-2*sd) and round(s08x_var/(s08x_ref + s08x_var), 6) < (0.5+2*sd):
				t+=1

		if (s10_geno == "0/1" or s10_geno == "0|1") and (s10x_ref + s10x_var > 500):
			n+=1
			sd = round(math.sqrt(0.5*0.5/(s10x_ref + s10x_var)), 6)
			if round(s10x_var/(s10x_ref + s10x_var), 6) > (0.5-2*sd) and round(s10x_var/(s10x_ref + s10x_var), 6) < (0.5+2*sd):
				t+=1

		if (s12_geno == "0/1" or s12_geno == "0|1") and (s12x_ref + s12x_var > 500):
			n+=1
			sd = round(math.sqrt(0.5*0.5/(s12x_ref + s12x_var)), 6)
			if round(s12x_var/(s12x_ref + s12x_var), 6) > (0.5-2*sd) and round(s12x_var/(s12x_ref + s12x_var), 6) < (0.5+2*sd):
				t+=1

f_in.close()
f_out = open("fixation.txt", "w")
f_out.write("t:\t{}\nn:\t{}\npercentage:\t{}\n".format(t,n,round(t/n,6)))
f_out.close()
