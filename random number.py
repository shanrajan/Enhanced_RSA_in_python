import random
from Crypto.Util.number import getPrime

p = getPrime(128)

print (p)
phi=6
e = random.randrange(2, phi)
print(e)