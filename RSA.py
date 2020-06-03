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
        p = Prime_number_generator.generate(int(a), -1)
        print('Processing value of q...')
        q = Prime_number_generator.generate(int(b), p)
        print('Processing value of n...')
        n = operator.mul(p, q)
        print('Processing value of fi_n...')
        fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
        print('Processing value of e...')
        e = e_value(n, fi_n)
        print('Processing value of d...')
        d = d_value(fi_n, e)
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
    value_being_tested = 1
    latest_key = 0
    poss_d = {}
    while True:
        value_being_tested += 1
        step_1 = operator.mul(value_being_tested, e)
        step_2 = operator.mod(step_1, fi_n)
        if step_2 == 1:
            latest_key += 1
            poss_d[latest_key] = value_being_tested
            if int(latest_key) == 3:
                break
    return poss_d[latest_key]


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
        current_key_ = 0
        text_encrypted = {}
        key = 99
        print('Processing...')
        while current_len_value != len(encrypt):
            current_len_value += 1
            current_text = encrypt[operator.sub(current_len_value, 1)]
            print(f'current_text: {current_text}')
            print(f'current_len_value: {current_len_value}')
            try:
                into_num[current_text]
            except KeyError:
                print('Excepted')
                key += operator.add(int(key), 1)
                print(key)
                into_num[str(current_text)] = str(key)
                into_let[str(key)] = str(current_text)
            character_into_int = into_num[str(current_text)]
            print(f'character into int: {character_into_int}')
            encrypted = operator.mod(operator.pow(int(character_into_int), e), n)
            text_encrypted[current_key_] = encrypted
            current_key_ += 1
        print(f'Text encrypted: {text_encrypted}')
        current_len_val_ = 0
        text_decrypted = ''
        while current_len_val_ != len(encrypt):
            current_len_val_ += 1
            print(f'Text current_len_val_: {current_len_val_}')
            current_num = text_encrypted[operator.sub(current_len_val_, 1)]
            print(f'Text current_num: {current_num}')
            decrypted = operator.mod(operator.pow(int(current_num), d), n)
            print(f'Text decrypted: {decrypted}')
            try:
                num_into_let = into_let[str(decrypted)]
            except KeyError:
                num_into_let = '*'
            print(f'number_into_let: {num_into_let}')
            text_decrypted = f'{text_decrypted}{num_into_let}'
        print(f'Text decrypted: {text_decrypted}')
        into_let.clear()
        into_num.clear()
        cipher(d, e, n)


run()
