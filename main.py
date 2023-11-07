import os
data_pattern = [
    0x55, 0xAA, [0x92,0x49,0x24], 0x55, 0xAA,[0x92,0x49,0x24], [0x49,0x24,0x92], [0x24,0x92,0x49]
]#A pattern of steps 4 to 31


def apply_to_file(file_path):#function which write to file text and pattern
    r0 = len("Oleksandr")#nameLength
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb+') as file:
        for i in range(0,4):#a cycle of steps 1-4
            random_pattern = (6*r0+223)%253
            r0=random_pattern
            write_pattern(file, file_size, random_pattern)
            file.flush()
            file.seek(0)

        for pattern in data_pattern:#a cycle of steps 4-31

            write_pattern(file, file_size, pattern)
            file.flush()
            file.seek(0)
        for i in range(0,4): # a cycle of steps 31 - 35
            random_pattern = (6*r0+223) % 253
            r0 = random_pattern
            write_pattern(file, file_size, random_pattern)
            file.flush()
            file.seek(0)


def write_pattern(file, file_size, pattern):
    if type(pattern)==int:#for pattern with 1 byte

        if type(pattern) == int:
            bytes_pattern = pattern.to_bytes(1, byteorder='big')
            for _ in range(file_size):
                file.write(bytes(bytes_pattern))

    elif type(pattern)==list:#for pattern with 3 byte
        remaining = file_size % 3
        for i in range(file_size//3):
            j=i%3
            bytes_pattern = pattern[j].to_bytes(1, byteorder='big')
            file.write(bytes_pattern)
        for i in range(remaining):
            file.write(bytes(bytes_pattern))



if __name__ == "__main__":
    file_to_wipe = "file.txt"  #file name change to u file
    apply_to_file(file_to_wipe)
    os.remove("file.txt")
