# Ejercicio N.2 Convertir grados centígrados a kelvin y fahrenheit 

# input
print("--------------------------------------")
C = int(input("digite los grados celcius que se quiere convertir a kelviny fahrenheit:"))

# prosesing

F = (C * (9/5)) + 32
K = C + 273.15

# output
print("--------------------------------------")
print("grados Fahrenheit" + str(F) )
print("grados kelvin" + str(K))
print("--------------------------------------")