import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric" #storing the indices of the bird Eric
speed = birddata.speed_2d[ix]
# >>>plt.hist(speed) #[F.A.I.L.S] ,since we have non numeric numbers in the speed array
# >>>plt.hist(speed[:10])  #plot a histogram using the first 10 observations of speed [works]
# >>>np.isnan(speed) #>>>np.isnan(speed).any()  #I am looking for any non number objects in the speed column using numpy's isnan function.
# >>>np.sum(np.isnan(speed)) # I find out the count of non numeric entries, False=0 & True =1 from isnan()

# >>>ind = np.isnan(speed)
# >>>plt.hist(speed[~ind]) #we will include only those entries for which ind != True

plt.figure(figsize = (8,4))
# >>>speed = birddata.speed_2d[birddata.bird_name == "Eric"] #step 5 & 6 combined
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed=True)
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()


'''
    We can also plot a similar histogram using the pandas module instead of pyplot.
    The benefit of using pandas is that we do not have to deal with NaNs explicitly.
    Instead, all of that happens under the hood.

    NaNs - Not-a-Number

    >>>birddata.speed_2d.plot(kind='hist', range=[0,30])
    >>>plt.xlabel("2D speed")
    >>>plt.savefig("hist_birdmig_speed.pdf")
'''
