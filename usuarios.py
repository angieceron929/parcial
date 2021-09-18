from bd import conexion

class RegistroUsu():
    def insertarUsu(self,nombre,email,password):
        conexions = conexion()
        with conexions.cursor() as cursor:
        
            cursor.execute("""insert into usuarios(
                nombre,
                email,
                contrasena
            )values (%s ,%s ,%s)
             """, (nombre,email,password,))
        conexions.commit()
        conexions.close()

    def login(self,email,password):
        conexions = conexion()
        usuario = None
        with conexions.cursor() as cursor:
            cursor.execute(""" select * from usuarios
            where email = %s and contrasena =%s""",(email,password,))
            usuario= cursor.fetchone()
        
        conexions.close()
        return usuario




