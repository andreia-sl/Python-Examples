import sys

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)

def simplificar(numerador, denominador):
    divisor = MDC(numerador, denominador)
    return numerador // divisor, denominador // divisor

def calcular(N1, D1, op, N2, D2):
    if op=='+':
        numerador = N1*D2 + N2*D1
        denominador = D1*D2
    elif op=='-':
        numerador = N1*D2 - N2*D1
        denominador = D1*D2
    elif op=='*':
        numerador = N1*N2
        denominador = D1*D2
    elif op=='/':
        numerador = N1*D2
        denominador = N2*D1
    else:
        raise ValueError('Operador incorreto!')
    return numerador, denominador
    
entrada = sys.stdin.read().splitlines()
N = int(entrada[0])
    
for i in range(1, N + 1):
    partes = entrada[i].split()
    N1 = int(partes[0])
    D1 = int(partes[2])
    op = partes[3]
    N2 = int(partes[4])
    D2 = int(partes[6])
    num, den = calcular(N1, D1, op, N2, D2)
    simp_num, simp_den = simplificar(num, den)

    print(f"{num}/{den} = {simp_num}/{simp_den}")
