import random

a = random.sample(range(1, 12), 8)


def end_list(a_list) :
    return a_list[0], a_list[len(a_list) - 1]

print(a)
print(end_list(a))
