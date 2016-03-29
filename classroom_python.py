from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer
import numpy
import matplotlib.pyplot as plt

## read data
Y = open('YData.txt','r')
X = open('XData.txt','r')
Y_temp = Y.read().split('\r\n')
X_temp = X.read().split('\t')
SI = []
Xdata = []
Y_temp.remove('')
n = 0
SPL = []
SNR = []
RT = []
G = []
BN = []
for dataY in Y_temp:
	SI.append(float(dataY))
for data in X_temp:
	T = data.split('\r\n')
	Xdata.append(float(T[0]))
	if '' in T:
		T.remove('')
	if len(T) == 2:
		Xdata.append(float(T[1]))
for dataX in Xdata:
	if n % 5 == 0:
		SPL.append(Xdata[n])
	elif n % 5 == 1:
		SNR.append(Xdata[n])
	elif n % 5 == 2:
		RT.append(Xdata[n])
	elif n % 5 == 3:
		G.append(Xdata[n])
	else:
		BN.append(Xdata[n])
	n = n + 1
	X_input = numpy.reshape(Xdata,(991,5))

Y.close()
X.close()
##
#print X_input[1][:]

#neural network, seems not working,may be not converge
#'''
ds = SupervisedDataSet(5,1)
net = buildNetwork(5, 6, 1, bias = True, hiddenclass = TanhLayer)

for count in range(0,990):
	ds.addSample(X_input[count][:],SI[count])

trainer = BackpropTrainer(net, ds)
errors = trainer.trainUntilConvergence(verbose = True, maxEpochs = 5000)

Y_test = []
snr = 10
t60 = 1
G = 0

for Ls in range(40, 110):
	XX = [Ls, snr, t60, G , Ls - snr]
	Y_test.append(net.activate(XX))
	

plt.figure()
#ax.scatter(y, predicted)
plt.plot(range(40, 110), Y_test, 'k--',lw = 4)
#ax.set_xlabel('Measured')
#ax.set_ylabel('Predicted')
plt.show()
#'''

