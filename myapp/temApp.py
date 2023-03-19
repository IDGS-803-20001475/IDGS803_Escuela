from db import get_connection

""" try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumnos()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()
except Exception as ex:
    print(ex) """

""" try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumno(%s)',(1,))
        resultset=cursor.fetchall()
        #for row in resultset:
        print(resultset)
    connection.close()
except Exception as ex:
    print(ex) """

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agrega_alumno(%s,%s,%s,%s)',("Armando","Ramirez Patlán","armando23@gmail.com","2023-03-11 11:23:00"))
    connection.commit()
    connection.close()
except Exception as ex:
    print(ex)