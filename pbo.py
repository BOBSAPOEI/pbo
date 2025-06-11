def kalkulator_nilai():
    try:
        # Meminta input jumlah mahasiswa
        jumlah_mhs = int(input("Masukkan jumlah mahasiswa yang ingin diinput: "))
        
        if jumlah_mhs < 1:  # Validasi: Jumlah mahasiswa harus minimal 1
            print("Error: Jumlah mahasiswa harus lebih dari 0.")
            return
        
        nilai_list = []  # List untuk menyimpan nilai-nilai
        
        for i in range(jumlah_mhs):
            while True:  # Loop untuk validasi input nilai
                try:
                    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1} (0-100): "))
                    
                    if nilai < 0 or nilai > 100:  # Validasi: Nilai harus antara 0 dan 100
                        print("Error: Nilai harus antara 0 dan 100. Silakan coba lagi.")
                    else:
                        nilai_list.append(nilai)  # Tambahkan nilai ke list
                        break  # Keluar dari loop jika valid
                except ValueError:  # Penanganan exception untuk input non-angka
                    print("Error: Input harus berupa angka. Silakan coba lagi.")
        
        if nilai_list:  # Hitung rata-rata jika ada nilai
            rata_rata = sum(nilai_list) / len(nilai_list)
            print(f"Rata-rata nilai dari {jumlah_mhs} mahasiswa adalah: {rata_rata:.2f}")
        else:
            print("Tidak ada nilai yang valid untuk dihitung.")
    
    except ValueError:  # Penanganan exception untuk input jumlah mhs yang salah
        print("Error: Jumlah mahasiswa harus berupa angka bulat positif.")
    except Exception as e:  # Penanganan exception umum
        print(f"Terjadi kesalahan: {e}")

# Jalankan program
kalkulator_nilai()