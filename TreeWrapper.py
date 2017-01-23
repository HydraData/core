from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

import numpy as np
import pandas as pd

clf = tree.DecisionTreeClassifier()

def build_tree(filename, targer_column):
    risk = pd.read_csv(filename)
    #clf = DecisionTreeRegressor(max_depth=4)
    train = risk.sample(frac=0.8, random_state=1)
    test = risk.loc[~risk.index.isin(train.index)]
    columns = risk.columns.tolist()
    columns.pop()
    target = targer_column
    clf.fit(train[columns], train[target])
    #tree.export_graphviz(clf, out_file='tree.dot') Export tree if needed
    pass
