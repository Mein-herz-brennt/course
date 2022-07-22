def typ(typ):
    def type_cheacher(fun):
        def _cheaker(*args):
            for a in args:
                if type(a) == typ:
                    continue
                else:
                    raise TypeError("Неправильний тип змінних")
            return fun(*args)

        return _cheaker

    return type_cheacher


@typ(int)  # вставити свій тип змінних
def func(a, b, c):
    print((a + b + c) / 3)


func(1, 3, 5)
