handle=open("daftarbuku.txt")
cari=input("massukan judul yang dicari: ")
b=False
for line in handle:
    a=line.split(",")
    judul=(a[0])
    if cari==judul:
        print (f"judul:{a[0]}")
        print (f"kode:{a[1]}")
        print (f"tanggal:{a[2]}")
        print (f"description:{a[3]}")
        b=True

if b==False:
    print ("buku tidak ditemukan silahkan mencari lagi")
