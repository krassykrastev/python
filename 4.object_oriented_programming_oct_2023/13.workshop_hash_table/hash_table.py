from typing import NamedTuple, Any, List, Optional, Union

DELETED = object()


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity: int = 4):
        self.capacity = capacity
        self._array: List[Optional[Union[Pair, DELETED]]] = self.capacity * [None]

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError('Capacity must be positive integer')
        self.__capacity = value

    @property
    def array(self):
        return {
            pair for pair in self._array
            if pair not in (None, DELETED)
        }

    @property
    def keys(self):
        return {pair.key for pair in self.array}

    @property
    def values(self):
        return [pair.value for pair in self.array]

    def hash(self, key):
        return hash(key) % self.capacity

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self):
        return len(self.array)

    def __setitem__(self, key, value):
        for index, pair in self._probe(key):
            if pair is DELETED:
                continue
            if pair is None or pair.key == key:
                self._array[index] = Pair(key, value)
                break
        else:
            self._resize()
            self[key] = value

    def __getitem__(self, key):
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __delitem__(self, key):
        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._array[index] = DELETED
                break
        else:
            raise KeyError(key)

        if key in self:
            self._array[self.hash(key)] = None
        else:
            raise KeyError(key)

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.array:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def _probe(self, key):
        index = self.hash(key)
        for _ in range(self.capacity):
            yield index, self._array[index]
            index = (index + 1) % self.capacity

    def _resize(self):
        copy = HashTable(capacity=self.capacity * 2)
        # copy.capacity = self.capacity * 2
        for key, value in self.array:
            copy[key] = value
        self.capacity = copy.capacity
        self._array = copy._array
