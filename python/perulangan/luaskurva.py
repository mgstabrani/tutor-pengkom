x1 = float(input("Masukkan batas bawah: "))
x2 = float(input("Masukkan batas atas: "))
interval = float(input("Masukkan interval: "))

x = x1
luas = 0
while(x <= x2):
    luas += x*interval
    x += interval
print(luas)