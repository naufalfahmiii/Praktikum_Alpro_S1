def main() :
    user = str(input("Masukkan 1/2/3 :"))
    "1 = kerucut"
    "2 = limas segilima"
    "3 = prisma segilima"
    if (user == "1") :
        lp_kerucut()
    elif (user == "2"):
        lp_limas_segilima()
    elif (user == "3"):
        lp_prisma_segilima
    else :
        print("pilihan hanya ada 1/2/3 ")
# luas permukaan kerucut
def lp_kerucut():
    phi = 22/7
    r = float(input("masukkan jari - jari kerucut :"))
    s = float(input("masukkan sisi kerucut :"))
    hasil = phi*r*(r+s)
    print ("luas permukaan kerucut adalah",round(hasil,2))
# luas permukaan limas segilima
def lp_limas_segilima():
    s = float(input("masukkan sisi limas segilima :"))
    t = float(input("masukkan tinggi limas segilima :"))
    luas_alas = 1.72*s*s
    luas_sisi_tegak = 5*(1/2*s*t)
    hasil = (luas_alas + luas_sisi_tegak)
    print("luas permukaan limas segilima adalah",round(hasil,2))
# # luas permukaan prisma segilima
def lp_prisma_segilima():
    s = float(input("masukkan sisi prisma segilima :"))
    t = float(input("masukkan tinggi prisma segilima :"))
    luas_alas = 1.72*s*s
    keliling_alas = 5*s
    hasil =(2*(luas_alas)) + (keliling_alas*t)
    print("luas permukaan prisma segilima adalah",round(hasil,2))
main()