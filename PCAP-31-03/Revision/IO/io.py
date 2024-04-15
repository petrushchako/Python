with open("fileIO.txt") as file:
    print(file.readlines())

    #file.seek(0)
    for line in file:
        print(line.strip())

with open("fileIO.txt", "a") as file:
    txt = "Additional text\n"
    file.write(txt)


# Binary data to write
binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21'

# Open a file in binary write mode ('wb')
with open("binary_data.bin", "wb") as file:
    # Write the binary data to the file
    file.write(binary_data)


# Open the file in binary read mode ('rb')
with open("binary_data.bin", "rb") as file:
    # Read the entire contents of the file into a bytes object
    binary_data_read = file.read()
    print("Binary data read from file:")
    print(binary_data_read)

    # Alternatively, you can read the file byte by byte
    print("\nBinary data read byte by byte:")
    file.seek(0)  # Reset the file pointer to the beginning of the file
    byte = file.read(1)
    while byte:
        print(byte)
        byte = file.read(1)