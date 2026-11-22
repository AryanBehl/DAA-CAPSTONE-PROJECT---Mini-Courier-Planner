import time


def measure_time(function, *args):
    start = time.perf_counter()

    result = function(*args)

    end = time.perf_counter()

    execution_time = end - start

    return result, execution_time
