while True :
    waktupinjam = int(input("Lama meminjam buku : "))
    DendaPerHari = 2000
    DendaPerMinggu = 5000
    TotalDenda = 0

    for i in range (1,waktupinjam+1) :
        if i > 7 :
            TotalDenda += DendaPerHari
            if i % 7 == 0 :
                TotalDenda += DendaPerMinggu
    if waktupinjam > 7 :
        print("Anda meminjam buku melebihi 1 minggu dan terlambat mengembalikan selama",((waktupinjam)-7),"Hari")
        print("jadi anda dikenai denda sebesar Rp",TotalDenda)  
    else :
        print("Anda meminjam buku selama",waktupinjam,"Hari")
        print("jadi tidak dikenai denda, Terima Kasih....")

    pilih = input("Apakah ingin melakukan perhitungan lagi ? :")
    while pilih.lower() not in ("yes", "no"):
        print("masukkan yes / no")
        pilih = input("Apakah ingin melakukan perhitungan lagi ? :")
    if pilih.lower() == "yes":
        print("Perhitungan dimulai lagi")
    else :
        print("Perhitungan dihentikan")
        break