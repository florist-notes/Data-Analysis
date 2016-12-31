import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv") #make sure,you are in the right directory , check (>>>pwd)

# >>>birddata.info() #look at basic info abot the data frame
# >>>birddata.head() #look for first 5 rows in the data set
# >>>birddata.tail() #look for last 5 rows in the data set

bird_names = pd.unique(birddata.bird_name) #look at the unique names of the birds in the csv_file
# >>>print(bird_name)

ix = birddata.bird_name == "Eric" #storing the indices of the bird Eric
x,y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize = (7,7))
plt.plot(x,y,"b.")
# >>>plt.show() #if you want to check trajectory of "Eric" only

''' To look at all the birds trajectories, we plot each bird in the same plot '''
plt.figure(figsize = (7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name  #storing the indices of the bird Eric
    x,y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()
