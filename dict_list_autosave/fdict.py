import json
import os
import threading


class fdict(dict):

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

    def __init__(self, file_name, seq=None, **kwargs):
        self.file_name = file_name
        self.lock = threading.Lock()
        data = self._load_from_json()
        if seq:
            data.update(seq)
        if kwargs:
            data.update(kwargs)
        super().__init__(data)
        self.save_to_json()

    def clear(self):
        super().clear()
        self.save_to_json()

    def copy(self):
        return dict(self)

    def pop(self, key, default=None):
        output = super().pop(key, default)
        self.save_to_json()
        return output

    def popitem(self):
        output = super().popitem()
        self.save_to_json()
        return output

    def setdefault(self, key, default=None):
        output = super().setdefault(key, default)
        self.save_to_json()
        return output

    def update(self, other=None, **kwargs):
        if other is not None:
            super().update(other)
        if kwargs:
            super().update(kwargs)
        self.save_to_json()

    def __delitem__(self, key):
        super().__delitem__(key)
        self.save_to_json()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.save_to_json()
