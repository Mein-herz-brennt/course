def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class CustomList:
    def __init__(self, num):
        self.n = []
        self.count = 0
        if isint(num):
            self.n.append(int(num))
        else:
            pass
        self.iters = len(self.n)

    def __iter__(self):
        i = 0
        for item in self.n:
            if self.n[i] <= + self.n[i+1]:
                if item % 2 != 0:
                    k = self.n[i]
                    i += 1
                    return k
                else:
                    pass
            elif self.n[i] >= self[i+1]:
                if item % 2 == 0:
                    p = self.n[i]
                    i += 1
                    return p
                else:
                    pass

    def __next__(self):
        if self.count <= self.iters:
            self.count += 1
            return item
        raise StopIteration
