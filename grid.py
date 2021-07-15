from abc import ABC, abstractmethod
import random


class Grid(ABC):
    def __init__(self, size, cells):
        self.size = size
        self.cells = cells
        if len(self.cells) != self.size ** 2:
            raise ValueError

    @abstractmethod
    def neighbours(self, n):
        pass

    @abstractmethod
    def neighbours_indices(self, n):
        pass

    def random_neighbour(self, n):
        neighbours = self.neighbours(n)
        neighbours_ind = self.neighbours_indices(n)
        ind = random.randrange(len(neighbours))
        return neighbours_ind[ind], neighbours[ind]

    def neighbours_same(self, n):
        neighbours = self.neighbours(n)
        for x in neighbours:
            if x.culture_id != self.cells[n].culture_id:
                return False
        return True

    def cultures(self):
        return set(tuple(a.culture) for a in self.cells)

    def distinct_cultures(self):
        return len(self.cultures())

    def culture_size_stats(self):
        cultures = {}
        for a in self.cells:
            cultures.setdefault(tuple(a.culture), 0)
            cultures[tuple(a.culture)] += 1
        sizes = list(cultures.values())
        avg_culture_size = round(sum(sizes) / len(sizes), 2)
        max_culture_size = max(cultures.values())
        return avg_culture_size, max_culture_size
