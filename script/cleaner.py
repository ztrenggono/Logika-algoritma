import pandas as pd
import re
import os

# === Path file di Downloads ===
home = os.path.expanduser("~")
file_path = os.path.join(home, "Downloads", "nama_profile_seller_in_app_sales.csv")

# === Baca CSV ===
df = pd.read_csv(file_path)

# === Fungsi bersihin nama ===
def clean_name(profile):
    # ambil sebelum tanda "-" (misalnya TANTI-V2000 -> TANTI)
    name = re.split(r"[-]", str(profile))[0].strip()
    # hapus karakter aneh (biar cuma huruf, titik, dan spasi)
    name = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ.\s]", "", name)
    return name.strip()

df["clean_name"] = df["profile"].apply(clean_name)

# === Ambil nama unik + filter tambahan ===
unique_names = sorted(
    n for n in df["clean_name"].unique()
    if len(n) >= 3 and not n.upper().startswith("V")  # buang nama aneh & kode V2000
)

# === Print hasil ke terminal ===
print("✅ Daftar nama seller bersih:")
for name in unique_names:
    print("-", name)

# === Simpan hasil ke CSV di Downloads ===
output_path = os.path.join(home, "Downloads", "nama_seller_bersih.csv")
pd.DataFrame(unique_names, columns=["seller_name"]).to_csv(output_path, index=False)

print(f"\n📂 Hasil juga disimpan ke: {output_path}")
