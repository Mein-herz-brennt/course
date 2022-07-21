# https://www.e-olymp.com/uk/submissions/7855006 
import collections

n = int(input())
cubes = list(input())

cubes = [item for item, count in collections.Counter(cubes).items() if count % 2 != 0]
if len(cubes) == 0:
    print("Ok")
else:
    print(cubes[0])
