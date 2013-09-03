import scipy as sci
import scipy.linalg as linalg
import math

def get_prob01():
  sum = 0
  for n in range(0, 334):
    sum += 3*n
  n = 0
  for n in range(0, 200):
    if n%3 > 0:
      sum += n*5
  return sum

def get_fibN(n):
  if n < 0:
    return 0
  elif n <= 1:
    return n
  else:
    return get_fibN(n-1) + get_fibN(n-2)

def get_prob02():
  sum = 0
  fib = 0
  n = 0
  while fib <= 4000000:
    fib = get_fibN(n)
    if fib < 4000001:
      sum += fib
    n += 3
  return sum

def find_facts(mfact):
  import itertools
  import operator
  import math

  pmax = int(math.sqrt(mfact))
  primes = list(itertools.takewhile(lambda x: x<pmax+1, itertools.count(3, 2)))
  for p in primes:
    primes = list(itertools.filterfalse(lambda x: (x>p and x%p==0) or mfact%x, primes))
  return primes

def get_prob03(num):
  return find_facts(num)

