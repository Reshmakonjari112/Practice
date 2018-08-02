
import random
# import rolling_dice

num = range(1, 100, 1)
random_num = 0
while num > 1 or num < 100:
    random_num = random_num + random.choice(num)
    break
print random_num

guess_input = input("Guess the number: ")

while guess_input != random_num:
    if guess_input > random_num:
        print "Number is high"
        guess_input = input("Guess the number again: ")
    else:
        print "Number is low"
        guess_input = input("Guess the number again: ")
else:
    print "Correct answer!!"
