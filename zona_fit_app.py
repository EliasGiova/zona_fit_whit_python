from cliente import Cliente
from cliente_dao import ClienteDAO

print('*** Clientes de Zona Fit ***')
opcion = None
while opcion != 5:
    print('''Menu:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir''')
    opcion =int(input(f'Escribe tu opcion (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
        print('\n')
    elif opcion == 2:
        nombre_var = input(f'Escribe el nombre: ')
        apellido_var = input(f'Escribe el apellido: ')
        membresia_var = input(f'Escribe el numero de la membresia: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        cliente_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes Insertados: {cliente_insertados}\n')
    elif opcion == 3:
        id_cliente_var = int(input(f'Escribe el id del cliente a modificar: '))
        nombre_var = input(f'Escribe el nombre: ')
        apellido_var = input(f'Escribe el apellido: ')
        membresia_var = input(f'Escribe el numero de la membresia: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes Actualizados: {clientes_actualizados}\n')
    elif opcion == 4:
        id_cliente_var = int(input(f'Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        cliente_eliminado = ClienteDAO.eliminar(cliente)
        print(f'Clientes Eliminados: {cliente_eliminado}\n')
else:
    print(f'Saliendo de la aplicacion')
