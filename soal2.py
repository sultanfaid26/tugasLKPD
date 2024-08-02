bil1= int(input("Masukkan bilangan pertama: "))
bil2= int(input("Masukkan bilangan kedua: "))
bil3= int(input("Masukkan bilangan Ketiga: "))

if bil1 > bil2 and bil1 > bil3 :
    print(f"Bilangan {bil1} adalah bilangan terbesar")
elif bil2 > bil1 and bil2 > bil3 :
    print(f"Bilangan {bil2} adalah bilangan terbesar")
else:
    print(f"Bilangan {bil3} adalah bilangan terbesar")