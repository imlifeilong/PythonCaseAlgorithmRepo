# n! = n * (n-1)!
# (n-1)! = (n-1) * (n-2)!
# .........
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1


def DPNFactorial(n):
	if n < 0:
		return
	if n == 1 or n == 0:
		return n

	return n * DPNFactorial(n-1)


if __name__ == '__main__':
	print(DPNFactorial(3))