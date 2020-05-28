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
        elif int(a) == 1 or int(b) == 1:
            print('Requested value of a_ and/or b_ is too small they both must be more than one.')
        else:
            break
    main(a, b, 0)


def main(a, b, ed):
    if ed == 0:
        print('Processing value of p...')
        p = int(f'{Prime_number_generator.generate(int(a), -1)}')
        print('Processing value of q...')
        q = int(f'{Prime_number_generator.generate(int(b), p)}')
        print('Processing value of n...')
        n = operator.mul(p, q)
        print('Processing value of fi_n...')
        fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
        print('Processing value of e...')
        e = int(f'{e_value(n, fi_n)}')
        print('Processing value of d...')
        d = int(f'{d_value(fi_n, e)}')
        print('Process fully complete')
        print(f'Public key: ({e}, {n})\n'
              f'Private key : ({d}, {n})')
        cipher(d, e, n)
    elif ed == -1:
        p = int(f'{Prime_number_generator.generate(int(a), -1)}')
        q = int(f'{Prime_number_generator.generate(int(b), p)}')
        n = operator.mul(p, q)
        fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
        e = int(f'{e_value(n, fi_n)}')
        d = int(f'{d_value(fi_n, e)}')
        values = {
            'p': p,
            'q': q,
            'n': n,
            'fi_n': fi_n,
            'e': e,
            'd': d,
            'public key': f'({e}, {n})',
            'private key': f'({d}, {n})'
        }
        return values


def find_factors(a):
    x = 1
    factors = []
    while x != int(a):
        x += 1
        z = operator.truediv(int(a), x)
        if z.is_integer():
            factors.append(x)
    return factors


def co_prime(a, b):
    num_1 = find_factors(a)
    num_2 = find_factors(b)
    x = -1
    while True:
        x += 1
        try:
            v = num_1[x]
        except IndexError:
            return True
        if v in num_1 and v in num_2:
            return False


def e_value(n, fi_n):
    value_being_tested = int(fi_n)
    while value_being_tested != 2:
        value_being_tested -= 1
        is_co_prime_n = co_prime(value_being_tested, n)
        is_co_prime = co_prime(value_being_tested, fi_n)
        if is_co_prime and is_co_prime_n:
            return int(value_being_tested)


def d_value(fi_n, e):
    val_being_tested = 1
    val_being_tested_ = 1
    while True:
        val_being_tested += 1
        step_1 = operator.mul(val_being_tested, e)
        step_2 = operator.mod(step_1, int(fi_n))
        if step_2 == 1 and int(val_being_tested) >= 20000 and val_being_tested != e:
            if val_being_tested_ < val_being_tested:
                return val_being_tested_
            return val_being_tested
        val_being_tested_ = val_being_tested


def cipher(d, e, n):
    encrypt = input('''Text to be encrypted: ''')
    encrypt_ = encrypt.isdigit()
    if encrypt_:
        encrypted = operator.mod(operator.pow(int(encrypt), e), n)
        print(f'Text encrypted: {encrypted}')
        decrypted = operator.mod(operator.pow(int(encrypted), d), n)
        print(f'Text decrypted: {decrypted}')
    else:
        current_len_value = 0
        text_encrypted = {}
        key = 0
        print('Processing...')
        while current_len_value != len(encrypt):
            current_len_value += 1
            current_text = encrypt[operator.sub(current_len_value, 1)]
            try:
                into_num[current_text]
            except KeyError:
                key += 1
                into_num[str(current_text)] = str(key)
                into_let[str(key)] = str(current_text)
            character_into_int = into_num[current_text]
            encrypted = operator.mod(operator.pow(int(character_into_int), e), n)
            text_encrypted[operator.sub(current_len_value, 1)] = encrypted
        print(f'Text encrypted: {text_encrypted}')
        current_len_val = 0
        text_decrypted = ''
        while current_len_val != len(encrypt):
            current_len_val += 1
            current_num = text_encrypted[operator.sub(current_len_val, 1)]
            decrypted = operator.mod(operator.pow(int(current_num), d), n)
            num_into_let = into_let[str(decrypted)]
            text_decrypted = f'{text_decrypted}{num_into_let}'
        print(f'Text decrypted: {text_decrypted}')
        into_let.clear()
        into_num.clear()
        cipher(d, e, n)


run()
