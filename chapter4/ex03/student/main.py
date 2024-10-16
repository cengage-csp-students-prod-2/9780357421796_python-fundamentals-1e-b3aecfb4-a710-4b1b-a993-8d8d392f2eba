skip_integers(*args):
    for value in args:
        if isinstance (value,int):
            continue
        print(value)
skip_integers(5.2, 42, 'value', 6.0, 100, True, None)