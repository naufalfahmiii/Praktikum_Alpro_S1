# # Daftar anggota ukm
print("Daftar UKM beserta anggotanya :")
ukm_pencinta_alam = {'Budi','Ani','Joko','Siti','Rina','Agus'}
ukm_bulutangkis = {'Joko','Siti','Eka','Rini','Deni'}
ukm_teater = {'Ani','Dedi'}
ukm_taritradisional = {'Siti','Fika','Gusman'}
# Menampilkan UKM beserta anggotanya

ukm = {
    "UKM Pencinta Alam": ukm_pencinta_alam,
    "UKM Bulutangkis": ukm_bulutangkis,
    "UKM Teater": ukm_teater,
    "UKM Tari Tradisional": ukm_taritradisional
}
for key,value in ukm.items():
    print(f"{key} : {value}")
# # Mahasiswa gabung lebih dari 1 ukm
anggota_ukmlebih = (
    ukm_pencinta_alam & ukm_bulutangkis |
    ukm_pencinta_alam & ukm_teater |
    ukm_teater & ukm_taritradisional
)
print("\nMahasiswa yang ikut lebih dari 1 UKM :")
for anggota in anggota_ukmlebih:
    print(anggota)
print("Ada", len(anggota_ukmlebih), "mahasiswa yang ikut lebih dari 1 UKM")
# # Menambahkan Hadi ke ukm pencinta alam dan ukm bulutangkis
print("\nData UKM setelah Hadi masuk :")
ukm_pencinta_alam.add('Hadi'),ukm_bulutangkis.add('Hadi')
for key,value in ukm.items():
    print(f"{key} : {value}")
# # Menghapus Rini dari ukm bulutangkis
tidak_ukm =[]
print("\nUpdate data ukm setelah Rini keluar :")
ukm_bulutangkis.remove('Rini')
tidak_ukm.append('Rini')
print("UKM Bulutangkis :",ukm_bulutangkis)
# # UKM yang memiliki anggota kurang dari 4 
print("\nDaftar UKM yang anggotanya kurang dari 4 :")
fix_kurang_4 = []
for i,j in ukm.items() :
    if len(j) < 4 :
        fix_kurang_4.append(i)
    else :
        continue
print(fix_kurang_4)
# # Menampilkan mahasiswa yang tidak mengikuti UKM
seluruh_ukm = (ukm_pencinta_alam,ukm_bulutangkis,ukm_teater,ukm_taritradisional)
print("\nMahasiswa yang tidak mengikuti UKM :")
tidak_ikutUKM = set()
for i in seluruh_ukm:
    for j in tidak_ukm:
        if j in i :
            continue
        else:
            tidak_ikutUKM.add(j)
print(tidak_ikutUKM)
