import unittest

from homework1.custom_types import CustomDict


class TestCustomDict(unittest.TestCase):
    """
    Test suite for the CustomDict class.
    This test class contains unit tests to verify the functionality of the CustomDict class,
    including initialization, adding key-value pairs, hashing, resizing, collision handling,
    and error handling.
    Test Cases:
    - test_initialization: Verifies that the CustomDict initializes with the correct default values.
    - test_add_key_value: Tests adding a key-value pair and retrieving the value by key.
    - test_hashing: Ensures that keys are hashed correctly and stored in the appropriate index.
    - test_resize: Checks that the CustomDict resizes its internal table when the scaling threshold is exceeded.
    - test_collision_handling: Validates that the CustomDict handles hash collisions correctly.
    - test_key_error: Confirms that accessing a non-existent key raises a KeyError.
    """

    def test_initialization(self):
        d = CustomDict()
        self.assertEqual(len(d._table), 8)
        self.assertEqual(d._size, 0)

    def test_add_key_value(self):
        d = CustomDict()
        d["key1"] = "value1"
        self.assertEqual(d["key1"], "value1")

    def test_hashing(self):
        d = CustomDict()
        d["key1"] = "value1"
        d["key2"] = "value2"
        index1 = d.__hash_item__("key1")
        index2 = d.__hash_item__("key2")

        self.assertEqual(d._table[index1][0], "key1")
        self.assertEqual(d._table[index2][0], "key2")

    def test_resize(self):
        d = CustomDict(scaling=0.5)
        d["key1"] = "value1"
        d["key2"] = "value2"
        d["key3"] = "value3"
        d["key4"] = "value4"
        d["key5"] = "value5"
        d["key6"] = "value6"

        self.assertEqual(len(d._table), 16)

    def test_collision_handling(self):
        d = CustomDict()
        d["key1"] = "value1"
        d["key2"] = "value2"
        d["key3"] = "value3"

        self.assertEqual(d["key1"], "value1")
        self.assertEqual(d["key2"], "value2")
        self.assertEqual(d["key3"], "value3")

    def test_key_error(self):
        d = CustomDict()
        d["key1"] = "value1"
        with self.assertRaises(KeyError):
            d["key2"]


if __name__ == "__main__":
    unittest.main()
