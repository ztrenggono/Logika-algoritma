from sklearn.linear_model import LinearRegression
import numpy as np

# Data: luas rumah (m²)
luas = np.array([30, 50, 80, 100, 120, 150, 200]).reshape(-1, 1)
# Data: harga rumah (juta)
harga = np.array([200, 350, 500, 650, 800, 1000, 1300])

# Buat model
model = LinearRegression()
model.fit(luas, harga)

# Prediksi harga rumah dengan luas tertentu
luas_baru = float(input("Masukkan luas rumah (m²): "))
prediksi = model.predict([[luas_baru]])

print(
    f"\nPerkiraan harga untuk {luas_baru} m² adalah sekitar {prediksi[0]:.2f} juta rupiah."
)
