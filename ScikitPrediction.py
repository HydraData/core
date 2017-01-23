import TreeWrapper as tw

tw.build_tree("ProfileDataset", "save_money")

print("I see... If I am to rate your money saving skills from 1 to 5 I would give you " + str(tw.clf.predict([[0, 0,1,19,0]])))

