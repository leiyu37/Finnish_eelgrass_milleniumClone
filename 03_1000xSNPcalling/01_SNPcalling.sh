#!/bin/bash
ulimit -n 60000
ulimit -a
date
hostname

gatk --java-options "-Xmx96G" Mutect2 \
   -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
   -I s8_1000x_markdup.bam \
   -I nature_markdup.bam \ #control sample is the one based on which the reference genome was constructed. 22 km distant from our studied clone.
   -normal nature \
   -O s8x_mutect2_raw.vcf \
   -bamout s8x_mutect2.bam \
   --f1r2-tar-gz s8x_f1r2.tar.gz \
   --tmp-dir /tmp

gatk --java-options "-Xmx96G" LearnReadOrientationModel \
    -O s8x_read-orientation-model.tar.gz \
    -I s8x_f1r2.tar.gz

gatk --java-options "-Xmx96G" FilterMutectCalls \
    -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
    -V s8x_mutect2_raw.vcf \
    -O s8x_MarkFiltered.vcf \
    --stats s8x_mutect2_raw.vcf.stats \
    --ob-priors s8x_read-orientation-model.tar.gz \
    --tmp-dir /tmp

gatk --java-options "-Xmx96G" SelectVariants \
    -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
    -V s8x_MarkFiltered.vcf \
    -O s8x_FilterRemoved.vcf \
    --exclude-filtered true

gatk --java-options "-Xmx96G" SelectVariants \
    -R /sfs/fs1/work-geomar/smomw353/sm_1000x/GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
    -V s8x_FilterRemoved.vcf \
    --select-type-to-include SNP \
    -O s8x_mutect_snp.vcf
