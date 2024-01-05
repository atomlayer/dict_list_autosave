import os
import unittest

from dict_list_autosave.fdict import fdict


class TestFDict(unittest.TestCase):
    def setUp(self):
        self.file_name = 'test.json'
        self.fdict = fdict(self.file_name, {'key1': 'value1', 'key2': 'value2'})

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_init(self):
        self.assertEqual(self.fdict['key1'], 'value1')
        self.assertEqual(self.fdict['key2'], 'value2')

    def test_update(self):
        self.fdict.update({'key3': 'value3'})
        self.assertEqual(self.fdict['key3'], 'value3')

    def test_clear(self):
        self.fdict.clear()
        self.assertEqual(len(self.fdict), 0)

    def test_pop(self):
        value = self.fdict.pop('key1')
        self.assertEqual(value, 'value1')
        with self.assertRaises(KeyError):
            _ = self.fdict['key1']

    def test_popitem(self):
        key, value = self.fdict.popitem()
        self.assertTrue(key in ['key1', 'key2'])
        self.assertTrue(value in ['value1', 'value2'])
        with self.assertRaises(KeyError):
            _ = self.fdict[key]

    def test_setdefault(self):
        default = self.fdict.setdefault('key3', 'default')
        self.assertEqual(default, 'default')
        self.assertEqual(self.fdict['key3'], 'default')

    def test_delitem(self):
        del self.fdict['key1']
        with self.assertRaises(KeyError):
            _ = self.fdict['key1']

    def test_setitem(self):
        self.fdict['key4'] = 'value4'
        self.assertEqual(self.fdict['key4'], 'value4')

if __name__ == '__main__':
    unittest.main()


