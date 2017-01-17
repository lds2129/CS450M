from sklearn import datasets
from sklearn.cross_validation import train_test_split

# side note: it does not work with scikit 18.0 version.
# need to figure out different importation might work similar to cross_validation.
# This would be the another option  ====>  from sklearn.model_selection import train_test_split
'''
>>> clf = svm.SVC(kernel='linear', C=100)
>>> scores = cross_validation.cross_val_score(
...    clf, iris.data, iris.target, cv=5)
...
>>> scores
array([ 1.  ...,  0.96...,  0.9 ...,  0.96...,  1.  ...])
'''


'''
>>> from sklearn import metrics
>>> cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5,
...     score_func=metrics.f1_score)
...
array([ 1.  ...,  0.96...,  0.89...,  0.96...,  1.  ...])
'''
from random import randint
import HardCodedClassifier

iris = datasets.load_iris()
# Show the data (the attributes of each instance)
print(iris.data)

# Show the target values (in numeric format) of each instance
print(iris.target)

# Show the actual target names that correspond to each number
print(iris.target_names)

X, Y = iris.data, iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.7, random_state=randint(0, 1000))


# declared compare function
def match(list, target_test):
    result = 0
    for i in range(len(list)):
        if (list[i] == Y_test[i]):
            result += 1
    return result


cf = HardCodedClassifier.HardCodedClassifier()
cf.fit(X_train, Y_train)
pList = cf.predict(X_test)

# get the result
result = match(pList, Y_test)

# to make answer with percentage form
answer = result / float(len(Y_test)) * 100.0

# round float number with 2 decimal points
rAnswer = round(answer, 2)
print("Accuracy: ",rAnswer, "%")
print("Test is finished!")



