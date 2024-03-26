import time

import sys
sys.path.append(r"C:\Users\Koren Kaplan\Desktop\Studies\Python\LeetCodeDrills")


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Execution Time:{round(end_time-start_time,3)}')
        return result
    return wrapper

