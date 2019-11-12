#!/bin/bash
# mapping the clean reads against reference genome
bwa mem -R "@RG\tID:L001\tSM:H05087-L1_S1_L001\tPL:illumina\tLB:CGTGAT\tPU:unit" \
-M zm_v21 \
H05087-L1_S1_L001_f_p.fq \
H05087-L1_S1_L001_r_p.fq >H05087-L1_S1_L001.sam
