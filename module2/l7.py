# Write a decorator that logs the execution time of a function.
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()      # start
        result = func(*args, **kwargs)
        end_time = time.time()        # end
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(2)

slow_function()
