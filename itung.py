handle=open("mbox-short.txt")
hasil = handle.read()
print("Ukuran: ",len(hasil),"bytes")
print("Huruf dari belakang sendiri mundur 16 huruf adalah: " + hasil[-16::1])