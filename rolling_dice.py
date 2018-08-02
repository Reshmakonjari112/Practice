
import random

num = range(1, 7, 1)
random_num = 0
print num
while num < 7 or num >1:
    random_num = random_num + random.choice(num)
    break
print random_num
