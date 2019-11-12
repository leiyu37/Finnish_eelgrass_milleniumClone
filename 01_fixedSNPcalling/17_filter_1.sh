#!/bin/bash

vcftools --vcf sm_add1000x_clean_snp.vcf \
    --minGQ 30 \
    --minDP 20 \
    --recode \
    --recode-INFO-all \
    --out sm_vcffilter
