#!/usr/bin/env python3
# extract somatic mutations.
# cat somaticMutation.vcf | awk '/^LFYR/ {print}' | wc -l #7054

f_in = open("sm_only80x.recode.vcf")
f_out = open("somaticMutation.vcf", "w")
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		hr = 0
		hv = 0
		het = 0
		for i in range(9, len(columns)):
			genotype = columns[i].split(":")[0]
			if genotype == "0/0" or genotype == "0|0" :
				hr += 1
			elif genotype == "1/1" or genotype == "1|1" :
				hv += 1
			elif genotype == "0/1" or genotype == "0|1" :
				het +=1
		t = hr + hv + het
		if not (hr == t or hv == t or het == t):
			f_out.write(line)
	else:
		f_out.write(line)
f_in.close()
f_out.close()
