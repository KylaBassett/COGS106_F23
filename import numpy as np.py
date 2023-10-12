import numpy as np
import pandas as pd
data = pd.read_csv("ReactionTimeData.csv")
data.keys()

from numpy import random 

subject = data ['Subject']
subject = np.array(subject)