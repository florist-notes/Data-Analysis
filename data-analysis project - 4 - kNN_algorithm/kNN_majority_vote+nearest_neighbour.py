import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

points=np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p=np.array([2.5,2])

def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
           vote_counts[vote]+=1
        else:
            vote_counts[vote]=1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)    #returns winner randomly if there are more than 1 winner

# >>>votes=[1,2,3,2,2,3,1,1,1,2,3,1,1,1,2,3,3,3,2,2,2,3,2,3,1,1,2] #sample vote counts
# >>>vote_counts=majority_vote(votes)
def majority_vote_short(votes):
    mode,count = ss.mstats.mode(votes)
    return mode

def find_nearest_neighbours(p,points,k=5):  #algorithm to find the nearest neighbours
    distances=np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i]=distance(p,points[i])
    ind = np.argsort(distances)            #returns index,according to sorted values in array
    return ind[:k]

ind=find_nearest_neighbours(p,points,2);print(points[ind]) #gives the nearest neighbour's for this sample case

plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1], "bo")
plt.axis([0.5,3.5,0.5,3.5])
plt.show()
