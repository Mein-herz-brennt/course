class Len_file:
    def __init__(self, filename):
        self.f = filename
        self.list = ''

    def len_words(self):
        with open(self.f, 'r', encoding='utf-8') as f:
            self.list = f.read()
            word = self.list.split()
        return len(word)

    def len_symbols(self):
        letters = 0
        # symbol = ""
        with open(self.f, 'r', encoding='utf-8') as f:
            for line in f:
                letters += len(list(line))
                print(list(line))
        return letters

    def len_lines(self):
        lines = 0  # кількість рядків
        with open(self.f, 'r', encoding='utf-8') as f:
            for line in f:
                lines += 1
            return lines


a = Len_file('input').len_words()
print('кількість слів', a)
b = Len_file('input').len_lines()
print('кільксть рядків', b)
c = Len_file('input').len_symbols()
print("кількість літер", c)
s = list('abnmzvdfnfxnqwewsfghdhgfdfjfj')
print(len(s))
