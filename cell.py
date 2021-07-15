import random


class Cell:
    def __init__(self, traits, features, max_weight):
        self.culture = []
        self.weights = []
        for i in range(features):
            self.culture.append(
                random.choice([j for j in range(1, traits + 1)]))
            self.weights.append(random.uniform(0.01, max_weight))
        self.culture_id = int(''.join(str(x) for x in self.culture))

    def update_feature(self, feature, trait):
        self.culture[feature] = trait
        self.culture_id = int(''.join(str(x) for x in self.culture))

    def similarity(self, neighbour):
        counter = 0
        for i in range(len(self.culture)):
            if neighbour.culture[i] == self.culture[i]:
                counter += 1
        return counter / len(self.culture)
