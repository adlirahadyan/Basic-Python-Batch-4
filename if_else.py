a = 200
b = 33

if b>a :
    print('{} is greater than {}'.format(a,b))
elif b==a :
    print('{} is equal {}'.format(a,b))
else :
    print('{} is less than {}'.format(a,b))

num = int(input('Angka: '))
b = 33

if num % 2 == 0 :
    print('Angka {} adalah bilangan Genap'.format(num))
else :
    print('Angka {} adalah bilangan Ganjil'.format(num))