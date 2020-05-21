import Prime_number_generator
import operator
import sys


def run():
    while True:
        a = input('Min value of p: ')
        b = input('Min value of q: ')
        a_ = not a.isdigit()
        b_ = not b.isdigit()
        if a_ or b_:
            print('Please enter a integer for both entrances.')
        elif int(a) > 20 or int(b) > 20:
            print('Requested min value of q or/and p is too larger, they both must be less than 21')
        elif int(a) <= 1 or int(b) <= 1:
            print('Requested min value of q or/and p is too small, they both must be more than 1.')
        else:
            break
    main(a, b)


def main(a, b):
    p = int(Prime_number_generator.generate(int(a)))
    q = int(Prime_number_generator.generate(int(b)))
    n = operator.mul(p, q)
    fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
    e = e_value(n, fi_n)
    d = d_value(fi_n, e)
    encrypt = input('''Number to be encrypted: ''')
    encrypted = operator.mod(operator.pow(int(encrypt), e), n)
    print(f'Number encrypted: {encrypted}')
    decrypted = operator.mod(operator.pow(int(encrypted), d), n)
    print(f'Number decrypted: {decrypted}')
    if int(decrypted) != int(encrypt):
        exit('ValueError: identical values of p and q generated')


def __gcd(a, b):
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    if a > b:
        return __gcd(a - b, b)
    return __gcd(a, b - a)


def co_prime(a, b):
    if __gcd(a, b) == 1:
        return True
    else:
        return False


def e_value(n, fi_n):
    x = 1
    while x < fi_n:
        x += 1
        is_co_prime_n = co_prime(x, n)
        is_co_prime = co_prime(x, fi_n)
        if is_co_prime and is_co_prime_n:
            return x
    else:
        print('''ValueError: unable to return value of e''')
        sys.exit(0)


def d_value(fi_n, e):
    x = 6
    while True:
        x += 1
        z = operator.mul(x, e)
        y = operator.mod(z, fi_n)
        if y == 1:
            return x


run()
