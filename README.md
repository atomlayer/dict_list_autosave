# dict_list_autosave


The dict_list_autosave library allows you to automatically save changes to dict or list python objects to a file.
You don't need to write a bunch of regular python boilerplate code:  

~~with open(self.file_name, 'w', encoding='utf-8') as file:~~
     ~~json.dump(self, file, ensure_ascii=False)~~


Use the dict_list_autosave library objects (fdict, flist) as normal dict, list python objects.

## Installation

From Github:
```bash
pip install https://github.com/atomlayer/dict_list_autosave/archive/master.zip
```



## Example

```python
from dict_list_autosave.fdict import fdict  
  
d = fdict('test.json')  
d["test"] = 1  
d.update(x=5) 
```
```
Result: 
file: test.json
{"test": 1, "x": 5}
```

```python
from dict_list_autosave.flist import flist  

l = flist("test2.json")  
l.append("test")  
l.extend([5, 8, 9])
```

```
Result: 
file: test2.json
["test", 5, 8, 9]
```



