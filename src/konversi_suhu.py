"""
Program Konversi Suhu Modular
Mendukung input dan konversi antar skala Celsius, Fahrenheit, dan Kelvin.
"""

def get_input_suhu():
    """
    Fungsi 1: Mengambil dan memvalidasi input nilai suhu serta satuan dari pengguna.
    Commit: feat(suhu): tambahkan fungsi get_input_suhu untuk validasi input pengguna
    """
    print("=== PROGRAM KONVERSI SUHU ===")
    
    # Validasi input nilai angka
    while True:
        try:
            suhu = float(input("Masukkan nilai suhu: "))
            break
        except ValueError:
            print("[Error] Harap masukkan angka yang valid!")

    # Validasi input satuan
    satuan_valid = ['C', 'F', 'K']
    while True:
        satuan = input("Masukkan satuan asal (C / F / K): ").strip().upper()
        if satuan in satuan_valid:
            break
        print("[Error] Satuan tidak valid! Gunakan C, F, atau K.")

    return suhu, satuan


def hitung_konversi(suhu, satuan):
    """
    Fungsi 2: Menghitung konversi suhu ke skala Celsius, Fahrenheit, dan Kelvin.
    Commit: feat(suhu): tambahkan fungsi hitung_konversi untuk memproses rumus C/F/K
    """
    if satuan == 'C':
        c = suhu
        f = (suhu * 9/5) + 32
        k = suhu + 273.15
    elif satuan == 'F':
        c = (suhu - 32) * 5/9
        f = suhu
        k = c + 273.15
    elif satuan == 'K':
        c = suhu - 273.15
        f = (c * 9/5) + 32
        k = suhu
    else:
        raise ValueError("Satuan tidak dikenali.")

    return c, f, k


def tampilkan_hasil(c, f, k):
    """
    Fungsi 3: Mencetak hasil konversi suhu secara terformat ke layar.
    Commit: feat(suhu): tambahkan fungsi tampilkan_hasil untuk mencetak output terformat
    """
    print("\n--- Hasil Konversi ---")
    print(f"Celsius    : {c:.2f} °C")
    print(f"Fahrenheit : {f:.2f} °F")
    print(f"Kelvin     : {k:.2f} K")


if __name__ == "__main__":
    # Menjalankan rangkaian fungsi utama
    nilai_suhu, satuan_asal = get_input_suhu()
    celsius, fahrenheit, kelvin = hitung_konversi(nilai_suhu, satuan_asal)
    tampilkan_hasil(celsius, fahrenheit, kelvin)