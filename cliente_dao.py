from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'ocurrio un error al insertar cliente : {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'ocurrio un error al actualizar cliente {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'ocurrio un error al eliminar el cliente {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    pass
    #Eliminar
    #cliente_eliminar = Cliente(id=3)
    #clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    #print(f'Clientes eliminados: {clientes_eliminados}')

    #Actualiza
    #cliente_actualizar = Cliente(3, 'Ebert', 'Fabina Giovanella', 100)
    #cliente_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    #print(f'Clientes Actualizados : {cliente_actualizados}')

    #Insertar
    #cliente1 = Cliente(nombre='Elias', apellido='Giovanella', membresia=600)
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(f'Clientes insertados _ {clientes_insertados}')

    #Seleccionar Clientes
    #clientes = ClienteDAO.seleccionar()
    #for cliente in clientes:
    #    print(cliente)