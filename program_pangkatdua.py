b = int(input("Masukkan bilangan :"))
p = 2
def padu(b,p):
    if p == 0:
        return 1
    else:
        return b *(padu(b,(p-1)))
print(b,"^",p,"=",padu(b,p))



# p = int(input("Masukkan pangkat :"))
        # return b*(padu(b,(p-1)))