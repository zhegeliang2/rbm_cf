#coding:utf-8

#使用Metropolis-Hastings， 采样正太分布
import numpy as np
import math
from numpy import linalg as la
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import time

mu,sig,N = 0,1,1000000
pts = []

def q(x):
    return (1/(math.sqrt(2*math.pi*sig**2)))*(math.e**(-((x-mu)**2)/(2*sig**2)))

def metropolis(N):
    #初始值x0
    r = np.zeros(1)
    p = q(r[0])
    pts = []
    
    for i in range(N):
        #建议分布是均匀分布，使用这个分布的好处是aij=min{1, (q_ji*p_j/q_ij*p_i)}，其中q_ij和q_ji在建议分布中是相等的，因此aij仅仅是aij=min{1, p_j/p_i}
        #下一节点j
        rn = r + np.random.uniform(-1,1)
        #pj
        pn = q(rn[0])
        #如果p_j/p_i是1，接受转移
        if pn >= p:
            p = pn
            r = rn
        else:
            #否则，以一定概率接受
            u = np.random.rand()
            if u < pn/p:
                p = pn
                r = rn
        pts.append(r)
    
    pts = np.array(pts)
    return pts
    
b=metropolis(N)
plt.hist(b, bins=1000) 
plt.show()
