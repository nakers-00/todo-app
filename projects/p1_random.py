import random

low_num = int(input("Enter the lower bound: "))
high_num = int(input("Enter the upper bound: "))


rand_num = random.randrange(low_num, high_num)

print(rand_num)
