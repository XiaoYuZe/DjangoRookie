from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris

def creat_data(n):
	np.random.seed(1)
	x_11 = np.random.randint(0,100,(n,1))
	x_12 = np.random.randint(0,100,(n,1,))
	x_13 = 20 + np.random.randint(0,10,(n,1,))

	x_21 = np.random.randint(0,100,(n,1))
	x_22 = np.random.randint(0,100,(n,1,))
	x_23 = 10 - np.random.randint(0,10,(n,1,))	

	new_x_12 = x_12*np.sqrt(2)/2 - x_13*np.sqrt(2)/2
	new_x_13 = x_13*np.sqrt(2)/2 + x_13*np.sqrt(2)/2

	new_x_22 = x_22*np.sqrt(2)/2 - x_23*np.sqrt(2)/2
	new_x_23 = x_22*np.sqrt(2)/2 + x_23*np.sqrt(2)/2

	plus_samples = np.hstack([x_11,new_x_12,new_x_13,np.ones((n,1))])
	minus_samples = np.hstack([x_21,new_x_22,new_x_23,-np.ones((n,1))])
	samples = np.vstack([plus_samples,minus_samples])
	np.random.shuffle(samples)
	return samples

# print creat_data(2)

def plot_samples(ax,samples):
	Y = samples[:,-1]
	Y = samples[:,-1]
	position_p = Y == 1
	position_m = Y == -1
	ax.scatter(samples[position_p,0],samples[position_p,1],samples[position_p,2],marker='+',label='+',color='b')
	ax.scatter(samples[position_m,0],samples[position_m,1],samples[position_m,2],marker='^',label='-',color='y')


def hyper_plane(x,y,w,b):
	return (-w[0][0]*x-w[1][0]*y-b)/w[2][0]

	