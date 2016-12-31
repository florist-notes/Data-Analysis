import numpy as np
def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2-p1,2))) #distance between two points
p1 = np.array([1, 1])   #coordinate x=1,y=1
p2 = np.array([4, 4])   #coordinate x=4,y=4
distance(p1,p2)
