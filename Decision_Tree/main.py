training = open("training.txt", "r").read()
testing = open("testing.txt", "r").read()
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
d = DecisionTreeClassifier()
d.fit(training)