number = 12345

sum_digit = lambda x: int(x)
solution = sum(sum_digit(i) for i in str(number))
print(solution)