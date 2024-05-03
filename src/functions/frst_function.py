import random

def generate_random_booleans(n):
    s = 1 << n
    v = [random.choice([1, 0]) for _ in range(s)]
    return v

print(generate_random_booleans(3))