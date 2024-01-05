import os
import threading

from dict_list_autosave.fdict import fdict


def worker(dictionary, key, value):
    dictionary[key] = value

def test_thread_safety():
    d = fdict('test2.json')
    threads = []

    # Start 10 threads that try to modify the dictionary at the same time
    for i in range(10):
        t = threading.Thread(target=worker, args=(d, f'key{i}', f'value{i}'))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Check the results
    for i in range(10):
        assert d[f'key{i}'] == f'value{i}'

    print('All tests passed.')

test_thread_safety()
os.remove('test2.json')