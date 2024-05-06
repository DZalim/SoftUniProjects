from collections.abc import Iterable

from AdvancedModule.OOP.workshop_custom_list.custom_exceptions import EmptyListException


class CustomList:
    def __init__(self):
        self.__values = []

    def __check_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be of type integer")
        if index < 0:
            raise ValueError("Integer must be 0 or positive")
        if index >= len(self.__values):
            raise ValueError("Index is out of range")

    def append(self, value):
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        self.__check_index(index)
        return self.__values.pop(index)

    def get(self, index):
        self.__check_index(index)
        return self.__values[index]

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise ValueError("Value is not an iterable")

        self.__values.extend(iterable)
        return self.__values

    def insert(self, index, value):
        self.__check_index(index)
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        if not self.__values:
            raise EmptyListException("Can not pop from an empty list")
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index(self, value):
        if value not in self.__values:
            raise ValueError("Value is not in the list")
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return self.__values[:]

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self):
        data = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]

            try:
                value = self.__values[index+1]
            except IndexError:
                value = " "

            data[key] = value
        return data

    def move(self, n):

        if not isinstance(n, int) or n < 0:
            raise ValueError("Value is not a valid int")

        self.__values = self.__values[n:] + self.__values[:n]
        return self.__values

    def sum(self):
        total = 0

        for el in self.__values:
            if isinstance(el, Iterable):
                total += len(el)
            else:
                total += el

        return total


    def overbound(self):
        max_value = float('-inf')
        max_value_index = None

        for index in range(0, len(self.__values)):
            current_element = self.__values[index]

            if isinstance(current_element, Iterable):
                current_element = len(current_element)

            if max_value < current_element:
                max_value = current_element
                max_value_index = index

        return max_value_index

    def underbound(self):
        min_value = float('inf')
        min_value_index = None

        for index in range(0, len(self.__values)):
            current_element = self.__values[index]

            if isinstance(current_element, Iterable):
                current_element = len(current_element)

            if min_value > current_element:
                min_value = current_element
                min_value_index = index

        return min_value_index
