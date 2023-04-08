import random
from math import gcd, pi

n = 1000000 # liczba losowań
count = 0 # licznik par względnie pierwszych

for i in range(n):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    if gcd(a, b) == 1:
        count += 1

percentage = count / n
print("Odsetek par względnie pierwszych: {:.3f}".format(percentage))

cesaro_pi = (6 / (percentage ** 0.5)) ** 0.5
print("Wyznaczona wartość π: {:.3f}".format(cesaro_pi))
