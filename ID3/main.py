# reading file and store it into
file = open('iris.csv', 'r')
iris_data = []
for line in file:
    iris_data.append(line.split(',', len(line)))

for x in iris_data:
    print(x)