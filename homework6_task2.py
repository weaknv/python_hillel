library = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
tuple_lib = list(map(lambda value: (value[0], value[2], value[2]*value[3]
    if value[2]*value[3] >= 100
    else round(value[2]*(value[3] + 10), 2)), library))

print(tuple_lib)