import numpy as np

test_num = 10000

results = []

wins = []

dices = np.random.randint(1, 7, 2 * test_num)
dices.shape = (test_num, 2)
values = np.sum(dices, axis=1)
for i in values:
    if i == 7:
        results.append(1)
        wins.append(1)
    elif i == 11:
        results.append(1)
        wins.append(1)
    elif i == 2:
        results.append(0)
    elif i == 3:
        results.append(0)
    elif i == 12:
        results.append(0)
    else:
        while True:
            num1_2 = np.random.randint(1, 6)
            num2_2 = np.random.randint(1, 6)
            sum2 = num1_2 + num2_2
            if sum2 == 7:
                results.append(0)
                break
            elif sum2 == i == 6:
                results.append(1)
                wins.append(1)
                break
            elif sum2 == i == 8:
                results.append(1)
                wins.append(1)
                break
            elif sum2 == i == 4:
                results.append(2)
                wins.append(1)
                break
            elif sum2 == i == 10:
                results.append(2)
                wins.append(1)
                break
            elif sum2 == i == 5:
                results.append(1.5)
                wins.append(1)
                break
            elif sum2 == i == 9:
                results.append(1.5)
                wins.append(1)
                break
            elif i == sum2:
                results.append(1)
                wins.append(1)
                break


win_money = sum(results)
persent_of_wins = sum(wins) / test_num
print(f"Виграно всього : {win_money} од. в.")
print(f"Відсоток виграшу : {persent_of_wins}")
print(f"Виграно в середньому: {win_money/test_num}")
