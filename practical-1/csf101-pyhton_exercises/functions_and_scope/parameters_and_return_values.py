def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Jets")

def calculate_rectangle_area(width, height):
    return width*height

area=calculate_rectangle_area(10, 4)
print("The area of the rectangle is: {area}")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Jets", age=19, city="Gelephu Mindfulness")

def min_max(numbers):
    return min(numbers), max(numbers)

result=min_max([5,8,12,14,24,])
print(f"{result[0]}, Max:{result[1]}")

def safe_divide(a, b):
    if b==0:
        return "The difference is infinite"
    return a/b
print(safe_divide(14,7))
print(safe_divide(3,0))
