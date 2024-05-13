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
correo=input("Ingrese su Usuario o numero de telefono:")
if len(correo)<=10:
    print("Su Perfil se ha registrado correctamente")
while len(correo)>=10:
    print("Usuario no Valido")
    correo=input("Ingrese nuevamente su Usuario o numero de telefono:")

#Contrseña y Validacion
contraseña=input("Ingrese una contraseña:")
ncontraseña=input("Ingrese Nuevamente la contraseña:")
while contraseña!=ncontraseña:
    print("Contraseña Incorrecta")
    ncontraseña=input("Ingrese Nuevamente la contraseña:")

print("Has completado tu registro")

#---------Inicio de Seccion------------

print("---------Iniciar seccion AED4----------")
correis=input("Usuario o Numero de Telefono:")
if correis!=correo:
    print("Usuario no registrado")
    sys.exit()
Contr=input("Contraseña")
if Contr!=ncontraseña:
    print("Contraseña Incorrecta")
    sys.exit()
print("Has Iniciado Sección")