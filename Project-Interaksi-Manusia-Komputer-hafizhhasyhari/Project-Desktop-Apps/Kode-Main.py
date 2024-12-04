import tkinter as tk
from tkinter import ttk
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Simulasi data untuk model prediksi
def simulate_data():
    return np.random.rand(1, 10)  # Data pasien simulatif

# Fungsi untuk memproses prediksi
def process_prediction():
    data = simulate_data()
    result = model.predict(data)
    prediction_label.config(text=f"Prediction: {result[0][0]:.4f}")

# Membuat model Neural Network sederhana
def create_model():
    model = Sequential()
    model.add(Dense(10, input_dim=10, activation='relu'))
    model.add(Dense(5, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Membuat GUI dengan Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Aplikasi Sistem Penanganan Medis")
    root.geometry("600x400")

    # Title label
    ttk.Label(root, text="Aplikasi Medis Berbasis Nanorobot", font=("Arial", 16)).pack(pady=10)

    # Buttons
    ttk.Button(root, text="Simulasi Data Pasien", command=process_prediction).pack(pady=20)
    ttk.Label(root, text="Hasil Prediksi AI:").pack(pady=5)

    global prediction_label
    prediction_label = ttk.Label(root, text="Prediction: N/A", font=("Arial", 12))
    prediction_label.pack(pady=10)

    # Run the GUI
    root.mainloop()

# Program Utama
if __name__ == "__main__":
    print("Initializing AI model...")
    model = create_model()
    print("Model ready.")
    create_gui()
