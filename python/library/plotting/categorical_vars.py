#!/usr/bin/env python

# http://seaborn.pydata.org/tutorial/categorical.html

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

fig,axarray = plt.subplots(1,1,figsize=[15,10],sharey="row",sharex="col") 


sns.boxplot(x="day", y="total_bill", hue="time", data=tips)

sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
              palette={"male": "g", "female": "m"},
              markers=["^", "o"], linestyles=["-", "--"])
            
sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips);

plt.show()