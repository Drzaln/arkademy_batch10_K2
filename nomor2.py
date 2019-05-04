import re

user = input ('Masukkan Username: ')
matchUser = re.match(r"^[a-z]{8}$",user)

anu = input ('Masukkan Password: ')
matchPass = re.match(r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+\-=\[\]{};:\\|,.<>\/?])(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\|,.<>\/?]{8}$',anu)

if matchUser:
    print('Selamat Datang',user)
else:
    print('Error!!! Username harus terdiri dari 8 huruf a-z')
if matchPass:
    print('Berhasil Masuk',anu)
else:
    print('Error!!! Password harus terdiri dari 8 karakter a-z A-Z dan karakter spesial')