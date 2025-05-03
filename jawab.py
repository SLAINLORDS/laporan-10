handle=open("soal.txt")
for line in handle:
    b=line.strip()
    b=b.lower()
    b=b.split("||")
    print (b[0])
    jawab=input("jawab: ")
    jawab=jawab.lower()
    c=b[1]
    c=c.strip()
    if jawab == c:
        print ("jawaban benar!")
    elif jawab!=c:
        print ("jawaban salah")