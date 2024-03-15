# Description: Aula Prática 1 - Introdução à Programação em Python

#Função que apresenta os N primeiros termos de uma progressão aritmética, cujo primeiro termo é u e a razão é r.

def aritmeticProgression(u, r, N):
    for x in range(N):
        print(u + x*r)

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
            
    for x, y in symbols.items():
        if(y/total_chars > percentage):
            print("Symbol: '%s' - Occurrencies: %d" %(x, y))
    

    
aritmeticProgression(1, 2, 3)
print("Factorial: %d" %factorialNumber(2))
print("MMC: %d" %minMultipleCommon(10,25))
print("Primes: %s" %primes(1,3))
symbolsFrequency("/workspaces/CD/test.txt", 0.05)





