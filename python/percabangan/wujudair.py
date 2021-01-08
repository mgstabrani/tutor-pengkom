#PROGRAM

#KAMUS
#T : float

#ALGORITME
T = float(input("Masukkan suhu: "))

if(T <= 0):
    print("beku")
elif(T > 0 and T < 100):
    print("cair")
else:
    print("uap")