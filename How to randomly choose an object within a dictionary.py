import random

# for the value in a dictionary
d = {"a":3, "b": 5, "c":1, "d":2}
print(random.choice(list(d.values())))

# for the name in a dictionary
d = {"a":3, "b": 5, "c":1, "d":2}
print(random.choice(list(d.keys())))

# for both items in a dictionary
d = {"a":3, "b": 5, "c":1, "d":2}
print(random.choice(list(d.items())))
