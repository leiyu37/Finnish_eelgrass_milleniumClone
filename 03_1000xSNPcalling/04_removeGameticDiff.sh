#!/bin/bash
vcftools --vcf 03_s8x_twoAllele.vcf --out 04_s8x_rmGametic --recode --exclude-positions gametic.pos
vcftools --vcf 03_s10x_twoAllele.vcf --out 04_s10x_rmGametic --recode --exclude-positions gametic.pos
vcftools --vcf 03_s12x_twoAllele.vcf --out 04_s12x_rmGametic --recode --exclude-positions gametic.pos
