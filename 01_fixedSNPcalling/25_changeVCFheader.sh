#!/bin/bash
# old_new.txt is stored in data folder
bcftools reheader -s old_new.txt \
-o somaticMutation_nh.vcf \
somaticMutation.vcf
