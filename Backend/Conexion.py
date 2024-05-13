import psycopg2
#import subprocess

#Funcion que conecta a la base de datos
def connect():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            port='5432', 
            password='123',  #Coloca tu contraseña
            database='Jalisco' #cambia el nombre si lo tienes con otro
        )
        return connection
    except psycopg2.Error as ex:
        print("Error al conectar a la base de datos:", ex)
        return None
# Esta funcion da el nombre las tablas
def tablas():
    try:
        Informacion = []
        connection = connect()
        cursor = connection.cursor()

        # Query para seleccionar todas las tablas en la base de datos
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        #print("Tablas en la base de datos:")
        for row in cursor.fetchall():
            Informacion.append(row[0])
    
        # Cerrar la conexión
        cursor.close()
        connection.close()
        return Informacion
    
    except Exception as ex:
        print(f"Error al conectar o consultar la base de datos: {ex}")
        return None
# Esta funcion muestra los registros de la tabla, solo ingresa el nombre de la tabla correctamente
def mostrar_registros(nombre_tabla):
    try: 
        Informacion = []
        connection = connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{nombre_tabla}' AND table_schema = 'public'")
        columnas = [desc[0] for desc in cursor.fetchall()]
        Informacion.append(columnas)

        # Consulta para seleccionar todos los registros de la tabla
        consulta = f"SELECT * FROM {nombre_tabla}"
        cursor.execute(consulta)

        print("\nRegistros de la tabla:", nombre_tabla)
        print(columnas) # Imprime los nombres de las columnas
        for fila in cursor.fetchall():
            Informacion.append(fila)  
            print(fila)  # Imprime los valores de cada registro

        cursor.close()
        connection.close()
        return Informacion
    
    except Exception as ex:
        print(f"Error al conectar o consultar la base de datos: {ex}")
        
# A partir de aqui son un copy paste en add, para este ingresas el nombre del nuevo sector, el id incrementa automaticamente para no registrar errores
def add_sectores(nombre_sectores):
    try:
        connection = connect()  # Conexion a la BD valida
        cursor = connection.cursor()

        # Obtener el valor máximo actual de id
        cursor.execute("SELECT MAX(id) FROM sectores")
        max_id = cursor.fetchone()[0] + 1  # Sumamos 1 para asegurar que sea el siguiente valor autoincrementado

        # Insertar nuevo valor
        cursor.execute("INSERT INTO sectores (id, nombre) VALUES (%s, %s)", (max_id, nombre_sectores))
        
        # Confirmar la operación
        connection.commit()
        
        print("Nuevo registro en sector añadido correctamente.")
        cursor.execute("SELECT * FROM sectores")

        # Obtener todos los registros de la tabla
        registros_sector = cursor.fetchall()

        for registro in registros_sector:
            print(registro) 
        return registros_sector #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir registro en sector:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# aqui si ocupas darle el id del sector junto con el nombre para modificar
def update_sector(id_sector, nombre_sector): # valores de la tabla
    try:
        connection = connect()  # conexión a la base de datos
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM sectores WHERE id = %s", (id_sector,))
        sector_exists = cursor.fetchone()

        if not sector_exists: # evalua si existe el id
            print("El sector con el ID proporcionado no existe.")
            return  # Salir de la función 

        # Actualizar el registro existente
        cursor.execute("UPDATE sectores SET nombre = %s WHERE id = %s", (nombre_sector, id_sector))
        
        # Confirmar la operación
        connection.commit()
        
        print("Registro en Sector actualizado correctamente.")

        # Usamos el cursor para selecionar todos los elementos de la tabla
        cursor.execute("SELECT * FROM sectores")
        registros_sector = cursor.fetchall()

        # Imprimir los registros en la tabla
        for registro in registros_sector:
            print(registro)
        return registros_sector #imprime los valores de la tabla
    
    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar registro en sector:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# aqui ingresas el id para borrar
