import time
from contextlib import contextmanager

class cm_timer_1():
    def __init__(self):
        self._start_time_ = None
    def __enter__(self):
        self._start_time_ = time.perf_counter()
    def __exit__(self, *args):
        print(time.perf_counter()-self._start_time_)

@contextmanager
def cm_timer_2():
    try:
        start = time.perf_counter()
        yield 0
    finally:
        print(time.perf_counter() - start)

if __name__ == "__main__":
    print('cm_timer_1: ')
    with cm_timer_1():
        time.sleep(5.5)
    print('__' * 10, "\n")
    print('cm_timer_2: ')
    with cm_timer_2():
        time.sleep(5.5)