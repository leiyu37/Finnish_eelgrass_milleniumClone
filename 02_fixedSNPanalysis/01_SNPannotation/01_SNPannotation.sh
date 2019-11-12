#!/bin/bash
java -Xmx4g -jar directory_for_snpEff/snpEff.jar \
-c directory_for_configFile/snpEff.config \
-v zm somaticMutation_nh.vcf > ann_somaticMutation.vcf
