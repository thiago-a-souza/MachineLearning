'''
AUTHOR:
 Thiago Alexandre Domingues de Souza

LANGUAGE:
 Python3

INPUT:
 The input file should have the following format. The first line consists of an integer representing the k nearest neighbors.
 On the second line, two coordinates x and y represent the test data. On the third line, an integer n represents
 number of items in the training set. Then follow n lines, each of them consisting of two numbers xt and yt, representing
 the training coordinates and the corresponding category.

OUTPUT:
 A single line representing the most voted class around the k-nearest neighbors.

FORMAT:
k
x y
n
xt yt category

SAMPLE INPUT:
2
250 250
8
1 2 one
1 3 one
1 5 one
1 6 one
1 7 one
1 8 one
200 200 two
200 201 two

SAMPLE OUTPUT:
two
'''


class KNN():
    def squared_distance(self, a, b):
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

    def classify(self, k, training, test):
        # sorting training set by distance
        # training = ((x, y), category)
        sorted_by_distance = sorted(training, key=lambda p: self.squared_distance(p[0], test))

        # class_votes is a dictionary of {category, frequency}
        class_votes = {}

        # counting votes from k nearest neighbors
        for val in sorted_by_distance[:k]:
            if val[1] in class_votes:
                class_votes[val[1]] += 1
            else:
                class_votes[val[1]] = 1

        # sorting class_votes, so more voted classes appear first
        result = sorted(class_votes, key=class_votes.get, reverse=True)

        # return the first most voted class
        return result[0]


k = int(input())
x, y = map(float, input().split())

n = int(input())

training = []
for i in range(0, n):
    xt, yt, category = input().split()
    training.append(((float(xt), float(yt)), category))

knn = KNN()

print("Test example:", (x,y))
print("k:", k)
print("Category:", knn.classify(k, training, (x,y)))


