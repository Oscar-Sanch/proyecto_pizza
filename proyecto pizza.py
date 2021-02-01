# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:08:58 2021

@author: pc
"""


def desplegarMenu(texto,max):
    while (True):
        for i in texto:
            print (i) 
        opcion = int(input())            
        if (opcion >0 and opcion <= max):
            return opcion

def insertarOrden(orden,cliente):
    opcion=1
    total=[]
    textoMenu=("\n\n\t  Catálogo de Pizzas","\t**********************""\n\t1)Pepperoni","\t2)Hawuaiana","\t3)Especial","\t4)Mexicana","\t5)Ranchera","\t6)Completar orden","\nOpción: ")
    ing=('Pepperoni','Cerezas','Piña','Jamón','Chorizo','Frijoles','Aguacate','Salchicha','Jalapeños','Tocino','Cebolla')
    listaOrden=[]
    while (opcion !=6):
        opcion= desplegarMenu(textoMenu,len(textoMenu)-2)
        if(opcion==1):
            ingredientes=[]
            print("\n")
            print("")
            clave='001'
            nombre="Pepperoni"
            ingredientes.append(ing[0])
            ingredientes.append(ing[1])
            ingredientes.append(ing[9])
            precio=235.00
            listaOrden.append([clave,nombre,ingredientes,precio])
            total.append(precio)
            listar1(listaOrden)            
        elif(opcion==2):
            ingredientes=[]
            print("\n")
            print("")
            clave='022'
            nombre="Hawaiana"
            ingredientes.append(ing[1])
            ingredientes.append(ing[2])
            ingredientes.append(ing[3])
            precio=265.90
            listaOrden.append([clave,nombre,ingredientes,precio])
            total.append(precio)
            listar1(listaOrden)
        elif(opcion==3):
            ingredientes=[]
            print("\n")
            print("")
            clave='054'
            nombre="Especial"
            ingredientes.append(ing[2])
            ingredientes.append(ing[7])
            ingredientes.append(ing[8])
            precio=215.50
            listaOrden.append([clave,nombre,ingredientes,precio])
            total.append(precio)
            listar1(listaOrden)
        elif(opcion==4):
            ingredientes=[]
            print("\n")
            print("")
            clave='105'
            nombre="Mexicana"
            ingredientes.append(ing[4])
            ingredientes.append(ing[5])
            ingredientes.append(ing[10])
            precio=250.00
            listaOrden.append([clave,nombre,ingredientes,precio])
            total.append(precio)
            listar1(listaOrden)
        elif(opcion==5):
            ingredientes=[]
            print("\n")
            print("")
            clave='113'
            nombre="Ranchera"
            ingredientes.append(ing[5])
            ingredientes.append(ing[6])
            ingredientes.append(ing[9])
            precio=239.610
            listaOrden.append([clave,nombre,ingredientes,precio])
            total.append(precio)
            listar1(listaOrden) 
    nom=input("Nombre del Cliente: ")    
    numero=1
    print(f"Número de orden: {numero}")
    cantidad=len(listaOrden)
    print(f"Número de items: {cantidad}")
    print("Su orden es: ")
    listar1(listaOrden) 
    cliente.append([numero,nom,cantidad,sum(total)])
    sum(total)
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSu total es: ${sum(total)}")
    orden.append(listaOrden)
    print("Orden registrada\n")
    
def listar1(listaOrden):
    print("")
    print("\tClave\t\t\t  Pizza\t\t\t\t\tIngredientes\t\t\t\t\t\t   Precio")
    print("\t******\t\t\t**********\t\t\t***********************\t\t\t\t\t***************")
    for contacto in listaOrden:
        for dato in contacto:
            print("\t",dato,end="\t\t  ")
        print()

def listar2(cliente):
    print("")
    print("\t Orden #\t Cliente\t\t items\t\t Total")
    print("\t********\t*********\t\t*******\t\t*******")
    for contacto in cliente:
        for dato in contacto:
            print("\t",dato,end="\t\t")
        print()
        
def buscarCliente(cliente):
    nombre=input("\t  Nombre: ")
    pos=[unCliente[1] for unCliente in cliente].index(nombre)
    print(f"Orden de {nombre} servida!\n")
    return pos
    
        
def borrar(cliente):
    pos=buscarCliente(cliente)
    del(cliente[pos])

def main():
    textoMenu=("\n\t\t   PIZZA DOMINO","\t=======================","\t\t 1)Ordenar","\t\t 2)Servir Orden","\t\t 3)Salir","Seleccione una opción:")      
    cliente=[]
    orden = []
    opcion =1
    while (opcion !=3):
        opcion= desplegarMenu(textoMenu,len(textoMenu)-2)
        if(opcion==1):
            insertarOrden(orden,cliente)
            print("\n")
            print("\t\tOrdenes en espera:\n")
            listar2(cliente)
            print("\n")
        elif(opcion==2):
            print("\n")
            borrar(cliente)
            print("\n\t\tOrdenes en espera:\n")
            listar2(cliente)
            print("")   
                           
main()