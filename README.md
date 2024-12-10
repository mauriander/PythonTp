# PythonTp
# Trabajo Integrador Python

Bienvenido al repositorio del **Trabajo Integrador Python**. Este proyecto es un sistema de gestión de productos que permite agregar, vender, consultar stock, listar productos, generar pedidos a proveedores y realizar el cierre de caja.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Uso](#uso)
- [Funciones](#funciones)
- [Diccionario de Datos](#diccionario-de-datos)
- [Contribuciones](#contribuciones)

## Instalación
Para ejecutar este proyecto, necesitas tener Python 3.x instalado en tu sistema. Sigue estos pasos para instalar y ejecutar el proyecto:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mauriander/PythonTp.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd PythonTp
   ```
3. Ejecuta el script principal:
   ```bash
   python tpfinal.py
   ```

## Uso
Al ejecutar el script, se mostrará un menú con las siguientes opciones:
1. Agregar producto
2. Venta
3. Consultar stock
4. Lista de producto
5. Pedido a proveedores (Stock menor o igual a 3)
6. Cierre de caja

0. Salir

Selecciona la opción deseada ingresando el número correspondiente.

## Funciones
### Agregar Producto
Permite agregar un nuevo producto a la lista. Se debe ingresar el ID, nombre, precio y stock del producto.

### Venta de Producto
Registra una venta de producto. Se debe ingresar el ID del producto, la cantidad a vender y el método de pago.

### Consultar Stock
Consulta la información de un producto específico ingresando su ID.

### Listar Productos
Muestra una lista de todos los productos disponibles con su ID, nombre, precio y stock.

### Pedido a Proveedores
Genera una lista de productos que tienen un stock menor o igual a 3, indicando que necesitan reposición.

### Cierre de Caja
Muestra un resumen de todas las ventas realizadas, incluyendo el método de pago, el total de ventas en efectivo y con otros métodos, y el cierre de caja total.

## Diccionario de Datos
| **Nombre del Campo**    | **Descripción**                                                                 | **Tipo de Dato** | **Valores Permitidos** | **Ejemplo**            |
|-------------------------|---------------------------------------------------------------------------------|------------------|------------------------|------------------------|
| `cant`                  | Cantidad disponible del producto                                                | Entero           | Números enteros >= 0   | 6                      |
| `cant`                  | Cantidad de producto vendida                                                    | Entero           | Números enteros > 0    | 2                      |
| `cont`                  | Opción de continuar en el proceso de venta                                       | Entero           | 1 (Agregar otra venta), 2 (Finalizar) | 1                      |
| `id`                    | Identificador único del producto                                                | Entero           | Números enteros > 0    | 1                      |
| `idc`                   | Identificador del producto para consulta                                        | Entero           | Números enteros > 0    | 1                      |
| `idn`                   | Identificador del nuevo producto                                                | Entero           | Números enteros > 0    | 1                      |
| `idv`                   | Identificador del producto para venta                                           | Entero           | Números enteros > 0    | 1                      |
| `maximo`                | Cantidad máxima permitida para la venta                                         | Entero           | Números enteros > 0    | 10                     |
| `metodo`                | Método de pago utilizado en la venta                                             | Entero           | 1 (Contado), 2 (Otro)  | 1                      |
| `metp`                  | Método de pago utilizado en la venta                                             | Entero           | 1 (Contado), 2 (Otro)  | 1                      |
| `nomn`                  | Nombre o descripción del producto                                               | Cadena de texto  | Texto                  | "AZUCAR"               |
| `opcion`                | Opción seleccionada en el menú                                                  | Entero           | Números enteros entre 0 y 6 | 1                      |
| `p`                     | Precio del producto                                                             | Flotante         | Números > 0            | 1.45                   |
| `pren`                  | Precio del nuevo producto                                                       | Flotante         | Números > 0            | 1.45                   |
| `productos`             | Lista de productos                                                              | Lista            | Lista de productos     | [[1, 'AZUCAR', 1.45, 6], ...] |
| `stockn`                | Cantidad de stock del nuevo producto                                            | Entero           | Números enteros >= 0   | 6                      |
| `suma`                  | Total de ventas                                                                 | Flotante         | Números > 0            | 100.00                 |
| `sumacontado`           | Total de ventas realizadas en efectivo                                          | Flotante         | Números > 0            | 50.00                  |
| `sumaotrometodo`        | Total de ventas realizadas con otros métodos de pago                            | Flotante         | Números > 0            | 50.00                  |
| `total`                 | Total de la venta                                                               | Flotante         | Números > 0            | 2.90                   |
| `valor`                 | Valor ingresado por el usuario                                                  | Cadena de texto  | Texto                  | "123"                  |
| `ventas`                | Lista de ventas                                                                 | Lista            | Lista de ventas        | [[1, 1, 'AZUCAR', 1.45, 2, 2.90], ...] |

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
