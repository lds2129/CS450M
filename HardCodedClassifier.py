class HardCodedClassifier():
    def fit(self, train_data, train_target):
        # Nothing is going to happen in first week
        return 0
    def classify(self, row):
        return 0

    def predict(self, test_data):
        list = []
        for r in test_data:
            result = self.classify(r)
            list.append(result)
        return list