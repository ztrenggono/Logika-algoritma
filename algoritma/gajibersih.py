# input : nama_karyawan, gaji_pokok,
# proses: tunjangan =  ( gaji_pokok * 20 % )
#       : pajak = gaji_pokok + tunjangan * 15%
# output : gaji_bersih = gaji_pokok + tunjangan - pajak

input_nama_karyawan = input("Masukkan nama karyawan: ")
input_gaji_pokok = float(input("Masukkan gaji pokok: "))

tunjangan = input_gaji_pokok * 0.20
pajak = input_gaji_pokok + tunjangan * 0.15
gaji_bersih = input_gaji_pokok + tunjangan - pajak

print(f"Nama Karyawan: {input_nama_karyawan}")
print(f"Gaji Bersih: {gaji_bersih:.2f}")
