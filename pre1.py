
# Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.


from word2number import w2n
from num2words import num2words
def gcd(a, b):

	if (a == 0):
		return num2words(b)
	if (b == 0):
		return num2words(a)

	if (a == b):
		return num2words(a)

	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)

a = w2n.word_to_num(input())
b = w2n.word_to_num(input())
if(gcd(a, b)):
	print('GCD of',a, 'and',b, 'is', gcd(a, b))
else:
	print('not found')
