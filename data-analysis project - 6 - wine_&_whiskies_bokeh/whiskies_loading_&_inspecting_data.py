import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
# >>>whisky.head()  #iloc method to index a data frame by location.

# >>>whisky.iloc[0:10] #we specified the rows from 0 - 9
# >>>whisky.iloc[0:10,0:5] #we specified the rows from 0 - 9 & columns from 0-5

# >>>whisky.columns
flavors=whisky.iloc[:,2:14]

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)
