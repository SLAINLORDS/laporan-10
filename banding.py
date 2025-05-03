def banding(file1,file2):
    handle1 = open(file1)
    handle2 = open(file2)

    baris = 1

    for line1, line2 in zip(handle1, handle2):
        if line1 != line2:
            print(f"Perbedaan pada baris {baris}:")
            print(f"File1: {line1.strip()}")
            print(f"File2: {line2.strip()}")

        baris += 1

    handle1.close()
    handle2.close()
file1=("teks1.txt")
file2=("teks2.txt")
banding(file1,file2)