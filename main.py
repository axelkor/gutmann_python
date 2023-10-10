import os
data_pattern = [
    0x55, 0xAA, 0x92_49_24, 0x49_24_92, 0x24_92_49, 0x00, 0x11, 0x22,
    0x33, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB,
    0xCC, 0xDD, 0xEE, 0xFF, 0x92_49_24, 0x49_24_92, 0x24_92_49,
    0x6D_B6_DB, 0xB6_DB_6D, 0xDB_6D_B6,
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
        for i in range(0,4):#a cycle of steps 31-35
            random_pattern = (6*r0+223)%253
            r0 = random_pattern
            write_pattern(file, file_size, random_pattern)
            file.flush()
            file.seek(0)


def write_pattern(file, file_size, pattern):
    bytes_pattern = pattern.to_bytes(4, byteorder='big')
    remaining = file_size % 4
    for _ in range(file_size // 4):
        file.write(bytes_pattern)

    for i in range(remaining):
        file.write(bytes([bytes_pattern[i]]))


if __name__ == "__main__":
    file_to_wipe = "file.txt"  #file name change to u file
    apply_to_file(file_to_wipe)
