# Input suhu dalam Celsius 
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi Celsius ke Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Tampilkan hasil konversi
print(f"Suhu dalam Fahrenheit adalah: {fahrenheit} derajat Fahrenheit")

print()
print()

# Input suhu dalam Fahrenheit 
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Konversi Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5/9

# Tampilkan hasil konversi
print(f"Suhu dalam Celsius adalah: {celsius}°C")

print()
print()

# Input suhu dalam Kelvin
kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Konversi Kelvin ke Celsius
celsius = kelvin - 273.15

# Tampilkan hasil konversi
print(f"Suhu dalam Celsius adalah: {celsius}°C")