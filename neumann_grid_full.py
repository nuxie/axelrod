from abc import ABC
from grid import Grid


class NeumannGridFull(Grid, ABC):
    def neighbours(self, n):
        self_size_sq = self.size ** 2
        if n == 0:  # top left
            nb = [self.cells[self_size_sq - self.size],
                  self.cells[self.size - 1],
                  self.__n3(n),
                  self.__n4(n)]
        elif n == self.size - 1:  # top right
            nb = [self.cells[self_size_sq - 1],
                  self.__n2(n),
                  self.cells[0],
                  self.__n4(n)]
        elif n == self.size * (self.size - 1):  # bottom left
            nb = [self.__n1(n),
                  self.cells[self_size_sq - 1],
                  self.__n3(n),
                  self.cells[0]]
        elif n == self.size ** 2 - 1:  # bottom right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.cells[self_size_sq - self.size],
                  self.cells[self.size - 1]]
        elif n < self.size:  # top
            nb = [self.__n1(self_size_sq + n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n1(n),
                  self.__n2(n + self.size),
                  self.__n3(n),
                  self.__n4(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n - self.size + 2),
                  self.__n4(n)]
        elif n >= self.size * (self.size - 1):  # bottom
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n - self_size_sq)]
        else:
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n)]
        return nb

    def neighbours_indices(self, n):
        self_size_sq = self.size ** 2
        if n == 0:  # top left
            nb = [self_size_sq - self.size,
                  self.size - 1,
                  self.__n3_index(n),
                  self.__n4_index(n)]
        elif n == self.size - 1:  # top right
            nb = [self_size_sq - 1,
                  self.__n2_index(n),
                  0,
                  self.__n4_index(n)]
        elif n == self.size * (self.size - 1):  # bottom left
            nb = [self.__n1_index(n),
                  self_size_sq - 1,
                  self.__n3_index(n),
                  0]
        elif n == self.size ** 2 - 1:  # bottom right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self_size_sq - self.size,
                  self.size - 1]
        elif n < self.size:  # top
            nb = [self.__n1_index(self_size_sq + n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n1_index(n),
                  self.__n2_index(n + self.size),
                  self.__n3_index(n),
                  self.__n4_index(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n - self.size + 2),
                  self.__n4_index(n)]
        elif n >= self.size * (self.size - 1):  # bottom
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n - self_size_sq)]
        else:
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n)]
        return nb

    def __n1(self, n):
        return self.cells[self.__n1_index(n)]

    def __n2(self, n):
        return self.cells[self.__n2_index(n)]

    def __n3(self, n):
        return self.cells[self.__n3_index(n)]

    def __n4(self, n):
        return self.cells[self.__n4_index(n)]

    def __n1_index(self, n):
        return n - self.size

    def __n2_index(self, n):
        return n - 1

    def __n3_index(self, n):
        return n + 1

    def __n4_index(self, n):
        return n + self.size
