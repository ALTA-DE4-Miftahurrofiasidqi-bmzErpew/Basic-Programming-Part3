bilangan = int(input("Masukkan bilangan :"))

for i in range(bilangan):
    f = bilangan - i
    if bilangan % f == 0:
        print(f)
