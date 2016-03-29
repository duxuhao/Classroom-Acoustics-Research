library(e1071)
X <- XData
Y <- YData
samplesize <- 991
TrainX <- sample(1:samplesize,round(samplesize*0.8))
TestX <- setdiff(1:samplesize,TrainX)

for (D in 2:8){
  for (C in 0:20){
    SI <- svm(X[TrainX ,],Y[TrainX ,],type = 'eps',kernel = 'polynomial',degree =  D, cost = C*5+1)
    SVMTrain <- predict(SI,X[TrainX ,])
    name <- paste('Trsvm_',D,'_',C,'.txt')
    write.table(SVMTrain, file = name)
    SVMTest <- predict(SI,X[TestX ,])
    name <- paste('Tesvm_',D,'_',C,'.txt')
    write.table(SVMTest, file = name)
    name <- paste('TeYsvm_',D,'_',C,'.txt')
    write.table(Y[TestX ,], file = name)
    SVMPredict <- predict(SI,XT)
    name <- paste('Psvm_',D,'_',C,'.txt')
    write.table(SVMPredict, file = name)    
  }
}