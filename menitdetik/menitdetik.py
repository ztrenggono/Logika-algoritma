total_jam = int(input("Masukkan total jam: "))
total_menit = int(input("Masukkan total menit: "))
total_detik = int(input("Masukkan total detik: "))

jam = total_jam * 3600
menit = total_menit * 60
detik = total_detik

total_detik = jam + menit + detik

print(f"Total detik: {total_detik}")
