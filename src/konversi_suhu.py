print("=== PROGRAM KONVERSI SUHU ===")
suhu = float(input("NILAI: "))
satuan = input("TIPE (C / F / K): ").strip().upper()

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
    print("input tidak valid")

print("\n--- Hasil Konversi ---")
print(f"Celsius    : {c:.2f} °C")
print(f"Fahrenheit : {f:.2f} °F")
print(f"Kelvin     : {k:.2f} K")