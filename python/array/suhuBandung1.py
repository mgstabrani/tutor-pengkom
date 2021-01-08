suhu = [20,20,21,22,19,31,19,20,18,23,27,18,23,16,14,17,21,17,16,21,33,23,24,22,15,14,18,19,20,23]

#Cai suhu terendah
min = suhu[0]
for i in range(1,30):
    if (min > suhu[i]):
        min = suhu[i]
print(min)
