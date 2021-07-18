# Write your code below this line 👇
import math


def prime_checker(number):
    is_prime = True
    div = 3
    iter_count = 0
    if number == 1:
        is_prime= False
    elif number == 2 or number == 3:
        is_prime = True
    else:
        while ~is_prime and div < math.sqrt(number):
            if number % div == 0:
                is_prime = False
            div += 1
            iter_count+=1

    if is_prime:
        print(f"Prime, {iter_count}")
    else:
        print(f"Not prime, {iter_count}")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(n)
