import random
import string

N = 7
a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

print(a)
