#!/usr/bin/env python
# File: sum_primes.py
# Author: Vitalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com

import math
import sys
import pp
import time


def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in range(2, n) if isprime(x)])


print("""Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system""")

# tuple of all parallel python servers to connect with
ppservers = ('*',)
#only use remote node
job_server = pp.Server(ppservers=ppservers,ncpus=0)
#use remote node and create local node at the same time
# job_server = pp.Server(ppservers=ppservers)
print("Starting pp with %s workers" % job_server.get_ncpus())

# Submit a job of calulating sum_primes(100) for execution.
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before
#             sum_primes execution
# Execution starts as soon as one of the workers will become available
job1 = job_server.submit(sum_primes, (100, ), (isprime, ), ("math", ))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will
# wait here until result is available
result = job1()

print("Sum of primes below 100 is %s" % result)
time.sleep(0.5)


# The following submits 8 jobs and then retrieves the results
inputs = (100000 for i in range(100))
jobs = [(upper, job_server.submit(sum_primes, (upper, ), (isprime, ),
        ("math", ))) for upper in inputs]

for upper, job in jobs:
    print("Sum of primes below %s is %s" % (upper, job()))
job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com
