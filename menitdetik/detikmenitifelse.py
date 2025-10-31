def convert_total_seconds(total_detik: int):
    """Konversi total detik ke (jam, menit, detik)."""
    jam = total_detik // 3600
    sisa = total_detik % 3600
    menit = sisa // 60
    detik = sisa % 60
    return jam, menit, detik


def main():
    try:
        raw = input("Masukkan total detik (integer >= 0): ").strip()
        total_detik = int(raw)
    except ValueError:
        print("❌ Input harus bilangan bulat (integer). Program dihentikan.")
        return

    if total_detik < 0:
        print("❌ Input tidak boleh negatif. Program dihentikan.")
        return

    jam, menit, detik = convert_total_seconds(total_detik)
    print(f"Hasil: {jam} jam, {menit} menit, {detik} detik")


if __name__ == "__main__":
    main()
