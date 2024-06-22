bilangan = int(input("Masukkan bilangan :"))

for i in range(bilangan):
    f = i + 1
    if bilangan % f == 0:
        print(f)
