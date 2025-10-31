total_detik = int(input("Masukkan total detik: "))

jam = total_detik // 3600
sisa = total_detik % 3600
menit = sisa // 60
detik = sisa % 60

print(f"{jam} jam, {menit} menit, {detik} detik")
