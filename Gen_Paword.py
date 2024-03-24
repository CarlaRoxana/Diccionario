import random
v = "1234567890¿?&%$#+abcdrteACEUJHLOMWQkomny/!¡="

pregunta = int(input("escribe la longitud de tu contraseña = "))
password = ("")

for i in range(pregunta):
    password += random.choice(v)
print(password)
