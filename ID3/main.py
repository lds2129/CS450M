import numpy as np
from collections import Counter
from math import log
import operator
# reading file and store it into

file = open('loan.txt')
loan_data = []
for line in file:
    temp = line.split(',', len(line))
    loan_data.append(temp)

for x in loan_data:
    print(x)

loanAnswer = []

for answer in loan_data[0]:
    for row in answer[3]:
        loanAnswer.append(row)

for y in loanAnswer:
    print(loanAnswer)

count = [0, 0, 0, 0]



def classify(input_tree, feat_labels, test_vec):
    first_str = input_tree.keys()[0]
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    key = test_vec[feat_index]
    feat_value = second_dict[key]
    if isinstance(feat_value, dict):
        class_label = classify(feat_value, feat_labels, test_vec)
    else:
        class_label = feat_value
    return class_label



def calc_ent(data_set):
    num_entries = len(data_set)
    label_counts = {}
    # the the number of unique elements and their occurrence
    for featVec in data_set:
        current_label = featVec[-1]
        if current_label not in label_counts.keys(): label_counts[current_label] = 0
        label_counts[current_label] += 1
    ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        ent -= prob * log(prob, 2)  # log base 2
    return ent

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
