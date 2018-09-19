
print("======================================")
print("|1. Tambah                           |")
print("|2. Kurang                           |")
print("|3. Kali                             |")
print("|4. Bagi                             |")
print("======================================")
select = int(input("Pilih angka sesuai dengan operasi matematika : "))
x =  int(input("Number 1 : "))
y = int(input("Number 2 : "))


print("Number 1: " + str(x))
print("Number 2: " + str(y))

if select == 1:
    total = x + y
    print("Total " + str(total))
elif select == 2:
    total = x - y
    print("Total " + str(total))
elif select == 3:
    total = x * y
    print("Total " + str(total))
elif select == 4:
    total = x / y
    print("Total " + str(total))
else:
    print("Invalid input")
