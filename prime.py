<<<<<<< HEAD
import math

def is_prime(n):
    "Devuelve True si n es primo, False en caso contrario."
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    "Ejecuta la logica principal: Imprime los números primos de 0 a 99."
    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
=======
import math

def is_prime(n):
    "Devuelve True si n es primo, False en caso contrario."
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    "Ejecuta la logica principal: Imprime los números primos de 0 a 99."
    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
>>>>>>> ab8afeb48b00a5afa9bc7c3905aa6adf0834859f
