from math import fabs, ceil


def diamond(n):
	if n < 0 or n % 2 == 0:
		return None
	midpoint = (n - 1) // 2
	spaces = lambda x: abs(x - midpoint)
	filled = lambda x: n - 2 * abs(x-midpoint)
	layer = lambda l: " " * spaces(l) + "*" * filled(l) + "\n"
	return "".join([layer(l) for l in range(n)])


print(diamond(5))


'''
s d
0 1  *

1 1   *
0 3  ***
1 1   *

2 1   *
1 3  ***
0 5 *****
1 3  ***
2 1   *

3 1    *
2 3   ***
1 5  *****
0 7 *******
1 5  *****
2 3   ***
3 1    *
'''