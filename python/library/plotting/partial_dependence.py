from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor

X, y = make_friedman1()

clf = GradientBoostingRegressor(n_estimators=10).fit(X, y)

fig, axs = plot_partial_dependence(clf, X, [0, (0, 1)])
