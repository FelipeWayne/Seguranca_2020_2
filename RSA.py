# UNIVERSIDADE FEDERAL DA FRONTEIRA SUL
# PROFESSOR: Emílio Wuerges
# ALUNO: FELIPE AUGUSTO DA SILVA
# EMAIL: felipeaugustosilva94@gmail.com
# DESENVOLVIDO NO AMBIENTE LINUX
#   

# TRABALHO 04 - RSA
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1716

import sys

# Função que encontra o valor de P 
def fator(i, N):
    if (N%i == 0):
        return i
    else: 
        # Por serem valores primos impares calculo apenas com os valores impares
        return fator(i+2, N)

# Função responsavel por calculo a Função totiente de Euler (phi)
def phi( N ):
    P = fator(3, N) #Inicia no 3 para encontrar três pois (15<=N)
    Q = N/P         #Se N = PQ e sabendo P teos que Q = N/P
    return (P-1)*(Q-1)

#Calcula a chave para descriptrografar a mensagem
def D(N, E):
    c = 1
    tot = phi(N)
    while(c*E%tot != 1): #DE = 1 (mod φ(N)) para Calcular D utilizo a variavel c
        c+=1
    return c

#Descriptografar a mensagem
def mensagem(N, E, C):
    m=1
    i=0
    d = D(N, E)
    #M = Cd (mod n) definitivamente usar isso estoura  qualquer tipo de inteiro par valores altos. Então calculo 1 a 1
    while(i < d): 
        m = m*C % N
        i+=1
    return m


def main():
    N, E, C = map(int, sys.stdin.readline().split())
    print(mensagem(N,E,C))
    return 0

main()