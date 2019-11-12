#!/usr/bin/env python3
# need the gff file in the current directory
# gff annotation file: https://www.ncbi.nlm.nih.gov/genome/?term=eelgrass
import subprocess

f_log = open("01_commands_log.txt", "w")
f = open("01_categories.txt", "w")
f.write("module\ttotal\tnongene\tgene\tintron\texon\tCDS\tUTR\n")
for vcf in ["lowfreq_s08xPrivate.recode.vcf", "lowfreq_s10xPrivate.recode.vcf", "lowfreq_s12xPrivate.recode.vcf"]:
	total = 0
	f_in = open(vcf)
	for line in f_in.readlines():
		if line.startswith("LFYR"):
			total += 1
	f_in.close()
	name = vcf.split("_")[-1].split(".")[0]
	cmd10 = "java -Xmx4g -jar snpEff.jar -c snpEff.config -v zm {} > ann_{}.vcf".format(vcf,name)
	f_log.write(cmd10 + "\n")
	subprocess.call(cmd10, shell=True)
	cmd11 = "mkdir {}".format(name)
	f_log.write(cmd11 + "\n")
	subprocess.call(cmd11, shell=True)
	cmd12 = "mv snpEff_summary.html ./{}".format(name)
	f_log.write(cmd12 + "\n")
	subprocess.call(cmd12, shell=True)

	cmd01 = "bedtools intersect -b {} -a GCA_001185155.1_Zosma_marina.v.2.1_genomic.gff -wo >{}.intersect".format(vcf,name)
	f_log.write(cmd01 + "\n")
	subprocess.call(cmd01, shell=True)

	cmd02 = "cat {}.intersect | awk '$3 == \"exon\" {{{}}}' | wc -l".format(name, "print")
	f_log.write(cmd02 + "\n")
	exon = int(subprocess.getoutput(cmd02))

	cmd03 = "cat {}.intersect | awk '$3 == \"gene\" {{{}}}' | wc -l".format(name, "print")
	f_log.write(cmd03 + "\n")
	gene = int(subprocess.getoutput(cmd03))

	cmd04 = "cat {}.intersect | awk '$3 == \"CDS\" {{{}}}' | wc -l".format(name, "print")
	f_log.write(cmd04 + "\n\n")
	CDS = int(subprocess.getoutput(cmd04))

	nongene = total - gene
	intron = gene - exon
	utr = exon - CDS
	f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, total, nongene, gene, intron, exon, CDS, utr))
f.close()
f_log.close()
