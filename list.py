import time
import tracemalloc
N = 5_000_000
def transform(x):
    return x * x
print("LIST COMPREHENSION")
tracemalloc.start()
start = time.perf_counter()
result_list = [transform(x) for x in range(N)]
creation_time_list = time.perf_counter() - start
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Creation time:", creation_time_list, "seconds")
print("Memory used:", peak / (1024 * 1024), "MB")
start = time.perf_counter()
total_list = sum(result_list)
consumption_time_list = time.perf_counter() - start
print("Consumption time:", consumption_time_list, "seconds")
print("Total:", total_list)
print("\nGENERATOR EXPRESSION")
tracemalloc.start()
start = time.perf_counter()
result_generator = (transform(x) for x in range(N))
creation_time_generator = time.perf_counter() - start
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Creation time:", creation_time_generator, "seconds")
print("Memory used:", peak / (1024 * 1024), "MB")
start = time.perf_counter()
total_generator = sum(result_generator)
consumption_time_generator = time.perf_counter() - start
print("Consumption time:", consumption_time_generator, "seconds")
print("Total:", total_generator)