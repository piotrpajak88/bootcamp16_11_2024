import random
import time
import threading
import multiprocessing

from concurrent.futures import ThreadPoolExecutor

import numpy as np

# obliczanie pi metoda monte-carlo

def monte_carlo_pi(num_samples):
    x = np.random.uniform(-1,1,num_samples)
    y = np.random.uniform(-1,1,num_samples)
    inside_circle = x**2 + y**2 <= 1
    num_inside_circle = np.sum(inside_circle)
    pi_estimate = 4 * num_inside_circle / num_samples
    return pi_estimate

def no_threads(iterations):
    start = time.time()
    pi = monte_carlo_pi(iterations)
    end = time.time()
    print(f'Bez watkow : {pi}, czas {end - start}')

def with_threads(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads
    threads = []
    total_points_inside_circle = 0

    def thread_monte_carlo_pi():
        global total_points_inside_circle
        points_inside_circle_th = monte_carlo_pi(iterations_per_thread)
        with lock:
            total_points_inside_circle += points_inside_circle_th

    lock = threading.Lock()
    start = time.time()
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_monte_carlo_pi())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi =  (total_points_inside_circle/ num_threads)
    end = time.time()
    print(f'Z watkami : {pi}, czas {end - start}')

iterations = 10_000_000
if __name__ == '__main__':
    #no_threads(iterations)
    with_threads(iterations)
