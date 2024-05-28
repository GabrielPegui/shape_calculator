from clases import clases_figuras
import sys

# Importación de las figuras
Cuadrado = clases_figuras.cuadrado(0, 'cuadrado')
Circulo = clases_figuras.circulo(0, 'circulo')
Rectangulo = clases_figuras.rectangulo(0, 0, 'rectangulo')

# Arreglo donde se almacenan las figuras
Figuras = [Cuadrado, Circulo, Rectangulo]

def validar_entrada_numero(mensaje):
    entrada = input(mensaje)
    while not entrada.isdigit():
        print('Debe poner la medida sin cms o m. solo el número.')
        entrada = input(mensaje)
    return int(entrada)

def seleccionar_figura():
    print('Bienvenido a su Calculadora de Figuras Geométricas')
    print()
    print('A continuación le mostraremos las figuras disponibles para calcular área y perímetro:')
    for idx, figura in enumerate(Figuras, start=1):
        print(f'Figura número {idx}: {figura}')
    print()
    print('Presione 4 si quiere salir del Calculador de Figuras.')
    print()

def main():
    seleccionar_figura()
    while True:
        seleccion = input('Nombre cuál figura desea calcular: ')
        if seleccion.isdigit() and int(seleccion) == 4:
            sys.exit('Ha seleccionado la opción de salir, el programa se cerrará.')

        figuras_disponibles = {figura.tipofigura: figura for figura in Figuras}
        if seleccion not in figuras_disponibles:
            print('Escriba una figura disponible por favor.')
            continue

        figura = figuras_disponibles[seleccion]
        if isinstance(figura, clases_figuras.cuadrado):
            lados = validar_entrada_numero('La medida de los lados de su cuadrado es: ')
            figura.lados = lados

        elif isinstance(figura, clases_figuras.circulo):
            radio = validar_entrada_numero('La medida del radio de su círculo es: ')
            figura.radio = radio

        elif isinstance(figura, clases_figuras.rectangulo):
            longitud = validar_entrada_numero('La medida de la longitud de su rectángulo es: ')
            ancho = validar_entrada_numero('La medida del ancho de su rectángulo es: ')
            figura.longitud = longitud
            figura.ancho = ancho

        perimetro = figura.perimetro()
        area = figura.area()
        print(f'El perímetro de su {figura.tipofigura} es de {perimetro}.')
        print(f'El área de su {figura.tipofigura} es de {area}.')
        print()

if __name__ == "__main__":
    main()
    


        

        
    
    

    







