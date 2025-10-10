import tuple
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5, 1, 3, 4)
new_tuple = tuple1 + tuple2
print(new_tuple)
for t in [tuple1, tuple2, new_tuple]:
		print(t)
		repeated_tuple = new_tuple * 3
		print(repeated_tuple)