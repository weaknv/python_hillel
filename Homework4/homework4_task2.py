list = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 300), (5, 50, 500)]
print([turple[:-1] + (turple[-1]**2,) for turple in list])