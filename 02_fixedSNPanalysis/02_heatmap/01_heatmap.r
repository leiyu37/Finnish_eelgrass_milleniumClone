#!/usr/bin/env Rscript
library(vcfR)
library(poppr)
library(ggplot2)
vcf <- read.vcfR("somaticMutation_nh.vcf")
aa.genlight <- vcfR2genlight(vcf, n.cores=1)
ploidy(aa.genlight) <- "2"

distance <- bitwise.dist(aa.genlight, percent = FALSE, mat = TRUE)
write.table(distance, file = "distance.matrix.txt", quote = FALSE, sep = "\t")

#prepare the data with a pythons script ./prepareData.py


obj <- read.table("distance.ggplot2.txt")
pdf("HeatMAP.pdf",width=8,height=8)
ggplot(data = obj, aes(x=V1, y=V2, fill=V3)) +
  geom_tile() +
  ylab("") +
  xlab("") +
  scale_fill_gradient2(low = "blue", high = "red", name = "Genetic\ndistance") +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1))
dev.off()
