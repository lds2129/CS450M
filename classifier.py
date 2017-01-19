from sklearn import datasets
from sklearn.cross_validation import train_test_split
from random import randint


class KNNClassifier():
    def __init__(self, iris):
        self.prediction = []
        self.distances = []
        self.train_data, self.test_data, self.train_target, self.test_target = train_test_split(iris.data, iris.target,
                                                                                                test_size=0.7,
                                                                                                random_state=randint(0,
                                                                                                                     1000))

    def fit(self):
        # Nothing is going to happen in first week
        pass

    # result of the predict
    def classify(self, key):
        count = [0, 0, 0]
        for t in key:
            count[t] += 1
        return count.index(max(count))

    def predict(self, k=3):
        for r in self.test_data:
            self.distances.append(self.getDistances(r, k))
        self.compareData()

    def getDistances(self, item, k=3):
        distances = []
        for row in range(len(self.train_data)):
            temp = 0
            for col in range(len(self.train_data[row])):
                temp += ((item[col] - self.train_data[row][col])**2)
                distances.append((temp, row))
        distances.sort()
        return distances[:k]

    # calculate the prediction data
    def compareData(self):
        for item in self.distances:
            temp = []
            for row in item:
                temp.append(self.train_target[row[1]])
            self.prediction.append(self.classify(temp))

    def computeResult(self):
        count = 0.0
        for x in range(len(self.test_target)):
            if (self.prediction[x] == self.test_target[x]):
                count += 1
        percent = count / len(self.test_target) * 100
        modifiedPercent = round(percent, 2)
        return modifiedPercent

classifier = KNNClassifier(datasets.load_iris())
classifier.predict(3)
print(classifier.distances)
print(classifier.prediction)
print("Accuracy is: " + str(classifier.computeResult()) + "%")