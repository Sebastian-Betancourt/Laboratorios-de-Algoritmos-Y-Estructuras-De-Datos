Nombre = input ("Ingrese su nombre: ")
cedula = int(input("Digite su numero de cedula: "))
Salario = float(input("Ingrese cual es su salario actual actual: "))

print ( "¿Que tipo de contrato tiene actualmente?: ")
print ("Inicial (A)")
print ("Medio (B)")
print ("Intermedio (C)")
print ("Avanzado (D)")

decision = input("Elija una opción: ")

if decision == 'A':
    incremento = (Salario * 0.03)
    nuevo_salario = Salario + incremento
    print(f"Estimado {Nombre}, con número de cédula {cedula}, su salario nuevo es: {nuevo_salario}.")
    print("El porcentaje de incremento es del 3%")
elif decision == 'B':
    incremento = (Salario * 0.10)
    nuevo_salario = (Salario + incremento)
    print(f"Estimado {Nombre}, con número de cédula {cedula}, su salario nuevo es: {nuevo_salario}.")
    print("El porcentaje de incremento es del 10%")
elif decision == 'C':
    incremento = (Salario * 0.25)
    nuevo_salario = Salario + incremento
    print(f"Estimado {Nombre}, con número de cédula {cedula}, su salario nuevo es: {nuevo_salario}.")
    print("El porcentaje de incremento es del 25%")
elif decision == 'D':
    incremento = (Salario * 0.45)
    nuevo_salario = Salario + incremento
    print(f"Estimado {Nombre}, con número de cédula {cedula}, su salario nuevo es: {nuevo_salario}.")
    print("El porcentaje de incremento es del 45%")
else:
    print("Esta opcion no es valida")