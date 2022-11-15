from random import randint

r = randint(0,10)
print(r)

# guess = int(input('huj'))
# print(type(guess))

while True:
    guess = int(input('Guess num: '))
    if guess == r:
        break
