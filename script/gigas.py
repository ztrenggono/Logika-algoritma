#!/usr/bin/env python3
"""
Script untuk enkripsi dan dekripsi text
Menggunakan metode Caesar Cipher dan Base64
"""

import base64
from typing import Union


def caesar_encrypt(text: str, shift: int = 3) -> str:
    """
    Enkripsi text menggunakan Caesar Cipher

    Args:
        text: Text yang akan dienkripsi
        shift: Jumlah pergeseran karakter (default: 3)

    Returns:
        Text yang sudah dienkripsi
    """
    result = ""

    for char in text:
        if char.isalpha():
            # Tentukan apakah huruf besar atau kecil
            ascii_offset = ord("A") if char.isupper() else ord("a")
            # Geser karakter
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Karakter non-alfabet tetap sama
            result += char

    return result


def caesar_decrypt(text: str, shift: int = 3) -> str:
    """
    Dekripsi text dari Caesar Cipher

    Args:
        text: Text yang akan didekripsi
        shift: Jumlah pergeseran karakter (default: 3)

    Returns:
        Text yang sudah didekripsi
    """
    # Dekripsi adalah enkripsi dengan shift negatif
    return caesar_encrypt(text, -shift)


def base64_encrypt(text: str) -> str:
    """
    Enkripsi text menggunakan Base64

    Args:
        text: Text yang akan dienkripsi

    Returns:
        Text yang sudah dienkripsi dalam format Base64
    """
    text_bytes = text.encode("utf-8")
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode("utf-8")


def base64_decrypt(encrypted_text: str) -> str:
    """
    Dekripsi text dari Base64

    Args:
        encrypted_text: Text terenkripsi dalam format Base64

    Returns:
        Text yang sudah didekripsi
    """
    try:
        base64_bytes = encrypted_text.encode("utf-8")
        text_bytes = base64.b64decode(base64_bytes)
        return text_bytes.decode("utf-8")
    except Exception as e:
        return f"Error: Tidak dapat mendekripsi - {str(e)}"


def double_encrypt(text: str, shift: int = 3) -> str:
    """
    Enkripsi ganda: Caesar Cipher + Base64

    Args:
        text: Text yang akan dienkripsi
        shift: Jumlah pergeseran untuk Caesar Cipher

    Returns:
        Text yang sudah dienkripsi dua kali
    """
    caesar_encrypted = caesar_encrypt(text, shift)
    return base64_encrypt(caesar_encrypted)


def double_decrypt(encrypted_text: str, shift: int = 3) -> str:
    """
    Dekripsi ganda: Base64 + Caesar Cipher

    Args:
        encrypted_text: Text terenkripsi
        shift: Jumlah pergeseran untuk Caesar Cipher

    Returns:
        Text yang sudah didekripsi
    """
    base64_decrypted = base64_decrypt(encrypted_text)
    if base64_decrypted.startswith("Error:"):
        return base64_decrypted
    return caesar_decrypt(base64_decrypted, shift)


def main():
    """Fungsi utama untuk menjalankan program"""
    print("=" * 50)
    print("PROGRAM ENKRIPSI DAN DEKRIPSI TEXT")
    print("=" * 50)

    while True:
        print("\nPilih metode:")
        print("1. Caesar Cipher")
        print("2. Base64")
        print("3. Double Encryption (Caesar + Base64)")
        print("4. Keluar")

        pilihan = input("\nMasukkan pilihan (1-4): ").strip()

        if pilihan == "4":
            print("Terima kasih! Program selesai.")
            break

        if pilihan not in ["1", "2", "3"]:
            print("Pilihan tidak valid!")
            continue

        print("\nPilih operasi:")
        print("1. Enkripsi")
        print("2. Dekripsi")

        operasi = input("Masukkan pilihan (1-2): ").strip()

        if operasi not in ["1", "2"]:
            print("Pilihan tidak valid!")
            continue

        text = input("\nMasukkan text: ").strip()

        if not text:
            print("Text tidak boleh kosong!")
            continue

        # Caesar Cipher
        if pilihan == "1":
            try:
                shift = int(input("Masukkan shift (default: 3): ").strip() or "3")
            except ValueError:
                shift = 3
                print("Menggunakan shift default: 3")

            if operasi == "1":
                hasil = caesar_encrypt(text, shift)
                print(f"\nText terenkripsi: {hasil}")
            else:
                hasil = caesar_decrypt(text, shift)
                print(f"\nText terdekripsi: {hasil}")

        # Base64
        elif pilihan == "2":
            if operasi == "1":
                hasil = base64_encrypt(text)
                print(f"\nText terenkripsi: {hasil}")
            else:
                hasil = base64_decrypt(text)
                print(f"\nText terdekripsi: {hasil}")

        # Double Encryption
        elif pilihan == "3":
            try:
                shift = int(
                    input("Masukkan shift untuk Caesar (default: 3): ").strip() or "3"
                )
            except ValueError:
                shift = 3
                print("Menggunakan shift default: 3")

            if operasi == "1":
                hasil = double_encrypt(text, shift)
                print(f"\nText terenkripsi: {hasil}")
            else:
                hasil = double_decrypt(text, shift)
                print(f"\nText terdekripsi: {hasil}")

        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()
