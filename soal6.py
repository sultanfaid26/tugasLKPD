nilai = []
nilai_tertinggi = 0
jumlah_tertinggi = 0

for i in range(10) :
    nilai_input = int(input(f"Masukan nilai ke-{i+1} :"))
    nilai.append(nilai_input)
    
    if nilai_input > nilai_tertinggi:
        nilai_tertinggi = nilai_input
        jumlah_tertinggi = 1
    elif nilai_input == nilai_tertinggi:
        jumlah_tertinggi += 1

print(f"Nilai tertinggi yang didapat siswa: {nilai_tertinggi}")
print(f"Jumlah siswa yang mendapat nilai tertinggi: {jumlah_tertinggi}")