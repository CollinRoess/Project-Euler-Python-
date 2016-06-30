"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def pfactor(x):
	p=2
	while (p*p)<x:
		while x%p==0:
			x=(x/p)
		p+=1
	print x
	
pfactor(600851475143)