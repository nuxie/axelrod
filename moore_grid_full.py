from abc import ABC
from grid import Grid


class MooreGridFull(Grid, ABC):

    def neighbours(self, n):
        self_size_sq = self.size ** 2
        if n == 0:  # top left
            nb = [self.cells[self_size_sq - 1],
                  self.cells[self_size_sq - self.size],
                  self.cells[self_size_sq - self.size + 1],
                  self.cells[self.size - 1],
                  self.__n5(n),
                  self.cells[self.size * 2 - 1],
                  self.__n7(n),
                  self.__n8(n)]
        elif n == self.size - 1:  # top right
            nb = [self.cells[self_size_sq - 2],
                  self.cells[self_size_sq - 1],
                  self.cells[self_size_sq - self.size],
                  self.__n4(n),
                  self.cells[0],
                  self.__n6(n),
                  self.__n7(n),
                  self.cells[self.size]]
        elif n == self_size_sq - self.size:  # bottom left
            nb = [self.cells[self_size_sq - self.size - 1],
                  self.__n2(n),
                  self.__n3(n),
                  self.cells[self_size_sq - 1],
                  self.__n5(n),
                  self.cells[self.size - 1],
                  self.cells[0],
                  self.cells[1]]
        elif n == self_size_sq - 1:  # bottom right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.cells[self_size_sq - 2 * self.size],
                  self.__n4(n),
                  self.cells[self_size_sq - self.size],
                  self.cells[self.size - 2],
                  self.cells[self.size - 1],
                  self.cells[0]]
        elif n < self.size:  # top
            nb = [self.__n1(self_size_sq + n),
                  self.__n2(self_size_sq + n),
                  self.__n3(self_size_sq + n),
                  self.__n4(n),
                  self.__n5(n),
                  self.__n6(n),
                  self.__n7(n),
                  self.__n8(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n1(n + self.size),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n + self.size),
                  self.__n5(n),
                  self.__n6(n + self.size),
                  self.__n7(n),
                  self.__n8(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n - self.size),
                  self.__n4(n),
                  self.__n5(n - self.size),
                  self.__n6(n),
                  self.__n7(n),
                  self.__n8(n - self.size)]
        elif n >= self_size_sq - self.size:  # bottom
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n),
                  self.__n5(n),
                  self.__n6(n - self_size_sq),
                  self.__n7(n - self_size_sq),
                  self.__n8(n - self_size_sq)]
        else:
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n),
                  self.__n5(n),
                  self.__n6(n),
                  self.__n7(n),
                  self.__n8(n)]
        return nb

    def neighbours_indices(self, n):
        self_size_sq = self.size ** 2
        if n == 0:  # top left
            nb = [self_size_sq - 1,
                  self_size_sq - self.size,
                  self_size_sq - self.size + 1,
                  self.size - 1,
                  self.__n5_index(n),
                  self.size * 2 - 1,
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n == self.size - 1:  # top right
            nb = [self_size_sq - 2,
                  self_size_sq - 1,
                  self_size_sq - self.size,
                  self.__n4_index(n),
                  0,
                  self.__n6_index(n),
                  self.__n7_index(n),
                  self.size]
        elif n == self_size_sq - self.size:  # bottom left
            nb = [self_size_sq - self.size - 1,
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self_size_sq - 1,
                  self.__n5_index(n),
                  self.size - 1,
                  0,
                  1]
        elif n == self_size_sq - 1:  # bottom right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self_size_sq - 2 * self.size,
                  self.__n4_index(n),
                  self_size_sq - self.size,
                  self.size - 2,
                  self.size - 1,
                  0]
        elif n < self.size:  # top
            nb = [self.__n1_index(self_size_sq + n),
                  self.__n2_index(self_size_sq + n),
                  self.__n3_index(self_size_sq + n),
                  self.__n4_index(n),
                  self.__n5_index(n),
                  self.__n6_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n1_index(n + self.size),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n + self.size),
                  self.__n5_index(n),
                  self.__n6_index(n + self.size),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n - self.size),
                  self.__n4_index(n),
                  self.__n5_index(n - self.size),
                  self.__n6_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n - self.size)]
        elif n >= self_size_sq - self.size:  # bottom
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n),
                  self.__n5_index(n),
                  self.__n6_index(n - self_size_sq),
                  self.__n7_index(n - self_size_sq),
                  self.__n8_index(n - self_size_sq)]
        else:
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n),
                  self.__n5_index(n),
                  self.__n6_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        return nb

    def __n1(self, n):
        return self.cells[self.__n1_index(n)]

    def __n2(self, n):
        return self.cells[self.__n2_index(n)]

    def __n3(self, n):
        return self.cells[self.__n3_index(n)]

    def __n4(self, n):
        return self.cells[self.__n4_index(n)]

    def __n5(self, n):
        return self.cells[self.__n5_index(n)]

    def __n6(self, n):
        return self.cells[self.__n6_index(n)]

    def __n7(self, n):
        return self.cells[self.__n7_index(n)]

    def __n8(self, n):
        return self.cells[self.__n8_index(n)]

    def __n1_index(self, n):
        return n - self.size - 1

    def __n2_index(self, n):
        return n - self.size

    def __n3_index(self, n):
        return n - self.size + 1

    def __n4_index(self, n):
        return n - 1

    def __n5_index(self, n):
        return n + 1

    def __n6_index(self, n):
        return n + self.size - 1

    def __n7_index(self, n):
        return n + self.size

    def __n8_index(self, n):
        return n + self.size + 1

