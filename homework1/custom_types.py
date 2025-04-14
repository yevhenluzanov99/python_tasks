class CustomDict(object):
    """
    CustomDict is a custom implementation of a hash table with open addressing and linear probing.
    Attributes:
        _size (int): The number of key-value pairs currently stored in the hash table.
        _table (list): The internal storage for the hash table, initialized with a fixed size.
        _scaling (float): The load factor threshold at which the hash table resizes.
    Methods:
        __init__(scaling: float = 0.7, *args, **kwargs):
            Initializes the CustomDict with an optional scaling factor.
        __hash_item__(key):
            Computes the hash value for a given key and maps it to the index of the internal table.
        _resize():
            Resizes the hash table when the load factor exceeds the scaling threshold.
        __setitem__(key, value):
            Inserts or updates a key-value pair in the hash table. Resizes the table if necessary.
        __getitem__(key):
            Retrieves the value associated with the given key. Raises KeyError if the key is not found.
    """

    def __init__(self, scaling: float = 0.7, *args, **kwargs):
        self._size = 0
        self._table = [None] * 8
        self._scaling = scaling

    def __hash_item__(self, key):
        return hash(key) % len(self._table)

    def _resize(self):
        old_table = self._table
        self._table = [None] * (len(old_table) * 2)
        self._size = 0

        for item in old_table:
            if item is not None:
                self.__setitem__(item[0], item[1])

    def __setitem__(self, key, value):
        if self._size / len(self._table) >= self._scaling:
            self._resize()

        index = self.__hash_item__(key)
        for i in range(len(self._table)):
            probe_index = (index + i) % len(self._table)
            if self._table[probe_index] is None:
                self._table[probe_index] = (key, value)
                self._size += 1
                return
            elif self._table[probe_index][0] == key:
                self._table[probe_index] = (key, value)
                return
        raise RuntimeError("Hash table is full")

    def __getitem__(self, key):
        index = self.__hash_item__(key)
        for i in range(len(self._table)):
            probe_index = (index + i) % len(self._table)
            entry = self._table[probe_index]
            if entry is None:
                break
            if entry[0] == key:
                return entry[1]
        raise KeyError(f"Key {key} not found in CustomDict")
