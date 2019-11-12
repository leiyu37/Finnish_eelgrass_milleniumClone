#!/usr/bin/env Rscript
library(ggplot2)
data <- read.table("number_Het_modules.txt", header = TRUE)

#pdf("no_het.pdf", width = 3, height = 3)
setEPS()
postscript("singleClone.eps",height = 4, width = 4)
ggplot(data, aes(noHet))+
  geom_histogram(binwidth = 1) +
  xlab("Number of heterozygous modules") +
  ylab("Number of loci") +
  scale_y_continuous(labels = scales::comma) +
  #xlim(0, 25) +
  theme(aspect.ratio = 1) +
  theme_classic()
dev.off()


setEPS()
postscript("singleClone_part.eps",height = 4, width = 4)
#pdf("no_het_zoomin.pdf", width = 6, height = 6)
ggplot(data, aes(noHet))+
  geom_histogram(binwidth = 1) +
  xlab("Number of heterozygous modules") +
  ylab("Number of loci") +
  scale_y_continuous(labels = scales::comma) +
  xlim(0, 11) +
  theme(aspect.ratio = 1) +
  theme_classic()
dev.off()
