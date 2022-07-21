"""
https://www.e-olymp.com/uk/submissions/7626697
"""

arguments = list(input().split())
array = list(input().split())
array = map(int, array)

array = sorted(array)
print(array[int(arguments[1])-1])