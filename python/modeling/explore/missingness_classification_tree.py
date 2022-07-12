# Use a Classification Tree to automatically discover patterns in the missingness of a specified variable
import numpy as np
from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# ToDo: create target by encoding missing values as 1 and non-missing values as 0

clf = DecisionTreeClassifier(max_leaf_nodes=5, random_state=0)
clf.fit(X, y)

tree.plot_tree(clf)
plt.show()
