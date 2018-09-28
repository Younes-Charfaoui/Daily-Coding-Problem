"""This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28"""

def make_perfect(number):
	arr = str(number)
	r = 0
	for i in arr:
		r+= int(i)
	return arr+str()

def sum_number(number):
	if int(number) < 10 : 
		return int(number)
	else:
		return int(number[0]) + sum_number(number[1:])
