def create_and_write_file(filename):
    with open(filename, 'w') as file:
        file.write("This is Jets\n")
        file.write("19 years old\n")
        file.write("I am gonna become a king\n")

create_and_write_file('intro.txt')
print("FILE CREATED AND WRITTEN SUCCESSFULLY")

def read_and_print_file(filename):
    with open(filename, 'r') as file:
        content=file.read()
        print(content)

read_and_print_file('intro.txt')

def append_to_file(filename, newline):
    with open(filename, 'a') as file:
        file.write(newline + "\n")
    
append_to_file('intro.txt', "In the next 5 years, I am gonna be at peak")
print("LINE APPENDED SUCCESSFULLY")
read_and_print_file('intro.txt')

def print_lines_with_numbers(filename):
    with open(filename, 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")

print_lines_with_numbers('intro.txt')

def count_words(filename):
    with open(filename, 'r') as file:
        content=file.read()
        words=content.split()
        return len(words)
    
word_count=count_words('intro.txt')
print(f"THE FILE CONTAINS {word_count} WORDS.")

