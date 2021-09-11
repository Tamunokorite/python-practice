'''

This code will print out all even numbers between 1 and a number entered by the user
using the built-in filter function and a lambda function

'''

n = int(input("Enter number: "))

numbers = [i for i in range(1, n)]

even_numbers = filter(lambda x: (x % 2 == 0), numbers)

print(f"The even numbers between 1 and {n} are:")

for i in even_numbers:
    print(i)