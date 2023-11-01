# list kosong data mahasiswa
data_mahasiswa =[]
# memasukkan data mahasiswa
d = int(input("masukkan jumlah mahasiswa :"))
for i in range(d):
    print(f"Masukkan data mahasiswa ke-{i + 1}:")
    nim = int(input("NIM: "))
    nama = str(input("Nama: ")).lower()
    alamat = input("Alamat: ")
    prodi = str(input("Program Studi: ")).lower()
    datamh = (nim,nama,alamat,prodi)
    data_mahasiswa.append(datamh)
# mencari data berdasarkan prodi
cari_prodi = str(input("Cari mahasiswa berdasarkan prodi :")).lower()
hasil_cari = []

for data in data_mahasiswa:
    if cari_prodi == data[3]:
        hasil_cari.append(data)
# mencetak hasil pencarian berdasarkan prodi
if hasil_cari:
    print(f"Hasil Pencarian Mahasiswa Program Studi {cari_prodi}:")
    for data in hasil_cari:
        print(f"NIM: {data[0]}, Nama: {data[1]}, Alamat: {data[2]}, Prodi: {data[3]}")
else:
    print(f"Tidak ada data Mahasiswa dengan Program Studi {cari_prodi}")