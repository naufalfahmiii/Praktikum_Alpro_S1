# list kosong untuk diisi 
daftar_menu = []
i = 0
# perulangan while untuk memasukkan makanan dan harga
while True:
    makanan = str(input(f"masukkan makanan ke {i+1}:"))
    harga = int(input("masukkan harga makanan :"))
    # menambahkan input makanan dan harga ke daftar menu dalam bentuk tuple
    daftar_menu.append((makanan,harga))
    i +=1
    # variabel input dan pengkondisian untuk mengatur perulangan
    isi_lagi = str(input("mau isi menu lagi ? (y/n):"))
    if isi_lagi != "y":
        break
# mencetak data yang sudah dimasukkan
print("Daftar Menu :")
for item in daftar_menu:
    makanan,harga = item
    print(f"{makanan}: Rp {harga}")