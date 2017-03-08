import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


primes = []
for i in range(2, 3000):
  if is_prime(i):
    primes.append(i)

n = int(raw_input())
count = 0
for i in range(1, n + 1):
  divisors = 0
  for prime in primes:
    if i % prime == 0:
      divisors = divisors + 1
  if divisors == 2:
    count = count + 1
print count
