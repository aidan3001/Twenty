import random

# name = input("what is your name?")



def rand10():
    return random.randint(1,10)

userpoints = rand10()
comppoints = rand10()

print(comppoints)

if comppoints < 16:
    comppoints = comppoints + rand10()
    print(comppoints)

