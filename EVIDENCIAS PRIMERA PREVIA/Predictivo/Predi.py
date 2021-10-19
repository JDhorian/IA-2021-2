import os
import csv



Agenda={}
def registrar_objeto(nombre_archivo):
    with open(nombre_archivo, 'a', newline='') as archivo:
        writer=csv.writer(archivo, delimiter=',')
        os.system('cls')

        nombre=input("Nombre: ")
        print('y')
        caract1=input("primera caracteristica: ")
        caract2=input('segunda caracteristica: ')
        caract3=input('tercera caracteristica: ')

        writer.writerow([nombre, caract1, caract2, caract3 ])

def recupera_info(nombre_archivo):
    os.system('cls')
    with open(nombre_archivo, 'r', newline='') as archivo:
        for linea in archivo:
            linea=linea.rstrip()
            lista=linea.split(',')
    return(lista)


def buscarobjeto(SintomasEnfermedad,sintomas):
  for i in SintomasEnfermedad:
    if (len(set(SintomasEnfermedad[i]) & set(sintomas)) > 0):
      Agenda[i] = len(set(SintomasEnfermedad[i]) & set(sintomas))
  objeto =max(Agenda)
  return (objeto)


if __name__ == "__main__":
  caracteristica = []
  ciclo = True
  ciclo2 = "m"
  csintomas = 1
  objeto = 0
  archivo='objetos.csv'


  while (ciclo == True): #un ciclo que hasta que diga que no quiere ingresar mas datos, no se sale
    ciclo2 = ""
    print("Ïngrese la caracteristica ", csintomas,": ")
    caracteristica.append(input())
    csintomas += 1
    while (not (ciclo2 == "Y" or ciclo2 =="N")): #un ciclo que hasta que no diga Y o N no sale
      ciclo2 = input("Quiere ingresar mas caracteristicas? Y o N: ")
      if ciclo2 == "N":
        ciclo = False

    objeto=  buscarobjeto(recupera_info(archivo),caracteristica)
    print(objeto)
