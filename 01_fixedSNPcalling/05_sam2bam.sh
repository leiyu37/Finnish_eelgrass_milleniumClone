#!/bin/bash
# convert sam format file resulted from BWA to bam format.

samtools view -Sb H05087-L1_S1_L001.sam >H05087-L1_S1_L001.bam
