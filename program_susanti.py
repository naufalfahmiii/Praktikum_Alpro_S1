# # Membuat data diri awal Susanti
data_awal ={
    'Nama' : input("nama mahasiswi :"),
    'Alamat': input("alamat awal :"),
    'prodi' : input("prodi awal :"),
    'Semester' : input("semester saat ini :"),
    'Angkatan' : input("angkatan tahun :")
}
# # Menampilkan data diri awal Susanti
print("\nData diri awal Susanti")
for key,value in data_awal.items():
    print(f"{key} : {value}")
# # Mengubah data diri Susanti saat 2018 karena pindah alamat dan prodi
data_2018 = {'Alamat' : input("\nalamat baru :"),'Prodi' : input("pindah prodi ke :")}
data_awal.update(data_2018)
# # Menampilkan data diri pada tahun 2018
print("\nData Susanti Tahun 2018")
for key,value in data_awal.items():
    print(f"{key} : {value}")
# # Susanti memutuskan berhenti pada 2019
data_awal.clear()
# # Menampilkan bahwa Susanti telah berhenti kuliah
print("\nPada Tahun 2019")
print("Keputusan Susanti pindah prodi ternyata salah dan dia memutuskan berhenti kuliah pada 2019")