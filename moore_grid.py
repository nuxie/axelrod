from abc import ABC
from grid import Grid


class MooreGrid(Grid, ABC):

    def neighbours(self, n):
        if n == 0:  # top left
            nb = [self.__n5(n),
                  self.__n7(n),
                  self.__n8(n)]
        elif n == self.size - 1:  # top right
            nb = [self.__n4(n),
                  self.__n6(n),
                  self.__n7(n)]
        elif n == self.size * (self.size - 1):  # bottom left
            nb = [self.__n2(n),
                  self.__n3(n),
                  self.__n5(n)]
        elif n == self.size ** 2 - 1:  # bottom right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n4(n)]
        elif n < self.size:  # top
            nb = [self.__n4(n),
                  self.__n5(n),
                  self.__n6(n),
                  self.__n7(n),
                  self.__n8(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n2(n),
                  self.__n3(n),
                  self.__n5(n),
                  self.__n7(n),
                  self.__n8(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n4(n),
                  self.__n6(n),
                  self.__n7(n)]
        elif n >= self.size * (self.size - 1):  # bottom
            nb = [self.__n1(n),
                  self.__n2(n),
                  self.__n3(n),
                  self.__n4(n),
                  self.__n5(n)]
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
        if n == 0:  # top left
            nb = [self.__n5_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n == self.size - 1:  # top right
            nb = [self.__n4_index(n),
                  self.__n6_index(n),
                  self.__n7_index(n)]
        elif n == self.size * (self.size - 1):  # bottom left
            nb = [self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n5_index(n)]
        elif n == self.size ** 2 - 1:  # bottom right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n4_index(n)]
        elif n < self.size:  # top
            nb = [self.__n4_index(n),
                  self.__n5_index(n),
                  self.__n6_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n % self.size == 0:  # left
            nb = [self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n5_index(n),
                  self.__n7_index(n),
                  self.__n8_index(n)]
        elif n % self.size == self.size - 1:  # right
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n4_index(n),
                  self.__n6_index(n),
                  self.__n7_index(n)]
        elif n >= self.size * (self.size - 1):  # bottom
            nb = [self.__n1_index(n),
                  self.__n2_index(n),
                  self.__n3_index(n),
                  self.__n4_index(n),
                  self.__n5_index(n)]
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
