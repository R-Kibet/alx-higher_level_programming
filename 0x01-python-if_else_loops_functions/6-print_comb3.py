#!/usr/bin/python3

for i in range (0, 90):
	if i % 10 > i / 10:
		if i == 89:
			print(f"{i}")
		else:
			print(f"{i:02d}", end = ', ')
