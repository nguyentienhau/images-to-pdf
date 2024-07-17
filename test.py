from math import sqrt
from os import listdir

factor = sqrt(2)
min_diff = 1
width_result = 0

for width in range(1920, 3000):
	temp = width*factor
	diff = abs(round(temp) - temp)
	
	if diff < min_diff:
		min_diff = diff
		width_result = width

print(f"({width_result}, {round(width_result*factor)})", min_diff)

file_names = listdir("D:/Privates/Test")
file_names.sort()
print(file_names)
