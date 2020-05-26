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
            print('Requested min value of q or/and p is too larger, they both must be less than 32')
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
        print(f'''P and Q are identical, so we have created a new value for p and q, p = {p}, q = {q}.
Otherwise, the RSA code would not work.''')
    n = operator.mul(p, q)
    fi_n = operator.mul(operator.sub(p, 1), operator.sub(q, 1))
    e = e_value(n, fi_n)
    d = d_value(fi_n, e)
    print(f'Public key: ({e}, {n})\n'
          f'Private key : ({d}, {n})')
    cipher(d, e, n)


def __gcd(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    if num_1 == num_2:
        return num_1
    if num_1 > num_2:
        return __gcd(num_1 - num_2, num_2)
    return __gcd(num_1, num_2 - num_1)


def co_prime(a, b):
    if __gcd(a, b) == 1:
        return True
    return False


def e_value(n, fi_n):
    value_being_tested = 1
    poss_of_e = 0
    poss_e = {}
    while value_being_tested < fi_n:
        value_being_tested += 1
        is_co_prime_n = co_prime(value_being_tested, n)
        is_co_prime = co_prime(value_being_tested, fi_n)
        if is_co_prime and is_co_prime_n:
            poss_of_e += 1
            poss_e[poss_of_e] = value_being_tested
    return poss_e[poss_of_e]


def d_value(fi_n, e):
    number_of_d_poss = 0
    val_being_tested = 1
    poss_d = {}
    while True:
        val_being_tested += 1
        step_1 = operator.mul(val_being_tested, e)
        step_2 = operator.mod(step_1, fi_n)
        if step_2 == 1:
            number_of_d_poss += 1
            poss_d[number_of_d_poss] = val_being_tested
            if int(number_of_d_poss) == 11:
                break
    return poss_d[number_of_d_poss]


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
        while current_len_value != len(encrypt):
            current_len_value += 1
            current_text = encrypt[operator.sub(current_len_value, 1)]
            try:
                into_num[current_text] and into_let[current_text]
            except KeyError:
                key += 1
                into_num[str(current_text)] = str(key)
                into_let[str(key)] = str(current_text)
            character_into_int = into_num[current_text]
            encrypted = operator.mod(operator.pow(int(character_into_int), e), n)
            decrypted = operator.mod(operator.pow(int(encrypted), d), n)
            text_encrypted[operator.sub(current_len_value, 1)] = decrypted
        print(f'Text encrypted: {text_encrypted}')
        current_len_val = 0
        text_decrypted = ''
        while current_len_val != len(encrypt):
            current_len_val += 1
            current_let = text_encrypted[operator.sub(current_len_val, 1)]
            num_into_let = into_let[str(current_let)]
            text_decrypted = f'{text_decrypted}{num_into_let}'
        print(f'Text decrypted: {text_decrypted}')
        into_let.clear()
        into_num.clear()
        cipher(d, e, n)


run()
