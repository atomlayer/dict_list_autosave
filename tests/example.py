from dict_list_autosave.fdict import fdict
from dict_list_autosave.flist import flist

d = fdict('test.json')
d["test"] = 1
d.update(x=5)

l = flist("test2.json")
l.append("test")
l.extend([5, 8, 9])
