import json
import os
import threading


class flist(list):


    def __init__(self, file_name, seq=()):

        self.file_name = file_name
        self.lock = threading.Lock()
        data = self._load_from_json()
        if seq:
            data.extend(seq)
        super().__init__(data)

    def save_to_json(self):
        with self.lock:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(self, file, ensure_ascii=False)

    def _load_from_json(self):
        with self.lock:
            if not os.path.exists(self.file_name):
                return {}
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from {self.file_name}")
                return {}

    def append(self, object):
        super().append(object)
        self.save_to_json()

    def clear(self):
        super().clear()
        self.save_to_json()

    def copy(self):
        return list(self)

    def extend(self, iterable):
        super().extend(iterable)
        self.save_to_json()

    def insert(self, index, object):
        super().insert(index, object)
        self.save_to_json()

    def pop(self, index=-1):
        output = super().pop(index)
        self.save_to_json()
        return output

    def remove(self, value):
        super().remove(value)
        self.save_to_json()

    def reverse(self):
        super().reverse()
        self.save_to_json()

    def sort(self, key=None, reverse=False):
        output = super().sort(key=key, reverse=reverse)
        self.save_to_json()
        return output


    def __add__(self, x):
        output = super().__add__(x)
        self.save_to_json()
        return output

    def __delitem__(self, i):
        super().__delitem__(i)
        self.save_to_json()

    def __iadd__(self, x):
        output = super().__iadd__(x)
        self.save_to_json()
        return output

    def __imul__(self, n):
        output = super().__imul__(n)
        self.save_to_json()
        return output

    def __setitem__(self, s, i):
        super().__setitem__(s, i)
        self.save_to_json()
