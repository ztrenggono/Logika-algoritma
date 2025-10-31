# Input
jam = int(input("Masukkan jam: "))
menit = int(input("Masukkan menit: "))
detik = int(input("Masukkan detik: "))

# Validasi input
if jam >= 0 and menit >= 0 and detik >= 0:
    if menit <= 59 and detik <= 59:
        total_detik = (jam * 3600) + (menit * 60) + detik
        print(f"Total detik: {total_detik}")
    else:
        print("❌ Menit dan detik tidak boleh lebih dari 59!")
else:
    print("❌ Input tidak boleh negatif!")
