# input : nama_karyawan, gaji_pokok,
# proses: tunjangan =  ( gaji_pokok * 20 % )
#       : pajak = gaji_pokok + tunjangan * 15%
# output : gaji_bersih = gaji_pokok + tunjangan - pajak

# input
nama_karyawan = input("Masukkan nama karyawan: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# proses
tunjangan = gaji_pokok * 0.20
pajak = (gaji_pokok + tunjangan) * 0.15
gaji_bersih = gaji_pokok + tunjangan - pajak

# output
print("\n=== Rincian Gaji Karyawan ===")
print("Nama Karyawan :", nama_karyawan)
print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
print(f"Tunjangan     : Rp {tunjangan:,.2f}")
print(f"Pajak         : Rp {pajak:,.2f}")
print(f"Gaji Bersih   : Rp {gaji_bersih:,.2f}")
