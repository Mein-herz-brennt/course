import numpy as np
import json


def krap(n: int):
    results = []
    for i in range(n):
        num1 = np.random.randint(1, 6)
        num2 = np.random.randint(1, 6)
        suma = num1 + num2
        if suma == 7:
            results.append(1)
        elif suma == 11:
            results.append(1)
        elif suma == 2:
            results.append(0)
        elif suma == 3:
            results.append(0)
        elif suma == 11:
            results.append(0)
        else:
            while True:
                num1_2 = np.random.randint(1, 6)
                num2_2 = np.random.randint(1, 6)
                sum2 = num1_2 + num2_2
                if sum2 == 7:
                    results.append(0)
                    break
                elif sum2 == suma == 6:
                    results.append(1)
                    break
                elif sum2 == suma == 8:
                    results.append(1)
                    break
                elif sum2 == suma == 4:
                    results.append(2)
                    break
                elif sum2 == suma == 10:
                    results.append(2)
                    break
                elif sum2 == suma == 5:
                    results.append(1.5)
                    break
                elif sum2 == suma == 9:
                    results.append(1.5)
                    break
                elif suma == sum2:
                    results.append(1)
                    break
    return sum(results), n


money = krap(10000)
with open("dx20_05.json", "w") as file:
    information = {"data": []}
    for i in range(100):
        money = krap(10000)
        win_or_lose_money = {"money": money[1] - money[0]}
        information["data"].append(win_or_lose_money)
    json.dump(information, file, indent=3)
