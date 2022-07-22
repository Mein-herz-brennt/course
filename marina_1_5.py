class Line_calculator:
    def __init__(self, string):
        self.nums_params = float(string)
        # for i in range(0, len(self.nums_params)):
        #     print(self.nums_params[i])
        #     if self.nums_params[i] == '+' or '-' or '*' or '/':
        #         del(self.nums_params[i])

    def show(self):
        print(self.nums_params)


if __name__ == '__main__':
    Line_calculator(3 - 2 + 4 / 5 * 6).show()
