x.pca <- prcomp(XData[-1],center = TRUE,scale. = TRUE)
print(x.pca)
plot(x.pca, type = "l")
summary(x.pca)