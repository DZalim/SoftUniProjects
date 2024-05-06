from unittest import TestCase, main

from AdvancedModule.OOP.workshop_custom_dictionary.custom_hashtable import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.h = HashTable()

    def test_init(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_count(self):
        result = self.h.count
        self.assertEqual(result, 0)

        # TODO test when there is element which is not None

    def test_length(self):
        self.assertEqual(len(self.h), 4)
        self.assertEqual(len(self.h), self.h._HashTable__length)

        # Test with resizing
        self.h["name"] = "Peter"
        self.h["age"] = 25
        self.h["id"] = 1
        self.h["city"] = "Plovdiv"
        self.h["street"] = "Markovo Tepe"

        self.assertEqual(len(self.h), 8)
        self.assertEqual(len(self.h), self.h._HashTable__length)

    def test_get_item(self):
        self.h["name"] = "Peter"

        self.assertEqual(self.h["name"], "Peter")

    def test_get_item_key_not_presented_raises(self):
        with self.assertRaises(KeyError) as err:
            self.h["no-such-key"]
        self.assertEqual(err.exception.args[0], "Key does not exist")

    def test_set_item(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h["name"] = "test"

        self.assertEqual(self.h._HashTable__keys, [None, "name", None, None])
        self.assertEqual(self.h._HashTable__values, [None, "test", None, None])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_same_key_is_replaced_with_latest_value(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h["name"] = "test"

        self.assertEqual(self.h._HashTable__keys, [None, "name", None, None])
        self.assertEqual(self.h._HashTable__values, [None, "test", None, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h["name"] = "test2"

        self.assertEqual(self.h._HashTable__keys, [None, "name", None, None])
        self.assertEqual(self.h._HashTable__values, [None, "test2", None, None])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_more_values_then_current_length_resizes_attributes(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h["name"] = "test"
        self.h["age"] = 25
        self.h["street"] = "new street"
        self.h["number"] = 8

        self.assertEqual(self.h._HashTable__keys, ["number", "name", "age", "street"])
        self.assertEqual(self.h._HashTable__values, [8, "test", 25, "new street"])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h['new_value'] = "hi"
        self.assertEqual(self.h._HashTable__keys, ["number", "name", "age", "street", None, None, "new_value", None])
        self.assertEqual(self.h._HashTable__values, [8, "test", 25, "new street", None, None, "hi", None])
        self.assertEqual(self.h._HashTable__length, 8)

    def test_hash(self):
        result = self.h.hash("name")

        self.assertEqual(result, 1)

    def test_get_existing_value(self):
        self.h["name"] = "test"
        result = self.h.get("name")
        self.assertEqual(result, "test")

    def test_get_non_existing_value_with_no_default_argument(self):
        self.assertNotIn("name", self.h._HashTable__keys)

        result = self.h.get("name")

        self.assertIsNone(result)

    def test_get_non_existing_value_with_default_argument(self):
        self.assertNotIn("name", self.h._HashTable__keys)

        result = self.h.get("name", "default")
        self.assertEqual(result, "default")

    def test_sort(self):
        self.h["name"] = "test"
        self.h["age"] = 25

        self.assertEqual(self.h._HashTable__keys, [None, "name", "age", None])
        self.assertEqual(self.h._HashTable__values, [None, "test", 25, None])
        self.assertEqual(self.h._HashTable__length, 4)

        result = self.h.sort()

        self.assertEqual(self.h._HashTable__keys, [None, "name", "age", None])
        self.assertEqual(self.h._HashTable__values, [None, "test", 25, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.assertEqual(result._HashTable__keys, ["age", "name", None, None])
        self.assertEqual(result._HashTable__values, [25, "test", None, None])
        self.assertEqual(result._HashTable__length, 4)

    def test_add(self):
        self.h["name"] = "test"
        self.h["age"] = 25

        self.assertEqual(self.h._HashTable__keys, [None, "name", "age", None])
        self.assertEqual(self.h._HashTable__values, [None, "test", 25, None])
        self.assertEqual(self.h._HashTable__length, 4)

        self.h.add("new_key", 6)

        self.assertEqual(self.h._HashTable__keys, [None, "name", "age", "new_key"])
        self.assertEqual(self.h._HashTable__values, [None, "test", 25, 6])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_string_representation(self):
        self.h["name"] = "test"
        self.h["age"] = 25

        result = str(self.h)

        self.assertEqual("{ name: test, age: 25 }", result)

if __name__ == "__main__":
    main()
