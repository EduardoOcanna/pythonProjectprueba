# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

try:
    # El mensaje de mostrará en pantalla y el valor ingresado se almacena en x
    x = float(input("Número: "))

    # El proceso se ejecuta: 1/X.
    inverse = 1.0 / x

except ValueError:
    # Este error se activa si se ingresa algún caracter no numérico
    print("Debe ir un int o float")

except ZeroDivisionError:
    # Este error se activa en caso se ingrese el valor 0 para x
    print("Infinito")

finally:
    # Este mensaje se imprime al finalizar el programa
    print("Puede que haya habido una excepción o no.")