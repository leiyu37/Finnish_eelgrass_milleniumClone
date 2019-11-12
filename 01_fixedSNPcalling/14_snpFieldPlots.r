#!/usr/bin/env Rscript
library(ggplot2)
Rtable_sm_snp <- read.table("Rtable_add1000x_snp.txt", header = TRUE)


pdf("add1000x_snp_QD.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=QD)) + geom_density()
dev.off()

pdf("add1000x_snp_FS.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=FS)) + geom_density() + scale_x_continuous(trans='log10')
dev.off()


pdf("add1000x_snp_SOR.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=SOR)) + geom_density() + xlim(0,10)
dev.off()

pdf("add1000x_snp_MQ.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=MQ)) + geom_density() + xlim(0,70)
dev.off()

pdf("add1000x_snp_MQRankSum.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=MQRankSum)) + geom_density() + xlim(-11,6)
dev.off()

pdf("add1000x_snp_ReadPosRankSum.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=ReadPosRankSum)) + geom_density() + xlim(-5,5)
dev.off()

pdf("add1000x_snp_DP.pdf",width=6,height=4,paper='special') 
ggplot(Rtable_sm_snp, aes(x=DP)) + geom_histogram(binwidth = 100) + xlim(0,20000) + geom_vline(xintercept = 4000)
dev.off()
