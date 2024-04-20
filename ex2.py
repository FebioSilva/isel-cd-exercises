# Description: Aula Prática 1 - Introdução à Programação em Python

#Função que apresenta os N primeiros termos de uma progressão aritmética, cujo primeiro termo é u e a razão é r.

def aritmeticProgression(u, r, N):
    numbers = ""
    for x in range(N):
        numbers += str(u + x*r) + ", "
    print(numbers)

#Função que calcula o fatorial de determinado número inteiro a.

def factorialNumber(N):
    result = 1
    for x in range(N):
        result += result*x
    return result

#Função que apresenta todos os números primos contidos no intervalo definido por lef t e right, inclusivamente.

def minMultipleCommon(a, b):
    c = a
    d = b
    while a != b:
        if a < b:
            a+=c
        else:
            b+=d
    return a

#Função que apresenta todos os números primos contidos no intervalo definido por lef t e right, inclusivamente.

def primes(left, right):
    primesList = []
    for x in range(left, right+1):
        if x > 1:
            for y in range(2,x):
                if x % y == 0:
                    break
            else:
                primesList.append(x)
    return primesList


#Função que apresenta todos os símbolos de um ficheiro, cuja frequência de ocorrência é superior a uma percentagem indicada como parâmetro.

def symbolsFrequency(file, percentage):
    f=open(file, "r")
    symbols = {}
    text = f.read()
    total_chars = len(text)

    for c in text:
        if(symbols.get(c) == None):
            symbols[c] = 1
        else:
            symbols[c] = symbols.get(c) + 1
    print(symbols)
    for x, y in symbols.items():
        if(y/total_chars > percentage):
            print("Symbol: '%s' - Occurrencies: %d" %(x, y))
    

print("Progressão aritmética 1: ")
aritmeticProgression(10, 3, 5)
print("Progressão aritmética 2: ")
aritmeticProgression(5,2,8)
print("Progressão aritmética 3: ")
aritmeticProgression(2,-1,6)
print("Factorial: %d" %factorialNumber(3))
print("Factorial: %d" %factorialNumber(5))
print("Factorial: %d" %factorialNumber(10))
print("MMC1: %d" %minMultipleCommon(10,15))
print("MMC2: %d" %minMultipleCommon(11,20))
print("MMC3: %d" %minMultipleCommon(7,25))
print("Primes1: %s" %primes(1,25))
print("Primes2: %s" %primes(1,50))
print("Primes3: %s" %primes(10,100))
symbolsFrequency("resources/alice29.txt", 0.05)





