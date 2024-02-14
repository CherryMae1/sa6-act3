numbers = [7, 11, -3, -999, 12, 56, 731, -1111]

def maximum(numbers):
  x = numbers[0]
  for i in range(len(numbers)):
    x = find_max(x, numbers[i])
  print(x)


find_max = lambda x, y: x if x > y else y
maximum(numbers)