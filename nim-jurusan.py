def input_data_mahasiswa():
    try:
        nim = input("Masukkan NIM (10 digit angka): ")
        
        # Validasi NIM
        if not nim.isdigit() or len(nim) != 10:
            print("Error: NIM harus terdiri dari 10 digit angka.")
            return

        jurusan = input("Masukkan jurusan: ")
        
        if not jurusan:
            print("Error: Jurusan tidak boleh kosong.")
            return

        print("\nData Mahasiswa:")
        print(f"NIM     : {nim}")
        print(f"Jurusan : {jurusan}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan program
if __name__ == "__main__":
    input_data_mahasiswa()
