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




if __name__ == "__main__":
    # Menjalankan rangkaian fungsi utama
    nilai_suhu, satuan_asal = get_input_suhu()