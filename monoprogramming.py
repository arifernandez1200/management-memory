# Anggota Kelompok 10:
# 5200411003 Berkah Fadli Nur Ramadlan
# 5200411114 Aulia Nugraheni
# 5200411178 Muhamad Ali Nugroho Ramadhan
# 5200411348 Ari Fernandez



RAM = float (input  ("Masukkan Kapasitas RAM (GB): "))
SOperasi = float (input("Masukkan Sistem Operasi (GB): "))
Terpakai = float (input("Masukkan Memori yang Terpakai(GB): "))

Sisa = RAM - SOperasi - Terpakai

print ("Sisa Ram yang Tidak Terpakai adalah", Sisa, "GB")


