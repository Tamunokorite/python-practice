'''

This code will add five to a list of numbers and print the equation and result

'''

numbers = [i for i in range(0, 41)]

five_added = list(map(lambda x: (x + 5), numbers))

len_numbers = len(numbers)

for i in range(len_numbers):
    print(f"{numbers[i]} + 5 = {five_added[i]}")