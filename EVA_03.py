import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


titanic_data = pd.read_csv("d:\Ciencia de Datos\EVA_03\Titanic_l.csv")


def limpieza():
    titanic_l = pd.read_csv('d:\Ciencia de Datos\EVA_03\Titanic.csv')
    titanic_l = titanic_l.drop(['Edad','Cabina','Bote de Rescate','Cuerpo', 'Destino'], axis=1)
    titanic_l.to_csv('d:\Ciencia de Datos\EVA_03\Titanic_l.csv')
    print(titanic_l, " \n")


def busqueda():
    ticket=str(input('Ingrese el ticket del o los pasajeros: '))
    t_ticket=titanic_data['Ticket'] == ticket
    busqueda_ticket=titanic_data[t_ticket]
    print(busqueda_ticket, " \n")


def grafica_f():
    estado_sobrevivencia= titanic_data.groupby('Sobrevivió')['Clase'].count()
    print(estado_sobrevivencia)
    y=np.array([ estado_sobrevivencia[0], estado_sobrevivencia[1]])
    
    estados=['Cant. Muertos', 'Cant. Vivos']

    plt.pie(y, labels= estados, autopct="%0.1f %%", shadow= True)
    plt.legend(title = "Sobrevivencia de pasajeros del Titanic")
    plt.show()


def grafica_b():
    eje_x = ['1','2','3']
    eje_y = titanic_data.groupby('Clase')['Sobrevivió'].count()
    print(eje_x)
    print(eje_y)
    
    y=np.array([eje_y[1],eje_y[2], eje_y[3]])
    
    plt.bar(eje_x,y)
    
    plt.ylabel('Cantidad de sobrevivientes')

    plt.xlabel('Clases')

    plt.show()


def costo_t():
  tarifa_ticket = titanic_data['Tarifa']  

  print('Tarifa maxima: ', tarifa_ticket.max())
  print('Tarifa minima: ', tarifa_ticket.min())


menu="""
1 - Limpieza de datos.
2 - Busqueda de usuarios por ticket.
3 - Grafica de personas fallecidad.
4 - Grafica de personas soibrevivientes por clase.
5 - Saber los costos de los tickers.
6 - Salir
Elige una opcion: """
opcion = input(menu)

if opcion == '1':
    limpieza()
elif opcion == '2':
    busqueda()
elif opcion == '3':
    grafica_f()
elif opcion == '4':
    grafica_b()
elif opcion == '5':
   costo_t()
elif opcion == '6':
    exit()
else:
    print('Ingrese una opcion correcta')
