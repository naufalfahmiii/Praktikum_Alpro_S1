b = int(input("Masukkan bilangan faktorial :"))
def faktorial(b):
    if b == 0:
        return 1
    elif b >= 1:
        return b*faktorial(b-1)
    else:
        print("Masukkan bilangan positif!")
print(b,"!=",faktorial(b))