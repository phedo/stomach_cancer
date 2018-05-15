# input data
directory <- "../data/all_data"
sampleFiles <- list.files(directory)
sampleCondition <- sub("^(.*)_.*","\\1",sampleFiles)
sampleTable <- data.frame(sampleName = sampleFiles,
                          fileName = sampleFiles,
                          condition = sampleCondition)
# for faster computation
library("DESeq2")
library("BiocParallel")
register(MulticoreParam(2))
ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable,
                                       directory = directory,
                                       design= ~ condition)
# check that condiotion is ok
colData(ddsHTSeq)

# calculate statistics
ddsHTSeq1 <- DESeq(ddsHTSeq, parallel=TRUE)

# consider all genes with padj < padj_threshold as significant 
# and choose log2 fold change threhold as lfct
padj_threshold = 0.01
for (lfct in c(2, 3, 4)){
  res <- results(ddsHTSeq1, contrast = c("condition", "cancer", "normal"), lfcThreshold = lfct, altHypothesis = c("greaterAbs"))
  print(sum(res$padj < padj_threshold, na.rm=TRUE))
  # make a subset with them
  resSig <- res[which(res$padj < padj_threshold),]
  write.table(resSig, paste("../data/all_genes_with_padj_less_0.01_threshold_", lfct, ".xls", sep = ""), sep='\t')
}

# log fold change and p-value<0.1
plotMA(res, alpha = 0.01, ylim = c(-8, 8))
# histogram of p-values
hist( res$padj, breaks=20, col="grey" )
