
import math


def find_factors(n):
	# sqrt = int(math.ceil(math.sqrt(n)))
	# for i in range(2,sqrt):
	for i in range(2,n):

		if n%i ==0:
			if is_prime(i):
				yield i
			else:
				find_factors(i)
			find_factors(n/i)
		


def is_prime(n):
	if n ==2:
		return True
	if n%2 ==0 or n==1:
		return False
	for i in range(2,int(math.ceil(math.sqrt(n)))+1):
		if n%i ==0:
			return False
			break
		# elif n%i !=0:
	return True


def find_highest_pal():
	for i in range(1000, 100, -1):
		for j in range(1000, 100, -1):
			if is_palindrome(i*j):
				yield i*j


def is_palindrome(n):
	return str(n) == str(n)[::-1]



li = range(20, 0, -1)
new_li = []
for i in li:
	for j in li:
		if i%j == 0 and i is not j:
			print i, j, i%j
			new_li.append(j)




square of the sum = sum(range(101))**2
sum of the squares 

def sum_of_squares():
	sum = 0
	for i in range(101):
		sum += i**2
	return sum

def find_primes(end):
	primes =[2]
	i=3
	while len(primes)<end:
		print i, is_prime(i)
		if is_prime(i):
			primes.append(i)
			print i, len(primes)
		i +=2



string = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
products = []
i=0
while i+5 < 1000:
	product = 1
	slizz = string[i:i+5]
	for s in slizz:
		product *=int(s)
		products.append(product)
	i += 1


#problem 9
for x in range(999):
	for y in range(999-x):
		z = 1000-x-y
		# print x,y,z
		if x**2 + y**2 == z**2:
			print x,y,z



def find_primes_under_x(x):
	primes = []
	for i in range(x):
		print i
		if is_prime(i):
			primes.append(i)
	return primes




def factorial(x):
	if x == 1:
		return 1
	else:
		return x* factorial(x-1)


