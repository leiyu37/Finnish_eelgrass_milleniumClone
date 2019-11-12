#!/bin/bash
# trim and filtering raw reads with trimmomatic-0.36
java -jar my_directory_for_trimmomatic/trimmomatic-0.36.jar \
PE H05087-L1_S1_L001_R1_001.fastq.gz \
H05087-L1_S1_L001_R2_001.fastq.gz \
H05087-L1_S1_L001_f_p.fq.gz \
H05087-L1_S1_L001_f_up.fq.gz \
H05087-L1_S1_L001_r_p.fq.gz \
H05087-L1_S1_L001_r_up.fq.gz \
ILLUMINACLIP:my_directory_for_adaptors/TruSeq3-PE-2.fa:2:30:10 \
LEADING:20 \
TRAILING:20 \
SLIDINGWINDOW:3:15 \
MINLEN:36
