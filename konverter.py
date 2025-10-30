def konversi_panjang():
    meter = float(input("Masukkan panjang (meter): "))
    kilometer = meter / 1000
    print(f"{meter} meter = {kilometer} kilometer")

def konversi_berat():
    gram = float(input("Masukkan berat (gram): "))
    kilogram = gram / 1000
    print(f"{gram} gram = {kilogram} kilogram")

def konversi_suhu():
    celsius = float(input("Masukkan suhu (°C): "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

def main():
    print("=== Konverter Satuan Sederhana ===")
    print("1. Panjang (meter -> kilometer)")
    print("2. Berat (gram -> kilogram)")
    print("3. Suhu (Celsius -> Fahrenheit)")

    pilihan = input("Pilih jenis konversi (1/2/3): ")

    if pilihan == "1":
        konversi_panjang()
    elif pilihan == "2":
        konversi_berat()
    elif pilihan == "3":
        konversi_suhu()
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
