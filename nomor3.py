num=int(input('Masukkan parameter: '))
print('   ---panjang---   ')
if num%2==1:
    for kol in range(0,num):
        for row in range(0,num):
            if(kol == round((num-1)/2)):
                print(' * ', end='')
            elif(row == 0 or row == num-1):
                print(' * ', end='')
            else:
                print(' = ', end='')
        print()
else:
    print('Masukkan angka ganjil')