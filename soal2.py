number1 = float(input("Masukkan angka pertama: "))
number2 = float(input("Masukkan angka kedua: "))
number3 = float(input("Masukkan angka ketiga: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3