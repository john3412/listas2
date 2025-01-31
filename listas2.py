# Nombre del programa: listas2
# Descripción: Programa que determina el mayor y menor de 5 números ingresados por el usuario, además de determinar si hay valores repetidos.
# Autor: Jonathan López Ayala
# Fecha: 30/01/2025

import os

def main():

    os.system("color f0")
    os.system("cls")

    while True:
        lista = []
        for x in range(5):
            valor = int(input("Ingrese valor:"))
            lista.append(valor)

        mayor = lista[0]
        for x in range(1, 5):
            if lista[x] > mayor:
                mayor = lista[x]

        menor = lista[0]
        for y in range(1, 5):
            if lista[y] < menor:
                menor = lista[y]

        # Corrección en la lógica para encontrar valores repetidos
        repetidos = False
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] == lista[j]:
                    repetidos = True
                    if repetidos:
                        repetidos = lista[i]
                    break
            if repetidos:
                break

        if repetidos:
            igual = repetidos
        else:
            igual = "No hay valores repetidos"

        print("Lista completa")
        print(lista)
        print("Mayor de la lista")
        print(mayor)
        print("Menor de la lista")
        print(menor)
        print("Igual de la lista")
        print(igual)

        resp = input("¿Quieres repetir el proceso? (s/n): ")
        if resp.lower() != 's':
            break

    os.system('pause')

main()
