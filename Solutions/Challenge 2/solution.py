from math import sqrt

def rotate(num):
  num = str(num)
  return int(num[1:] + num[:1])

def all_rotations_primes(num, primes):
  return True

def era_sieve(n):
  possiblePrimes = [True] * (n+1)#2 à n
  possiblePrimes[0] = possiblePrimes[1] = False
  
  for p in range(2, int(sqrt(n))+1): 
    if possiblePrimes[p]:
      for j in range(p**2, n+1, p):
        possiblePrimes[j] = False

  return possiblePrimes

expected= [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

def count_prime_rotations(n):
  possiblePrimes = era_sieve(n)
  count = 0

  for i in range(2, len(possiblePrimes)): #2 à n
    if possiblePrimes[i]:
      n = i
      j = 2
      while j < i:
        n = rotate(n)
        if not possiblePrimes[n]:
          break
        j+=1
      else:
        count +=1
      # for _ in range(2, i):
      #   n=rotate(n)
      #   if not possiblePrimes[n]:
      #     break
      

  return count

if __name__ == "__main__":
    print(count_prime_rotations(int(10e6)))
