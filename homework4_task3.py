tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)
sum=[]

for x, y, z in zip(tuple1,tuple2,tuple3):
   sum+=[x+y+z]

sum_tuple = tuple(sum)
print(sum_tuple)
