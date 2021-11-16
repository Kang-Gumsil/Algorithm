input_data = list(input())

alpha = [c for c in input_data if c.isalpha()]
number = [int(i) for i in input_data if not i.isalpha()]

result = ''.join(sorted(alpha)) + str(sum(number))
print(result)