def add(a, b):
	return a + b

def twice(x):
	return x * 2


aa = add(1, 2)
bb = twice(aa)
print(bb)


print('-' * 20)


def add2(a, b):
	n = twice2(a + b)
	return n

def twice2(x):
	return x * 2

cc = add2(1, 2)
print(cc)