import unittest
import os

from dict_list_autosave.flist import flist


class TestFlist(unittest.TestCase):

    def setUp(self):
        self.file_name = 'test.json'
        self.flist = flist(self.file_name)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_append(self):
        self.flist.append('test')
        self.assertEqual(self.flist, ['test'])

    def test_clear(self):
        self.flist.extend(['test1', 'test2'])
        self.flist.clear()
        self.assertEqual(self.flist, [])

    def test_copy(self):
        self.flist.append('test')
        copy = self.flist.copy()
        self.assertEqual(copy, ['test'])

    def test_extend(self):
        self.flist.extend(['test1', 'test2'])
        self.assertEqual(self.flist, ['test1', 'test2'])

    def test_insert(self):
        self.flist.insert(0, 'test')
        self.assertEqual(self.flist, ['test'])

    def test_pop(self):
        self.flist.extend(['test1', 'test2'])
        self.assertEqual(self.flist.pop(0), 'test1')

    def test_remove(self):
        self.flist.extend(['test1', 'test2'])
        self.flist.remove('test1')
        self.assertEqual(self.flist, ['test2'])

    def test_reverse(self):
        self.flist.extend(['test1', 'test2'])
        self.flist.reverse()
        self.assertEqual(self.flist, ['test2', 'test1'])

    def test_sort(self):
        self.flist.extend(['test2', 'test1'])
        self.flist.sort()
        self.assertEqual(self.flist, ['test1', 'test2'])

    def test_add(self):
        self.flist = self.flist + ['test']
        self.assertEqual(self.flist, ['test'])

    def test_delitem(self):
        self.flist.extend(['test1', 'test2'])
        del self.flist[0]
        self.assertEqual(self.flist, ['test2'])

    def test_iadd(self):
        self.flist += ['test']
        self.assertEqual(self.flist, ['test'])

    def test_imul(self):
        self.flist.extend(['test'])
        self.flist *= 2
        self.assertEqual(self.flist, ['test', 'test'])

    def test_setitem(self):
        self.flist.extend(['test1', 'test2'])
        self.flist[0] = 'test3'
        self.assertEqual(self.flist, ['test3', 'test2'])

if __name__ == '__main__':
    unittest.main()