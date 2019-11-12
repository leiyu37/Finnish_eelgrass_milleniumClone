#!/bin/bash
# mark duplicates

gatk --java-options "-Xmx10G" MarkDuplicates \
-I H05087-L1_S1_L001_sort.bam \
-O H05087-L1_S1_L001_markdup.bam \
-M H05087-L1_S1_L001_metrics.txt \
-MAX_FILE_HANDLES 1000
