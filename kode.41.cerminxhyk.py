# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
x = float(input("Tuliskan Nilai X : "))
y = float(input("Tuliskan Nilai Y: "))
hk = float(input("Tuliskan Nilai h / k : "))

# Mengkonversi
x1 = 2 * hk - x
y1 = 2 * hk - y 

# Menampilkan Hasil
print('==========================================================')
print('Maka Hasil Pencerminan A(%d,%d)' %(x,y))
print('Pada Sumbu X = h = %d' %(hk))
print('Maka X* = %d'  %(x1))
print('Maka Y* = %d'  %(y))
print('Pada Sumbu Y = k = %d' %(hk))
print('Maka X* = %d'  %(x))
print('Maka Y* = %d'  %(y1))
print('==========================================================')
