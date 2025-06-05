def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi nol!"
    return a / b

print("=== KALKULATOR SEDERHANA ===")
print("Operasi yang tersedia: +  -  *  /")

angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Pilih operasi (+ - * /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    hasil = tambah(angka1, angka2)
elif operasi == "-":
    hasil = kurang(angka1, angka2)
elif operasi == "*":
    hasil = kali(angka1, angka2)
elif operasi == "/":
    hasil = bagi(angka1, angka2)
else:
    hasil = "Operasi tidak valid"

print(f"Hasil: {hasil}")
