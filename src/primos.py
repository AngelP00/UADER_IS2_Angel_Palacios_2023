max = int(input("Find primes up to what number? : "))
primeList = []
#for loop for checking each number
#bucle for para verificar cada numero
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	#si es el numero es primo se agrega a la lista de numemros primos
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes
# calculadora de numeros primos: encuentra los primeros n primos
count = int(input("Find how many primes?: "))
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)