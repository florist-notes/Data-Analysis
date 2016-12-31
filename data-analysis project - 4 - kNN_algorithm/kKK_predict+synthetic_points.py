import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

''' add the functions and libraries from previous programmes '''

def knn_predict(p,points,outcomes,k=5):
    ind=find_nearest_neighbours(p,points,k)
    return majority_vote(outcomes[ind])

outcomes=np.array([0,0,0,0,1,1,1,1,1])
knn_predict(np.array([2.5,2.7]),points,outcomes,k=2)

def generate_synth_data(n=50):
    points = np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))),axis=0)
    outcomes = np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return (points,outcomes)

n=20
plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.show()
