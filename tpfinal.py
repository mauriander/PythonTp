import datetime
import time

## "{;10}" establece un ancho de campo mínimo de 10 RECURSO ADICIONAL PARA MOSTRAR DE FORMA ORDENADA
# https://docs.python.org/es/3.11/library/string.html#format-specification-mini-language


def cargarOpciones():
        print('\n')
        print('1 - Agregar producto')
        print('2 - Venta')
        print('3 - Consultar stock')
        print('4 - Lista de producto')
        print('5 - Pedido a proveerdores (Stock menor o igual a 3)')
        print('6 - Cierre de caja')
        print('0 - Salir')
        print('https://docs.python.org/es/3.11/library/string.html#format-specification-mini-language')
        print('\n')
###------------VALIDACIONES-------------###
def validarOpciones(opcion):
    while (opcion< 0 or opcion>6 ):
        print("ERROR: opción inválida")
        opcion=int(input("Seleccione la opción entre 0 - 6: "))
    return opcion

def existeID(id,productos):
    for p in productos: 
        if p[0] == id:
           return True
    return False

def pasarMayuscula(s):
    return s.upper()

def validarNuevoProducto(idn,productos):
    while idn<=0:    
        print("El ID no puede ser menor a 0.")
        idn = int(input('Ingrese nuevamente un nuevo ID: '))
    while existeID(idn, productos):
        print("El ID ya existe en la lista de productos.")
        idn = int(input('Ingrese nuevamente un nuevo ID: '))
    return idn  

def validarStock(cant):
    while (cant< 1):
        print("ERROR: La cantidad mayor a 0")
        cant=(input("Ingrese un entero donde la cantidad sea mayor a 0: "))
    return int(cant)

def validarPrecio(p):
    while (p<= 0):
        print("ERROR: El precio no puede ser menor a 0")
        p=float(input("Ingrese un precio superior a 0: "))
    return p

def validarID(id, productos):
    while not existeID(id, productos):
        print("El ID no es correcto o no existe en la lista de productos.")
        id = int(input('Ingrese nuevamente un ID: '))
    return id  
    
def validarMetodoPago(metodo):
    while (metodo< 1 or metodo>2 ):
        print("ERROR: Ingrese una opcion correcta")
        metodo=esNumero(input("Seleccione pago: (1)CONTADO --------(2) OTRO METODO : "))
    return int(metodo)

def validarContinuar(cont):
    while (cont< 1 or cont>2 ):
        print("ERROR: Ingrese una opcion correcta")
        cont = esNumero(input('Ingrese: (1)PARA AGREGAR OTRA VENTA --------(2) FINALIZAR '))
    return int(cont)

def validarCantidad(cant,maximo):
    while (cant< 1 or cant>maximo):
        print("ERROR: Opción inválida - Seleccione la cantidad mayor a 0 y menor a ", maximo,":")
        cant=int(input("Ingrese un entero donde la cantidad sea mayor a 0 y menor al maximo: "))
    return cant

def bajoStock(productos):
    bajo=0
    for p in productos:
        if(p[3]<4):
            bajo=1
    return bajo

def esNumero(valor):
    while not valor.isdigit(): 
        valor=(input("Ingrese un valor entero positivo, recuerde no se permiten letras: "))
    return int(valor)

#def esNumerof(valor):
 #   while not valor.isdigit(): 
  #      valor=(input("Ingrese un valor entero positivo, recuerde no se permiten letras: "))
   # return float(valor)     

## ----------- CARGAR STOCK
def cargarStock(productos):
    for p in productos:        
        stockn = esNumero(input(f'El nuevo stock {p[1]} de: '))
        stockn=validarStock(stockn)
        p[3]=stockn

### ---------- SECCION MENU-----------------###
### --------- AGREGAR NUEVO
def agregarProducto(productos):
    print('Escogió opción 1 - AGREGAR PRODUCTO')
    idn = esNumero(input('Ingrese número ID: '))
    idn=validarNuevoProducto(idn,productos)
    nomn = input('Ingrese el nombre/Descripción del producto: ')
    pren = float(input('Ingrese el precio: '))
    pren=validarPrecio(pren)
    stockn = esNumero(input('Ingrese el stock del producto: '))
    stockn=validarStock(stockn)
    productos.append([idn, nomn.upper(), pren, stockn])
    print(f"Producto agregado: {productos[-1]}")  

### --------- VENTA
def ventaProducto(productos,ventas):
    print('Escogio opcion 2 - VENTA')
    continuar=True
    while(continuar):
        idv = esNumero(input('Ingrese número ID: '))
        idv=validarID(idv,productos)
        for p in productos: 
            if p[0] == idv:
                producto=p
        print('Desea vender ',producto[1], ' id=',producto[0], 'solo contamos con ',producto[3],' en stock ')
        cant = esNumero(input('Ingrese la cantidad: '))
        while(cant>producto[3]):
            print('Solo tenemos ',producto[3],' productos en stock')
            cant = esNumero(input('Ingrese una cantidad: '))
        cant=validarCantidad(cant,producto[3])
        metp = esNumero(input('Ingrese el metodo de pago: (1)CONTADO --------(2) OTRO METODO '))
        metp=validarMetodoPago(metp)
        if metp==1:
            precio=producto[2]
            total=precio*cant
            ventas.append([metp,producto[0],producto[1],precio,cant,total])
        elif metp==2:
            precio=producto[2]*1.21
            total=precio*cant
            ventas.append([metp,producto[0],producto[1],precio,cant,total])

        nuevostock=producto[3]-cant
        producto[3]=nuevostock

        cont = esNumero(input('Ingrese: (1)PARA AGREGAR OTRA VENTA --------(2) FINALIZAR '))
        cont=validarContinuar(cont)
        if(cont==2):
            continuar=False

    

