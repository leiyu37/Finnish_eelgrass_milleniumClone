#!/usr/bin/env python3
# obtain the coverage and variant read frequency per SNP per module.
f_in = open("04_s8x_rmGametic.recode.vcf")
f_out = open("05_s8x_DPaAF.txt", "w")
f_out.write("CHROM\tPOS\tDP\tVAR_AF\n")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            chrom = columns[0]
            pos = columns[1]
            ref_count = int(columns[10].split(":")[1].split(",")[0])
            var_count = int(columns[10].split(":")[1].split(",")[1])
            dp = ref_count + var_count
            var_af = round(var_count/dp,4)
            f_out.write("{}\t{}\t{}\t{}\n".format(chrom, pos, dp, var_af))
f_out.close()
f_in.close()


f_in = open("04_s10x_rmGametic.recode.vcf")
f_out = open("05_s10x_DPaAF.txt", "w")
f_out.write("CHROM\tPOS\tDP\tVAR_AF\n")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            chrom = columns[0]
            pos = columns[1]
            ref_count = int(columns[10].split(":")[1].split(",")[0])
            var_count = int(columns[10].split(":")[1].split(",")[1])
            dp = ref_count + var_count
            var_af = round(var_count/dp,4)
            f_out.write("{}\t{}\t{}\t{}\n".format(chrom, pos, dp, var_af))
f_out.close()
f_in.close()


f_in = open("04_s12x_rmGametic.recode.vcf")
f_out = open("05_s12x_DPaAF.txt", "w")
f_out.write("CHROM\tPOS\tDP\tVAR_AF\n")
for line in f_in.readlines():
    if line.startswith("LFYR"):
        columns = line.split("\t")
        ref_state = columns[3]
        var_state = columns[4]
        if len(ref_state) == 1 and len(var_state) == 1 and len(columns) == 11:
            chrom = columns[0]
            pos = columns[1]
            ref_count = int(columns[10].split(":")[1].split(",")[0])
            var_count = int(columns[10].split(":")[1].split(",")[1])
            dp = ref_count + var_count
            var_af = round(var_count/dp,4)
            f_out.write("{}\t{}\t{}\t{}\n".format(chrom, pos, dp, var_af))
f_out.close()
f_in.close()
