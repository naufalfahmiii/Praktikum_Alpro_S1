awal = int(input("masukkan bilangan awal :"))
akhir = int(input("masukkan bilangan akhir :"))
print("bilangan prima antara",awal,"sampai",akhir , ":")
for a in range(awal,akhir+1):
    if a > 1:
        for b in range(2,a):
            if (a % b) == 0:
                break
        else:
            print(a)