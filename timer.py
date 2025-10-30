import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner(seconds):
    spin_chars = ['|', '/', '-', '\\']
    start = time.time()
    while time.time() - start < seconds:
        for char in spin_chars:
            elapsed = int(time.time() - start)
            remaining = seconds - elapsed
            percent = (elapsed / seconds) * 100
            bar_len = 25
            filled = int(bar_len * elapsed / seconds)
            bar = '█' * filled + '-' * (bar_len - filled)
            sys.stdout.write(
                f"\r{char}  [{bar}] {percent:5.1f}% | {elapsed}s / {seconds}s"
            )
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r✅  [█████████████████████████] 100.0% | Done!\n")

def timer():
    clear()
    print("=== CLI Timer Interaktif by Zaldi  ===")
    try:
        seconds = int(input("Masukkan waktu (detik): "))
        clear()
        print("Mulai dalam 3...")
        time.sleep(1)
        clear()
        print("Mulai dalam 2...")
        time.sleep(1)
        clear()
        print("Mulai dalam 1...")
        time.sleep(1)
        clear()
        print("🚀 Timer dimulai!\n")
        spinner(seconds)
    except ValueError:
        print("⚠️ Input harus berupa angka!")

if __name__ == "__main__":
    timer()
