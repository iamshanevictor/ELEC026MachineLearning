import numpy as np
from euclid import euclidean_distance, get_neighbors

X = [[2.7810836, 2.550537003],
     [1.465489372, 2.362125076],
     [3.396561688, 4.400293529],
     [1.38807019, 1.850220317],
     [3.06407232, 3.005305973],
     [7.627531214, 2.759262235],
     [5.332441248, 2.088626775],
     [6.922596716, 1.77106367],
     [8.675418651, -0.242068655],
     [7.673756466, 3.508563011]]

y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def predict(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

test_set = [float(np.random.randint(1, 10)), float(np.random.randint(1, 10))]

prediction = predict(X, test_set, 3)

print(test_set)
print(round(prediction,1))
