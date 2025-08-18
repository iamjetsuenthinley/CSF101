def create_binary_files(filename):
    data=bytes([0,1,2,3,4,5])
    with open(filename, 'wb') as file:
        file.write(data)

create_binary_files('binary_sample.bin')
print("BINARY FILE CREATED SUCCESSFULLY")

def read_binary_files(filename):
    with open (filename, 'rb') as file:
        content= file.read()
        print("Binary Content: ", content)

read_binary_files('binary_sample.bin')

def append_to_bianry_file(filename, data):
    with open(filename, 'ab') as file:
        file.write(data)

append_to_bianry_file('binary_sample.bin', bytes([6,7,8,9]))
print("BYTES APPENDED TO BINARY FILE.")
read_binary_files('binary_sample.bin')

