import pymysql

class Conexion:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'cv23952018',
            db = 'crud'
        )

        self.cursor = self.connection.cursor()

        print('base de datos conectada')

    def mostrarRegistro(self, name):
        sql = "SELECT id, nombre, email, telefono FROM usuarios WHERE nombre = '{}' ".format(name)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            raise

    def All_user(self):
        sql= 'SELECT id, nombre, email, telefono FROM usuarios'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
        except Exception as e:
            raise


    def regis_User(self, datos):
        sql = "INSERT INTO usuarios (nombre, email, telefono) VALUES ( '{}', '{}', '{}')".format(datos[0], datos[1], datos[2])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise


    def update_user(self, datos):
        sql = "UPDATE usuarios SET nombre = '{}', email = '{}', telefono = '{}' WHERE id = '{}' ".format(datos[1], datos[2], datos[3], datos[0])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise


    def delete_user(self, name):
        sql = "DELETE FROM usuarios WHERE nombre = '{}' ".format(name)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise


