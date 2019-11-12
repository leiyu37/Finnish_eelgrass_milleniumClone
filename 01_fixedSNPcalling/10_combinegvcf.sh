#!/bin/bash
# combine all the gvcf files to one file. This includes the 80x data for all 24 modules, and 1000x data for m08, m10, and m12.

gatk --java-options "-Xmx96G" CombineGVCFs \
 -R /sfs/fs1/work-geomar/smomw353/sm_1000x/GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05087-L1_S1_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05088-L1_S2_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05089-L1_S3_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05090-L1_S4_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05091-L1_S5_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05092-L1_S6_L001.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05093-L1_S7_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05094-L1_S8_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05095-L1_S9_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05096-L1_S10_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05097-L1_S11_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05098-L1_S12_L002.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05099-L1_S13_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05100-L1_S14_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05101-L1_S15_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05102-L1_S16_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05103-L1_S17_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05104-L1_S18_L003.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05105-L1_S19_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05106-L1_S20_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05107-L1_S21_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05109-L1_S23_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/H05110-L1_S24_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/new/H05108-L1_S22_L004.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/new/s10x.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/new/s12x.g.vcf \
--variant /sfs/fs1/work-geomar/smomw353/gatk_add1000x/gvcfs/new/s8x.g.vcf \
-O sm_add1000x_merg.g.vcf
