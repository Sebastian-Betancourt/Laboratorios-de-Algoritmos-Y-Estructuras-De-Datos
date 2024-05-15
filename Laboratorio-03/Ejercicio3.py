import sys
#-----------Resgristro----------------
print("-----Bienvenido a AED4-------")
nomb=input("Ingrese su Nombre:")
apell=input("Ingrese su apellido:")

#Fecha de nacimiento 
print("Ingrese su fecha de nacimiento:")
dia=int(input("Dia: "))
if dia>31:
    print("error")
    sys.exit()

mes=int(input("Mes: "))
if mes>12:
     print("error")
     sys.exit()
año=int(input("Año: "))

#Genero 
genero=input("Genero F, M, OTROS:")

#Correo 
user=input("Ingrese su Usuario o numero de telefono:")
if len(cuser)==10:
    print("Su Perfil se ha registrado correctamente")
while len(user)>=10:
    print("Usuario no Valido")
    user=input("Ingrese nuevamente su Usuario o numero de telefono:")

#Contrseña y Validacion
contraseña=input("Ingrese una contraseña:")
conficontraseña=input("Confirme la contraseña:")
while contraseña!=conficontraseña:
    print("Contraseña Incorrecta")
    conficontraseña=input("Ingrese Nuevamente la contraseña:")

print("Has completado tu registro")

#---------Inicio de Seccion------------

print("---------Iniciar seccion AED4----------")
userin=input("Usuario o Numero de Telefono:")
if userin!=user:
    print("Usuario no registrado")
    sys.exit()
Contr=input("Contraseña")
if Contr!=conficontraseña:
    print("Contraseña Incorrecta")
    sys.exit()
print("Has Iniciado Sección")
