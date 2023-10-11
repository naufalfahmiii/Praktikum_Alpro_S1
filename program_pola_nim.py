# Input ukuran
size = int(input("Masukkan size : "))

#Angka 0
# Bagian atas pola
print("o" * size)
# Bagian tengah pola
for i in range(size):
    print("o" + " " * (size - 2) + "o") 
# Bagian bawah pola
print("o" * size)
print()

#Angka 4
# Bagian atas pola
for i in range(size - 1):
    print("o" + " " * (size - 2) + "o")
# Bagian tengah pola
print("o"*size)
# Bagian bawah pola
for i in range(size-1):
    print(" "*(size - 1)+ "o")
print()

# Angka 2
# Bagian atas pola
print("o" * size)
# Bagian tengah pola
for i in range(size - 2):
    print(" " * (size - 1) + "o") 

print("o" * size)

for i in range(size - 2):
    print("o") 
# Bagian bawah pola    
print("o" * size)
print()