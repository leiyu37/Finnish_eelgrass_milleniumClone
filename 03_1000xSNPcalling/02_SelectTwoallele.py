#!/usr/bin/env python3

f_in = open("s8x_mutect_snp.vcf")
f_out = open("03_s8x_twoAllele.vcf", "w")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            f_out.write(line)
    else:
        f_out.write(line)
f_out.close()
f_in.close()


f_in = open("s10x_mutect_snp.vcf")
f_out = open("03_s10x_twoAllele.vcf", "w")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            f_out.write(line)
    else:
        f_out.write(line)
f_out.close()
f_in.close()




f_in = open("s12x_mutect_snp.vcf")
f_out = open("03_s12x_twoAllele.vcf", "w")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            f_out.write(line)
    else:
        f_out.write(line)
f_out.close()
f_in.close()

#vcftools --vcf 03_s8x_twoAllele.vcf --out 04_s8x_rmGametic --recode --exclude-positions /sfs/fs1/work-geomar/smomw353/gatk_add1000x/01_finalCheck/03_gameticDiff/gametic.pos
#vcftools --vcf 03_s10x_twoAllele.vcf --out 04_s10x_rmGametic --recode --exclude-positions /sfs/fs1/work-geomar/smomw353/gatk_add1000x/01_finalCheck/03_gameticDiff/gametic.pos
#vcftools --vcf 03_s12x_twoAllele.vcf --out 04_s12x_rmGametic --recode --exclude-positions /sfs/fs1/work-geomar/smomw353/gatk_add1000x/01_finalCheck/03_gameticDiff/gametic.pos
#./02_mutect_DPaAF.py
