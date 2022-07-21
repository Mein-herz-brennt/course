from textwrap import wrap

File = 'maxim.txt'
Filee = 'maxim.txt'


def forty_symbols_in_line(file, file2):
    f = open(file, "r")
    F = open(file2, "w")
    symbols = f.read()
    symbols1 = wrap(symbols, 40)
    for i in range(len(symbols1)):
        symbols1[i] += '\n'
    SYMBOLS = ''
    for i in symbols1:
        SYMBOLS += i

    F.write(SYMBOLS)
    f.close()
    F.close()


forty_symbols_in_line(File, Filee)