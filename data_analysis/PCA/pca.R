df <- read.csv('/media/valentin/Data/SR/data/input4R.csv')

# remove cols with all zeros
df1 <- df[, colSums(df != 0) > 0]
str(df1)
pca <- prcomp(df1[, 2:58432], scale=T)

# correlation between Class and PC
cor(df1$Class, pca$x[,1])

#VISUALISATION
# How many conponents should we choose?
std_dev <- pca$sdev
vari <- std_dev^2
prop_varex <- vari/sum(vari)
prop_varex[1:307]
# 230 components - 90%, 307 components - 96%
plot(prop_varex[1:30], xlab =  "Principal Component",
     ylab = "Proportion of Variance Explained",
     type = "b")

library(ggfortify)
autoplot(pca, data = df, colour = 'Class')

str(pca$x)
pca$x[1:10, 1:10]
write.table(pca$x,file="pca_x.txt", sep="\t")
