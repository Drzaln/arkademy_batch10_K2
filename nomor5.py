from hashlib import sha256
from time import time

def isi(s):
    return sha256(s.encode('ascii')).hexdigest()

def cetak(angka):
    acak=[isi(str(time()))[:32]]
    for i in range(0,angka):
        acak.append(isi(acak[i])[:32])
        print(acak[i])
    for i in range(0,angka):
        for j in range(0,i):
            if acak[i]==acak[j]:
                raise Exception('anomali')

angka = int(input('Masukkan angka: '))
print(cetak(angka))