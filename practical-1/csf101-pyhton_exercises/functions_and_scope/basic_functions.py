def greet(name):
    print(f"Hello, {name}!")

greet("Jets")

def square(num):
    return num**2

number=14
print(square(number))

def print_numbers(n):
    for i in range(1,n+1):
        print(i, end=" ")

print_numbers(10)
 
print()
def is_even(number):
    return number%2==0

print(is_even(8))
print(is_even(5))
