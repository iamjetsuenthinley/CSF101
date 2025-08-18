import os
import shutil
import csv

def create_sample_file(filename):
    with open(filename, 'w') as file:
        file.write("Sample file.\n")
create_sample_file('sample.txt')

def file_exists(filename):
    return os.path.exists(filename)

print(f"'sample.txt' exists: {file_exists('sample.txt')}")
print(f"'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

rename_file('sample.txt','renamed_sample.txt')
print("fILE RENAMED SUCCESSFULLY.")
print(f"'renamed_sample.txt' exists: {file_exists('renamed_sample.txt')}")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} HAS BEEN DELETED.")
    else: 
        print(f"{filename} DOES NOT EXIST.")

delete_file('binary_sample.bin')

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"DIRECTORY '{directory_name}' CREATED SUCCESSFULLY.")
    else:
        print(f"DIRECTORY '{directory_name}' ALREADY EXISTS.")

create_directory('new_folder')

def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)

print("FILES IN THE CURRENT DIRECTORY:")
list_files('.')

def copy_file(source, destination):
    shutil.copy2(source, destination)
    print(f"File copied from {source} to {destination}")

copy_file('renamed_sample.txt', 'new_folder/copied_sample.txt')

def read_csv_file(filename):
    with open(filename, 'r', newline='') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            print(", ".join(row))

with open('sample.csv', 'w', newline='') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Jets', '19', 'Gelephu Mindfulness'])
    csv_writer.writerow(['LeBron', '39', 'Los Angeles'])

print("CONTENTS OF sample.csv:")
read_csv_file('sample.csv')