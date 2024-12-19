from mysql.connector import connect, DatabaseError


def connnect_to_DB():
    try:
        con = connect(
            user="admin", password="admin", host="localhost", database="maktab"
        )
    except DatabaseError as e:
        print(f"Xatolik: {e}")

    except Exception as error:
        print(error)
