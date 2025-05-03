handle1=open("teks1.txt")
handle2=open("teks2.txt")
for line in handle1:
    a=line
    for baris in handle2:
        b=baris
    if a!=b:
        print (F"{a} berbeda dengan {b}")
        print()
