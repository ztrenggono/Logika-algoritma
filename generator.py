import random
import string
import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(text, duration=2):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for s in spinner:
            sys.stdout.write(f'\r{text} {s}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(text) + 2) + '\r')

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    clear()
    print("=== 🔐 Password Generator Interaktif ===")
    try:
        length = int(input("Panjang password: "))
        print()
        loading_animation("🔄 Generating password...")
        password = generate_password(length)
        print(f"\n✅ Password kamu: {password}\n")
    except ValueError:
        print("⚠️ Masukkan angka yang valid!")

if __name__ == "__main__":
    main()
