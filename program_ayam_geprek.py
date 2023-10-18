total_harga = 0

while True: 
    print("\nAyam Geprek Kamal siap melayani")
    print("Menu:\n 1. Biasa - Rp. 5.000\n 2. Double - Rp. 7.000\n 3. Special - Rp. 9.000 ")

    pilih_menu = input("Menu (1/2/3) :")

    if pilih_menu in ("1","2","3"):
        if pilih_menu == "1":
            total_harga += 5000
        elif pilih_menu == "2":
            total_harga += 7000
        elif pilih_menu == "3":
            total_harga += 9000

        tambah_nasi = input("Jika tambah nasi masukkan yes/no :").lower()
        if tambah_nasi == "yes":
            total_harga += 3000
        else:
            total_harga += 0

        if total_harga > 30000:
            total_harga *= 0.97
        elif total_harga > 70000:
            total_harga *= 0.93

        kode_promo = input("Masukkan kode promo (opsional) :")
        if kode_promo == "GEPREK17":
            total_harga *= 0.97

        print("Total harga pembelian : Rp.",(total_harga))

        pesan_lagi = input("\nApa ingin memesan lagi ? (yes/no) :").lower()
        if pesan_lagi != "yes":
            break
    else:
        print("\nMenu hanya ada (1/2/3)")