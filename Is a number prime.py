import random
def is_prime(n, k=5):
    if n <= 1:
      return False
    for _ in range(k):
      a = random.randint(1, n-1)
      if pow(a, n-1, n) != 1:
        return False
    return True

if __name__ == '__main__':
    print(is_prime(5))