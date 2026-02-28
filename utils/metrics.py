import time

def measure_time(func, prompt):
    start = time.time()
    result = func(prompt)
    end = time.time()
    return result, round(end - start, 2)