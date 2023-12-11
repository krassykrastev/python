from copy import deepcopy
from typing import Optional, Any, Iterable


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        self.__values.append(value)
        return self.__values

    def __check_index_type(self, index):
        if not isinstance(index, int):
            raise ValueError("Invalid index type. You must pass an integer")

    def remove(self, index):
        self.__check_index_type(index)
        try:
            element = self.__values.pop(index)
            return element
        except IndexError:
            raise IndexError("Invalid index")

    def save_remove(self, index):
        self.__check_index_type(index)
        try:
            element = self.__values[index]
            self.__values.pop(index)
            return element
        except IndexError:
            return None

    def get(self, index, default_val: Optional[Any] = None):
        self.__check_index_type(index)
        try:
            return self.__values[index]
        except IndexError:
            if default_val is None:
                return None
            return default_val

    def extend(self, value, *args):
        if isinstance(value, Iterable):
            self.__values.extend(value)
        else:
            self.__values.append(value)
        self.__values.extend(args)
        return self.__values

    def insert(self, index, value):
        self.__check_index_type(index)
        try:
            self.__values.insert(index, value)
            return self.__values
        except IndexError:
            raise IndexError("Invalid index")

    def pop(self):
        result = self.__values.pop()
        return result

    def clear(self):
        self.__values.clear()

    def index(self, value):
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return list(reversed(self.__values))

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self):
        result = {}
        for i in range(0, len(self.__values), 2):
            key = self.__values[i]
            try:
                value = self.__values[i + 1]
            except IndexError:
                value = " "
            result[key] = value
        return result

    def move(self, amount):
        self.__check_index_type(amount)
        first_part = self.__values[:amount]
        second_part = self.__values[amount:]
        self.__values = second_part + first_part
        return self.__values

    def sum(self):
        result = 0
        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            else:
                result += len(el)
        return result

    def overbound(self):
        biggest_index = None
        max_value = float("-inf")
        for index in range(len(self.__values)):
            element = self.__values[index]
            if isinstance(self.__values[index], Iterable):
                element = len(self.__values[index])
            if element > max_value:
                max_value = element
                biggest_index = index
        return biggest_index

    def underbound(self):
        smallest_index = None
        min_value = float("inf")
        for index in range(len(self.__values)):
            element = self.__values[index]
            if isinstance(self.__values[index], Iterable):
                element = len(self.__values[index])
            if element < min_value:
                min_value = element
                smallest_index = index
        return smallest_index
