#!/usr/bin/env python3
import os
import random
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# ==== KONFIG POSTGRES ====
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "eskulgo",
    "user": "ztrenggono",
    "password": "zaldi100",
}

# ==== FILE EXCEL ====
EXCEL_PATH = "/home/ztrenggono/Downloads/data_siswa_new.xlsx"   # ganti dengan path Anda

# ==== LIST ID ESKUL YANG VALID (WAJIB TIDAK KOSONG) ====
ESKUL_IDS = [1, 2, 3]

# ==== NAMA TABEL ====
TABLE_NAME = "siswa"

# ==== UTIL: cari kolom di Excel secara fleksibel ====
def find_col(df, candidates):
    """
    df: DataFrame
    candidates: list nama kandidat (case-insensitive, tanpa spasi/underscore)
    return: nama kolom di df yang match (or raise)
    """
    norm = {c.lower().replace(" ", "").replace("_", ""): c for c in df.columns}
    for cand in candidates:
        key = cand.lower().replace(" ", "").replace("_", "")
        if key in norm:
            return norm[key]
    raise KeyError(f"Tidak menemukan kolom untuk kandidat: {candidates}. Kolom Excel: {list(df.columns)}")

def main():
    if not ESKUL_IDS:
        raise ValueError("Daftar ESKUL_IDS kosong. Isi dengan id eskul yang valid, mis. [1,2,3].")

    # --- Baca Excel ---
    df = pd.read_excel(EXCEL_PATH)

    # Deteksi kolom
    col_nis = find_col(df, ["nis"])
    col_nama = find_col(df, ["nama", "nama_lengkap", "namalengkap"])
    col_rayon = find_col(df, ["rayon"])

    # Ambil kolom yang dibutuhkan
    sub = df[[col_nis, col_nama, col_rayon]].copy()

    # Bersihkan & tipe data
    sub[col_nis] = sub[col_nis].astype(str).str.strip()              # nis ke varchar
    sub[col_nama] = sub[col_nama].astype(str).str.strip()
    sub[col_rayon] = sub[col_rayon].astype(str).str.strip()

    # Hilangkan baris kosong NIS (opsional)
    sub = sub[sub[col_nis].str.len() > 0]

    # Tambahkan kolom id_eskul secara acak
    sub["id_eskul"] = [random.choice(ESKUL_IDS) for _ in range(len(sub))]

    # Siapkan records untuk batch insert
    # urutan kolom harus sesuai dengan query INSERT
    records = list(
        sub[[col_nis, col_nama, col_rayon, "id_eskul"]].itertuples(index=False, name=None)
    )

    if not records:
        print("Tidak ada data yang akan diinsert.")
        return

    # --- Koneksi & INSERT ---
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        with conn, conn.cursor() as cur:
            insert_sql = f"""
                INSERT INTO {TABLE_NAME} (nis, nama_lengkap, rayon, id_eskul)
                VALUES %s
            """
            # Jika Anda sudah punya UNIQUE constraint pada nis,
            # dan ingin upsert, ganti insert_sql jadi:
            #
            # insert_sql = f"""
            #   INSERT INTO {TABLE_NAME} (nis, nama_lengkap, rayon, id_eskul)
            #   VALUES %s
            #   ON CONFLICT (nis) DO UPDATE
            #   SET nama_lengkap = EXCLUDED.nama_lengkap,
            #       rayon = EXCLUDED.rayon,
            #       id_eskul = EXCLUDED.id_eskul,
            #       updated_at = NOW()
            # """
            execute_values(cur, insert_sql, records)
        print(f"Sukses insert {len(records)} baris ke tabel {TABLE_NAME}.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
