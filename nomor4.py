daftar = ['a','b','c']
daftar1 = ['c','d']
daftar2 = ['d','g','h','e']

a = len(daftar)
b = len(daftar1)
c = len(daftar2)

urut = [daftar, daftar1, daftar2]

print('list', urut)

for str_len in urut:
    print(str_len, '=',len(str_len))
    