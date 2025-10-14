from db import Conexion 

# La función devuelve una lista de tuplas con el historial de las órdenes
# cada tupla representa una orden con los campos:
# (id, date, customer, payment, delivery, total) (checar los campos)
def obtener_historial_ordenes():
    conn = Conexion.Conexion()
    # asegurarse de que la conexión fue exitosa
    # nos aseguramos de que la conexion no sea None, si es asi retornamos lista vacia
    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, date, customer, payment, delivery, total FROM orders ORDER BY date DESC")
        resultados = cursor.fetchall()
        data = []
        for row in resultados:
            data.append((
                str(row[0]),  # id como string
                row[1].strftime("%d %b %Y %H:%M") if hasattr(row[1], 'strftime') else str(row[1]),  # formatear fecha
                row[2],  # customer
                row[3],  # payment
                row[4],  # delivery
                f"${row[5]:.2f}"  # total con formato monetario
            ))
        return data
    except Exception as e:
        print(f"Error al obtener historial de órdenes: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
# nota: ajustar los campos según nuestra base de datos real
