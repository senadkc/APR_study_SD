# encoding:utf-8

for x in range(1, 10):
	y in range(1, 10):
		text = "x".join(map(str, (x, y)))
		text = "=".join(map(str, (text, x*y)))
		print(text)