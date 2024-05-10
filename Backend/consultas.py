import psycopg2
def connect():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            port='5432', 
            password='',  #Coloca tu contraseña
            database='crecimientojalisco' #cambia el nombre si lo tienes con otro
        )
        return connection
    except psycopg2.Error as ex:
        print("Error al conectar a la base de datos:", ex)
        return None
    
def consulta_agregadasum(nombre_columna, nombre_tabla):
    connection = connect()
    cursor = connection.cursor()

    try:
        query = "SELECT SUM(" + nombre_columna + ") FROM " + nombre_tabla + " "
        cursor.execute(query, (nombre_columna, nombre_tabla))
        
        resultado = cursor.fetchone()[0]
        return resultado

    except Exception as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        cursor.close()
        connection.close()

def consulta_agregadaavg(nombre_columna, nombre_tabla):
    connection = connect()

    cursor = connection.cursor()

    try:
        query = "SELECT AVG(" + nombre_columna + ") FROM " + nombre_tabla + " "
        cursor.execute(query, (nombre_columna, nombre_tabla))
        
        resultado = cursor.fetchone()[0]

        return resultado

    except Exception as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        cursor.close()
        connection.close()

def consulta_multitabla(tabla1, tabla2, columna_compartativa1, columna_compartativa2):
    try:
        connection = connect()
        cursor = connection.cursor()

        query = f"SELECT * FROM {tabla1} INNER JOIN {tabla2} ON {tabla1}.{columna_compartativa1} = {tabla2}.{columna_compartativa2}"

        cursor.execute(query)

        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila)
    except Exception as ex:
        print("Error al conectar a PostgreSQL:", ex)

    finally:
        if connection:
            cursor.close()
            connection.close()

def agregar_campo_calculado(tabla, nuevo_campo, expresion_calculada):
    try:
        connection = connect()
        cursor = connection.cursor()

        query_agregar_columna = f"ALTER TABLE {tabla} ADD COLUMN {nuevo_campo} NUMERIC"
        cursor.execute(query_agregar_columna)

        query_actualizar_valores = f"UPDATE {tabla} SET {nuevo_campo} = {expresion_calculada}"
        cursor.execute(query_actualizar_valores)

        connection.commit()
        print(f"Campo calculado '{nuevo_campo}' agregado a la tabla '{tabla}' con la expresión '{expresion_calculada}'")

    except Exception as ex:
        print("Error al conectar a PostgreSQL:", ex)

    finally:
        if connection:
            cursor.close()
            connection.close()

# Llamada a las variables
connect()
'''
agregar_campo_calculado("titulados", "nuevos_graduados", "graduados* 2")
nombre_columna = input("Ingresa el nombre de la columna a modificar: ")
nombre_tabla = input("Ingresa el nombre de la tabla a modificar: ")
resultado_avg = consulta_agregadaavg(nombre_columna, nombre_tabla)
print("El promedio de la columna es: {:.2f}" .format(resultado_avg))
resultado_suma = consulta_agregadasum(nombre_columna, nombre_tabla)
print("La suma de la columna es:", resultado_suma)
consulta_multitabla("sectores", "actividades_economicas", "id", "sector")
'''
