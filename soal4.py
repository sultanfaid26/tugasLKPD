total_detik = int(input("masukan total detik: "))
jam = int()
menit = int()
detik = int()

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60


print(jam,"Jam",menit,"Menit",detik,"Detik")