### --------- CONSULTA PRODUCTO
def consultaProducto(productos):
    print('Escogio opcion 3 - CONSULTAR PRODUCTO')
    idc = esNumero(input('Ingrese número ID del producto que quiere consultar: '))
    idc = validarID(idc, productos)  # Verificar y validar el ID ingresado
    producto=None
    for p in productos: 
        if p[0] == idc:
            producto=p
            break
    if producto:            
        print('\n---------------------------------------------')            
        print(f"{'ID':<5}{'NOMBRE':<15}{'PRECIO':<10}{'STOCK':<10}")
        #print(producto[0],' ',producto[1],' $',producto[2], ' ',producto[3])
        print(f"{producto[0]:<5}{producto[1]:<15}{producto[2]:<10.2f}{producto[3]:<10}")
        print('----------------------------------------------\n')
    else:
        print('\nEl prorducto no se encuentra\n')

### --------- LISTAR TODOS
def listarProductos(productos):
    print('Escogio opcion 4 - VER LISTADO DE PRODUCTOS')
    print('\n---------------------------------------------')
    print(f"{'ID':<5}{'NOMBRE':<15}{'PRECIO':<10}{'STOCK':<10}")
    for p in productos:
        #print(p[0],' ',p[1],' $',p[2], ' ',p[3])
        print(f"{p[0]:<5}{p[1]:<15}{p[2]:<10.2f}{p[3]:<10}")
    print('----------------------------------------------\n')
      

### --------- MOSTRAR LOS PEDIDOS A LOS PROVEEDORES
def listarPedidoProveedores(productos):
    print('Escogio opcion 5 - LISTADO A PROVEEDROES')
    if bajoStock(productos)==0:
        print('\nNo hay productos que necesitan su reposicion a la brevedad\n') 
    else:
        print('Los siguientes productos necesitan su reposicion a la brevedad')
        print('\n---------------------------------------------')
        print(f"{'ID':<5}{'NOMBRE':<15}{'STOCK':<10}")
        for p in productos:
            if(p[3]<4):
                print(f"{p[0]:<5}{p[1]:<15}{p[3]:<10}")
        print('------------------------------------------------\n')

### --------- CIERRE DE CAJA
def cierreCaja(ventas):
    print('Escogio opcion 6 - CIERRE DE CAJA')
    suma=0
    sumacontado=0
    sumaotrometodo=0  
    if len(ventas) == 0:
        print('\nNo hay ventas realizadas\n') 
    else:
        print('\n------------------------------------------------')
        print(f"{'METODO DE PAGO':<15}{'ID':<5}{'NOMBRE':<15}{'PRECIO':<10}{'CANTIDAD':<10}{'TOTAL':<10}")
        for v in ventas:
            if v[0] == 1:
                metodo = "CONTADO"
                sumacontado+=v[5]
            else:
                metodo = "OTRO METODO"
                sumaotrometodo+=v[5]
            suma+=v[5]
            print(f"{metodo:<15}{v[1]:<5}{v[2]:<15}{v[3]:<10.2f}{v[4]:<10}{v[5]:<10.2f}")
        print('------------------------------------------------\n')
        print(f"{'VENTAS DE CONTADO: $'} {sumacontado:.2f}' | VENTAS CON OTRO METODO DE PAGO: $', {sumaotrometodo:.2f},'\n")
        print(f"Cierre de caja: $', {suma:.2f},'\n") 


def main():
    # p { ID | NOMBRE | PRECIO | STOCK }
    productos=[
    [1,'AZUCAR', 1.45, 6],
    [2,'YERBA', 3.45, 3],
    [3,'HARINA', 2.5, 6],
    [4,'MANTECA', 3.05, 2],
    [5,'GALLETITAS', 10.45, 7],
    [6,'HAMBURGUESAS', 2.15, 1]]

    #VENTAS { METODO DE PAGO | ID | NOMBRE | CANTIDADVENDIDA | PRECIO | TOTAL }
    ventas=[]
    print("Bienvenido al sistema.")
    cargarStock(productos)
    while True:
        cargarOpciones()
        opcion =esNumero(input('Ingrese el numero de la opreacion a realizar: '))
        opcion=validarOpciones(opcion)
        if opcion == 0:
            print("\nGracias por usar el sistema. ¡Hasta luego!\n")
            break
        elif opcion==1:
            agregarProducto(productos)
        elif opcion==2:
            ventaProducto(productos,ventas)
        elif opcion==3:
            consultaProducto(productos) 
        elif opcion==4:
            listarProductos(productos)
        elif opcion==5:
            listarPedidoProveedores(productos)
        elif opcion==6:
            cierreCaja(ventas)
     #   elif opcion==7:
     #        print('Escogio opcion 7 ELIMINAR')
     #        ide = int(input('Ingrese número ID del producto que quiere consultar: '))
     #        for p in productos: 
     #            if p[0] == ide:
     #                producto=p 
     #        productos.remove(p)    
     #        print('---------------------------------------------\n')

main()


