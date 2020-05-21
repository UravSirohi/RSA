def generate(x):
    while True:
        x += 1
        if x == 2 or x == 3 or x == 5 or x == 7:
            is_integer_, is_integer_1, is_integer_11, is_integer_0 = (True, True, True, True)
        else:
            is_integer_ = not float(x / 2).is_integer()
            is_integer_1 = not float(x / 3).is_integer()
            is_integer_11 = not float(x / 5).is_integer()
            is_integer_0 = not float(x / 7).is_integer()
        if is_integer_1 and is_integer_ and is_integer_11 and is_integer_0:
            return x
