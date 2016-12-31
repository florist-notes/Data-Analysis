import pandas as pd
import matplotlib.pyplot as plt
import datetime

# >>>birddata.column  #check the columns of dataset
# >>>birddata.date_time[0:3] #check first few entries of date_time
# >>>datetime.datetime.today() #returns the current Date (yy-mm-dd) & time (h:m:s)

# >>>time_1 = datetime.datetime.today()
# >>>time_2 = datetime.datetime.today() #enter this code waiting few seconds
# >>>time_2-time_1 #you will get the measure of elapsed seconds as output,the resulting object is called date time time delta object

# >>>date_str = birddata.date_time[0]
# >>>date_str
# >>>date_str[:-3] # slices/removes the UTC +00 coordinated time stamps
# >>>datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S") #the time stamp strings from date_str are converted to datetime object to be worked upon.

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
'''
    The next step for me is to construct a panda series object
    and insert the timestamp from my Python list into that object.
    I can then append the panda series as a new column in my bird data data frame.
'''
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
# >>>birddata.timestamp[4] - birddata.timestamp[3]         #measure time difference between row 4 & 3

'''
    What I'd like to do next is to create a list that captures the amount of time
    that has elapsed since the beginning of data collection.
'''
times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time-times[0] for time in times]

#But how can we measure time in certain units, like hours or days?
# >>>elapsed_time[1000]/datetime.timedelta(days=1)  #output is the no of days have passed between these two points
# >>>len(elapsed_time) # check the length of entries
# >>>elapsed_time[19000]/datetime.timedelta(hours=1)  #output is the no of hours have passed between these two points

plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel(" Observation ")
plt.ylabel(" Elapsed time (days) ")
plt.show()