def delete_sectores(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sectores")

        # Eliminar un elemento de sectores
        cursor.execute(
            "DELETE FROM actividades_economicas WHERE sector = %s",
            (id,)
        )
        connection.commit()

        cursor.execute(
            "DELETE FROM sectores WHERE id = %s",
            (id,)
        )
        connection.commit()
        
        print("Elemento en Sector eliminado correctamente.")
        cursor.execute("SELECT * FROM sectores")

        registros_sector = cursor.fetchall()

        # Imprimir los registros en la tabla
        for registro in registros_sector:
            print(registro)
        return registros_sector #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar en Sector:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# aqui ingresas el nombre de la carrera, igualmente incrementa
def add_carreras(nombre_carrera):
    try:
        connection = connect() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM carreras")

        cursor.execute("SELECT MAX(id) FROM carreras")
        max_id = cursor.fetchone()[0] + 1 

        cursor.execute("INSERT INTO carreras (id, nombre) VALUES (%s, %s)", (max_id, nombre_carrera))
        
        connection.commit()
        
        print("Nueva carrera añadida correctamente.")
        cursor.execute("SELECT * FROM carreras")

        registros_carreras = cursor.fetchall()

        for registro in registros_carreras:
            print(registro)
        return registros_carreras #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir carrera:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# añáde el id, y nombre de la carrera a actualizar
def update_carreras(id_carrera, nombre_carrera): # valores de la tabla
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM carreras")

        cursor.execute("SELECT * FROM sectores WHERE id = %s", (id_carrera,))
        carrera_exists = cursor.fetchone()

        if not carrera_exists:
            print("La carrera con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE carreras SET nombre = %s WHERE id = %s", (nombre_carrera, id_carrera))
        
        connection.commit()
        
        print("Registro en Carrera actualizada correctamente.")
        cursor.execute("SELECT * FROM carreras")

        registros_carreras = cursor.fetchall()

        for registro in registros_carreras:
            print(registro)
        return registros_carreras #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar registro en carrera:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# se borra por id
def delete_carreras(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM carreras")

        cursor.execute(
            "DELETE FROM titulados WHERE carrera = %s",
            (id,)
        )
        connection.commit()

        cursor.execute(
            "DELETE FROM carreras WHERE id = %s",
            (id,)
        )
        connection.commit()
        
        print("Registro en Carrera eliminado correctamente.")
        cursor.execute("SELECT * FROM carreras")

        registros_carreras = cursor.fetchall()

        for registro in registros_carreras:
            print(registro)
        return registros_carreras #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar registro en Carrera:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# añade el id del periodo y la cantidad de población
def add_poblacion(periodo, cantidad_poblacion):
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM poblacion")

        cursor.execute("SELECT MAX(id) FROM poblacion")
        max_id = cursor.fetchone()[0] + 1 

        cursor.execute("INSERT INTO poblacion (id, periodo, cantidad) VALUES (%s, %s)", (max_id, periodo, cantidad_poblacion))
        
        connection.commit()
        
        print("Nuevo valor en poblacion añadido correctamente.")
        cursor.execute("SELECT * FROM poblacion")

        registros_poblacion = cursor.fetchall()

        for registro in registros_poblacion:
            print(registro)
        return registros_poblacion #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir poblacion:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# ingresa el id, numero de periodo que pertenece y la cantidad a corregir
def update_poblacion(id_poblacion, cantidad_poblacion): # valores de la tabla
    
    periodo = id_poblacion

    try:
        connection = connect() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM poblacion")
        
        cursor.execute("SELECT * FROM sectores WHERE id = %s", (id_poblacion,))
        poblacion_exists = cursor.fetchone()

        if not poblacion_exists:
            print("La carrera con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE poblacion SET periodo = %s, cantidad = %s WHERE id = %s", (periodo, cantidad_poblacion, id_poblacion))
        
        connection.commit()
        
        print("Elemento en Poblacion actualizado correctamente.")
        cursor.execute("SELECT * FROM poblacion")

        registros_poblacion = cursor.fetchall()

        for registro in registros_poblacion:
            print(registro)
        return registros_poblacion #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar registro en poblacion:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
#ingresa el id
def delete_poblacion(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM poblacion")

        cursor.execute(
            "DELETE FROM poblacion WHERE id = %s",
            (id,)
        )

        connection.commit()
        print("Registro en Poblacion eliminado correctamente.")
        cursor.execute("SELECT * FROM poblacion")

        registros_poblacion = cursor.fetchall()

        for registro in registros_poblacion:
            print(registro)
        return registros_poblacion #imprime los valores de la tabla
    
    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar registro en Poblacion:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# añade el nombre de la actividad y el id del sector al que pertenecerá
def add_actividad(nombre_actividad, id_sector):
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actividades_economicas")

        cursor.execute("SELECT MAX(id) FROM actividades economicas")
        max_id = cursor.fetchone()[0] + 1  
      
        cursor.execute("INSERT INTO actividades economicas (id, nombre, sector) VALUES (%s, %s, %s)", (max_id, nombre_actividad, id_sector))
        
        connection.commit()
        
        print("Nuevo registro en actividades economicas añadido correctamente.")
        cursor.execute("SELECT * FROM actividades_economicas")

        registros_actividades = cursor.fetchall()

        for registro in registros_actividades:
            print(registro)
        return registros_actividades #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir registro en actividades economicas:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# ingresa el id, nombre nuevo y sector nuevo (si es necesario)
def update_actividad(id_actividad, nombre_actividad, id_sector): # valores de la tabla
    try:
        connection = connect() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actividades_economicas")

        cursor.execute("SELECT * FROM sectores WHERE id = %s", (id_actividad,))
        actividad_exists = cursor.fetchone()

        if not actividad_exists:
            print("La carrera con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE actividades economicas SET nombre = %s, sector = %s WHERE id = %s", (nombre_actividad, id_sector, id_actividad))
        
        connection.commit()
        
        print("Registro en Actividad económica actualizada correctamente.")
        cursor.execute("SELECT * FROM actividades_economicas")

        registros_actividades = cursor.fetchall()

        for registro in registros_actividades:
            print(registro)
        return registros_actividades #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar la actividad económica:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# solo ingresa id y borras
def delete_actividad(id_act):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actividades_economicas")

        cursor.execute(
            "DELETE FROM resultados WHERE actividad = %s",
            (id_act,)
        )
        connection.commit()

        cursor.execute(
            "DELETE FROM actividades_economicas WHERE id = %s",
            (id_act,)
        )
        connection.commit()

        print("Registro en Actividad economica eliminado correctamente.")
        cursor.execute("SELECT * FROM actividades_economicas")

        registros_actividades = cursor.fetchall()

        for registro in registros_actividades:
            print(registro)
        return registros_actividades #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar registro en Actividad economica:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# añade el nombre a que periodo peretenece, id de la actividad y el el numero de resultado
def add_resultados(periodo, id_actividad, resultado):
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM resultados")

        cursor.execute("SELECT MAX(id) FROM resultados")
        max_id = cursor.fetchone()[0] + 1

        cursor.execute("INSERT INTO resultados (id, nombre, actividad, resultado) VALUES (%s, %s, %s, %s)", (max_id, periodo, id_actividad, resultado))
        
        connection.commit()
        
        print("Nuevo registro en resultados añadido correctamente.")
        cursor.execute("SELECT * FROM resultados")

        registros_resultados = cursor.fetchall()

        for registro in registros_resultados:
            print(registro)
        return registros_resultados #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir registro en resultados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# id, id del periodo del que pertenece, id de la actividad, y resultado nuevo
def update_resultados(id_resultado, periodo, id_actividad, resultado): # valores de la tabla
    try:
        connection = connect() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM resultados")

        cursor.execute("SELECT * FROM resultados WHERE id = %s", (id_actividad,))
        actividad_exists = cursor.fetchone()

        if not actividad_exists:
            print("El resultado con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE resultados SET nombre = %s, actividad = %s, resultado = %s WHERE id = %s", (periodo, id_actividad, resultado, id_resultado))
        
        connection.commit()
        
        print("Registro en Resultados actualizado correctamente.")
        cursor.execute("SELECT * FROM resultados")

        registros_resultados = cursor.fetchall()

        for registro in registros_resultados:
            print(registro)
        return registros_resultados #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar registro en resultados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

#id de resultados
def delete_resultados(id_resultados):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM resultados")
 
        cursor.execute(
            "DELETE FROM resultados WHERE id = %s",
            (id_resultados,)
        )

        connection.commit()
        print("Elemento en Resultados eliminado correctamente.")
        cursor.execute("SELECT * FROM resultados")

        registros_resultados = cursor.fetchall()

        for registro in registros_resultados:
            print(registro)
        return registros_resultados #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar registro en Resultados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# periodo al que pertenece, nombre de la nueva carrera, y graduados
def add_titulados(periodo, carrera, graduados):
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM titulados")

        cursor.execute("SELECT MAX(id) FROM titulados")
        max_id = cursor.fetchone()[0] + 1 
      
        cursor.execute("INSERT INTO titulados (id, periodo, carrera, graduados) VALUES (%s, %s, %s, %s)", (max_id, periodo, carrera, graduados))
        
        connection.commit()
        
        print("Nuevo registro en titulados añadido correctamente.")
        cursor.execute("SELECT * FROM titulados")

        registros_titulados = cursor.fetchall()

        for registro in registros_titulados:
            print(registro)
        return registros_titulados #imprime los valores de la tabla
    
    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir registro en titulados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# id_titulado, periodo cambiable, id_carrera, y nuevo valor a graduados
def update_titulados(id_titulado, periodo, id_carrera, graduados): # valores de la tabla titulados
    try:
        connection = connect() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM titulados")

        cursor.execute("SELECT * FROM titulados WHERE id = %s", (id_titulado,))
        actividad_exists = cursor.fetchone()

        if not actividad_exists:
            print("El valor en titulados con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE titulados SET periodo = %s, carrera = %s, graduados = %s WHERE id = %s", (periodo, id_carrera, graduados, id_titulado))
        
        connection.commit()
        
        print("Registro en titulados actualizado correctamente.")
        cursor.execute("SELECT * FROM titulados")

        registros_titulados = cursor.fetchall()

        for registro in registros_titulados:
            print(registro)
        return registros_titulados #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar registro en titulados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_titulados(id_titulados): #id_titulados
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM titulados")

        cursor.execute(
            "DELETE FROM titulados WHERE id = %s",
            (id_titulados,)
        )
        connection.commit()
        '''
        cursor.execute(
            "DELETE FROM carreras WHERE id = %s",
            (id_titulados,)
        )
        connection.commit()
        '''
        print("Elemento en Titulados eliminado correctamente.")
        cursor.execute("SELECT * FROM titulados")

        registros_titulados= cursor.fetchall()

        for registro in registros_titulados:
            print(registro)
        return registros_titulados #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al eliminar en Titulados:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# añade el nuevo año
def add_fechas(periodo): # periodo
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM fechas")

        cursor.execute("SELECT MAX(id) FROM fechas")
        max_id = cursor.fetchone()[0] + 1 

        cursor.execute("INSERT INTO fechas (id, periodo) VALUES (%s, %s)", (max_id, periodo))
        
        connection.commit()
        
        print("Nuevo valor en fechas añadido correctamente.")
        cursor.execute("SELECT * FROM fechas")

        registros_fechas = cursor.fetchall()

        for registro in registros_fechas:
            print(registro)
        return registros_fechas #imprime los valores de la tabla

    except (Exception, psycopg2.Error) as error:
        return print("Error al añadir fechas:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
# id, nuevo periodo
def update_fecha(id, nuevo_periodo): # valores de la tabla fecha
    try:
        connection = connect()  
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM fechas")

        cursor.execute("SELECT * FROM titulados WHERE id = %s", (id,))
        fecha_exists = cursor.fetchone()

        if not fecha_exists:
            print("El valor en titulados con el ID proporcionado no existe.")
            return  # Salir de la función
        
        cursor.execute("UPDATE fechas SET periodo = %s WHERE id = %s", (nuevo_periodo, id))
        
        connection.commit()
        
        print("Registro actualizado correctamente.")
        cursor.execute("SELECT * FROM fechas")

        registros_fechas = cursor.fetchall()

        for registro in registros_fechas:
            print(registro)
        return registros_fechas #imprime los valores de la tabla
        
    except (Exception, psycopg2.Error) as error:
        return print("Error al actualizar fecha:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# Llamada a las funciones
connect()

#backup()
#print("")
#tablas()
#print("")
#mostrar_registros("actividades_economicas")

#update_sector(12, "Cultural")
#add_sectores("Turistico")
#delete_actividad()
#delete_carreras()
#delete_poblacion()
#delete_resultados()
#delete_sectores()
#delete_titulados()
