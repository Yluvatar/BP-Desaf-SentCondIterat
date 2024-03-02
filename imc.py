import sys

try:

    peso = float(sys.argv[1])
    altura = float(sys.argv[2])

    imc = round(peso / (altura**2), 2)

    if imc < 18.5:
        oms = 'Bajo Peso'
    elif 18.5 <= imc < 25.0:
        oms = 'Peso Adecuado'
    elif 25.0 <= imc < 30.0:
        oms = 'Sobrepeso'
    elif 30.0 <= imc < 35.0:
        oms = 'Obesidad Grado I'
    elif 35.0 <= imc < 40.0:
        oms = 'Obesidad Grado II'
    else:
        oms = 'Obesidad Grado III'

    print("\n")
    print(f'SU IMC es {imc} ')
    print(f'La clasificación OMS es {oms}')

except IndexError:

    print('\nFaltan parámetros de entrada (Peso Altura)')

except ZeroDivisionError:

    print('\nNo se puede realizar el cálculo, se ha producido una división en 0')

except ValueError:

    print('\nLos Parámetros deben ser numéricos')

finally:

    print('\nFinalizando')

print("\n")
