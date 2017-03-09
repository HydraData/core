import TreeWrapper as tw

tw.build_tree("german_credit.csv", "Creditability")

print(str(tw.clf.predict([[1,30,2,2,6350,5,5,4,3,1,4,2,31,3,2,1,3,1,1,1]])))

