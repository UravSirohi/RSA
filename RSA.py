import Prime_number_generator
import operator
from Generator import *


def run():
    while True:
        a = input('Min value of p: ')
        b = input('Min value of q: ')
        a_ = not a.isdigit()
        b_ = not b.isdigit()
        if a_ or b_:
            print('Please enter a integer for both entrances.')
        elif int(a) > 31 or int(b) > 31:
            print('Requested min value of q or/and p is too larger, they both must be less than 21')
        elif int(a) <= 1 or int(b) <= 1:
            print('Requested min value of q or/and p is too small, they both must be more than 1.')
        else:
            break
    main(a, b)


def main(a, b):
    p = int(Prime_number_generator.generate(int(a)))
    q = int(Prime_number_generator.generate(int(b)))
    if int(p) == int(q):
        p = 31
        q = 29
        print(f'P and Q are identical so we have created a new value for p and q, p = {p}, q = {q}')
    n = operator.mul(p, q)
    fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
    e = e_value(n, fi_n)
    d = d_value(fi_n, e)
    print(f'Public key: ({e}, {n})\n'
          f'Private key : ({d}, {n})')
    cipher(d, e, n)


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
    y = 0
    poss_e = {}
    while x < fi_n:
        x += 1
        is_co_prime_n = co_prime(x, n)
        is_co_prime = co_prime(x, fi_n)
        if is_co_prime and is_co_prime_n:
            y += 1
            poss_e[y] = x
    return poss_e[y]


def d_value(fi_n, e):
    y_ = 0
    x = 1
    poss_d = {}
    while True:
        x += 1
        z = operator.mul(x, e)
        y = operator.mod(z, fi_n)
        if y == 1:
            y_ += 1
            poss_d[y_] = x
            if int(y_) == 11:
                break
    return poss_d[y_]


def cipher(d, e, n):
    while True:
        encrypt = input('''Text to be encrypted: ''')
        encrypt_ = encrypt.isdigit()
        if encrypt_:
            encrypted = operator.mod(operator.pow(int(encrypt), e), n)
            print(f'Text encrypted: {encrypted}')
            decrypted = operator.mod(operator.pow(int(encrypted), d), n)
            print(f'Text decrypted: {decrypted}')
        else:
            x = 0
            y = {}
            while x != len(encrypt):
                x += 1
                z = encrypt[operator.sub(x, 1)]
                g = into_num[z]
                encrypted = operator.mod(operator.pow(int(g), e), n)
                decrypted = operator.mod(operator.pow(int(encrypted), d), n)
                y[operator.sub(x, 1)] = decrypted
            x_ = 0
            y_ = ''
            while x_ != len(encrypt):
                x_ += 1
                z_ = y[operator.sub(x_, 1)]
                e_ = into_let[str(z_)]
                y_ = f'{y_}{e_}'
            print(f'Text decrypted: {y_}')


run()
