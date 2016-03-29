library(neuralnet)
traininginput <- XData
trainingoutput <- YData
trainingdata <- cbind(traininginput,trainingoutput)
colnames(trainingdata) <- c("SPL","SNR","RT","G","BN","SI")
for (n in 20:24){
  for (t in 1:10){
    net.SI <- neuralnet(SI~SPL+SNR+RT+G+BN,trainingdata, hidden=n,threshold=t/100,stepmax = 1e+6)
    #plot(net.SI)
    net.result <- compute(net.SI,XData)
    name <- paste('NN',n,'_',t,'.txt')
    write.table(net.result, file = name)
    #ls(net.result)
    #print(net.result$net.result)
  }
}

