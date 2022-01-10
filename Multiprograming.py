# Anggota Kelompok 10:
# 5200411003 Berkah Fadli Nur Ramadlan
# 5200411114 Aulia Nugraheni
# 5200411178 Muhamad Ali Nugroho Ramadhan
# 5200411348 Ari Fernandez



RAM = float (input  ("Masukkan Kapasitas RAM (GB): "))
SOperasi = float (input("Masukkan Sistem Operasi (GB): "))
program1 = float (input("Masukkan Ukuran Program 1 (GB): "))
program2 = float (input("Masukkan Ukuran Program 2 (GB): "))
program3 = float (input("Masukkan Ukuran Program 3 (GB): "))

Terpakai = SOperasi + program1 + program2 + program3

Sisa = RAM - Terpakai

print ("Sisa Ram yang Tidak Terpakai adalah", Sisa, "GB")
