
"""
POR REGISTRO

unpack[0] 64 -> Bytes que necesita TOD0 el registro
unpack[1] 15 -> Bytes de la parte del usuario
unpack[2.. inicio + 8] ... -> Datos del usuario: codigo, nombres... etc

si unpack[inicio + 9] no es null, entonces hay publicaciones (ej, en 12):
    unpack[12] 130 -> Bytes de la parte de la publicacion
    unpack[13.. inicio + 6] ... -> Datos de la publicacion: codigo, info...etc
    
    
    si unpack[inicio + 7] no es null, entonces hay comentarios (ej, en 20):
        unpack[20] 150 -> Bytes de la parte del comentario
        unpack[20.. inicio + 4 ] ... -> Datos del comentario: codigo, reaciones.. etc
        
        RECORRER EN UN BUCLE HASTA QUE LA POSICION ACTUAL DEL CURSOR SEA IGUAL AL TAMAÑO TOTAL DE LOS COMENTARIOS

    RECORRER EN UN BUCLE HASTA QUE LA POSICION ACTUAL DEL CURSOR SEA IGUAL AL TAMAÑO TOTAL DE LAS PUBLICACIONES

ALMACENAR USUARIO, PUBLICACIONES[] Y COMENTARIOS[] HASTA QUE LA POSICION ACTUAL DEL CURSOR SEA IGUAL AL TAMAÑO DE TOD0 EL REGISTRO 




EJ DE 1 REGISTRO:

TAMAÑO REGISTRO 1 | TAMAÑO USUARIO 1 | CODIGO USUARIO | lONG NOMBRE | NOMBRE DE USUARIO | FECHA | SEGUIDORES | SEGUIDOS | LONG BIO | BIO

TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 1 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO

TAMAÑO COMENTARIOS PUB 1 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO

"""


"""
VARIOS REGISTROS SERIAN ALGO ASÍ: 



TAMAÑO REGISTRO 2 | TAMAÑO USUARIO 2 | CODIGO USUARIO | lONG NOMBRE | NOMBRE DE USUARIO | FECHA | SEGUIDORES | SEGUIDOS | LONG BIO | BIO
    TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 2 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 2 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 3 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
    TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 3 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO 
        
        

TAMAÑO REGISTRO 3 | TAMAÑO USUARIO 3 | CODIGO USUARIO | lONG NOMBRE | NOMBRE DE USUARIO | FECHA | SEGUIDORES | SEGUIDOS | LONG BIO | BIO
    TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 1 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO
        TAMAÑO COMENTARIOS PUB 1 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
    TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 3 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
    TAMAÑO PUBLICACIONES | TAMAÑO PUBLICACION 3 | CODIGO PUBLICACION | FECHA PUBLICACION | REACCIONES | COMPARTIDOS | LONG CONTENIDO | CONTENIDO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
        TAMAÑO COMENTARIOS PUB 2 | TAMAÑO COMENTARIO 1 | REACCIONES | LONG INFO COMENTARIO | INFO COMENTARIO
"""

import struct
import os

FILE_PATH = "result/usuario.bin"

def leer_y_mostrar_registros():
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo aún no existe. ¡Registra algo de información primero!")
        return

    with open(FILE_PATH, "rb") as f:
        print("\n--- MOSTRANDO TODOS LOS REGISTROS ---")
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            tam_usuario = struct.unpack("<i", f.read(4))[0]
            codigo = f.read(5).decode("utf-8").strip('\x00')
            
            long_nombres = struct.unpack("<i", f.read(4))[0]
            nombre = f.read(long_nombres).decode("utf-8")
            fecha_nacimiento = f.read(10).decode("utf-8").strip('\x00')
            seguidores, seguidos, long_bios = struct.unpack("<iii", f.read(12))
            bio = f.read(long_bios).decode("utf-8")
            
            print(f"\nID: {codigo} | Nombre: {nombre}")
            print(f"Fecha Nacimiento: {fecha_nacimiento} | Seguidores: {seguidores} | Seguidos: {seguidos}")
            print(f"Bio: {bio}")
            
            # Calcular lo que ya leímos y saltar el resto (publicaciones y comentarios)
            bytes_leidos_seccion = 4 + 5 + 4 + long_nombres + 10 + 12 + long_bios
            bytes_restantes = tam_registro - bytes_leidos_seccion - 4 
            if bytes_restantes > 0:
                f.seek(bytes_restantes, 1)

def buscar_por_id(id_buscado):
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo no existe.")
        return

    encontrado = False
    with open(FILE_PATH, "rb") as f:
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            tam_usuario = struct.unpack("<i", f.read(4))[0]
            codigo_actual = f.read(5).decode("utf-8").strip('\x00')
            
            if codigo_actual == id_buscado:
                encontrado = True
                print(f"\n¡Usuario {id_buscado} encontrado!")
                
                long_nombres = struct.unpack("<i", f.read(4))[0]
                nombre = f.read(long_nombres).decode("utf-8")
                fecha = f.read(10).decode("utf-8").strip('\x00')
                seguidores, seguidos, long_bios = struct.unpack("<iii", f.read(12))
                bio = f.read(long_bios).decode("utf-8")
                
                print(f"Nombre: {nombre}")
                print(f"Bio: {bio}")
                break 
            else:
                # Saltar al siguiente registro si no es el que buscamos
                f.seek(tam_registro - 9 - 4, 1) 
                
    if not encontrado:
        print(f"\nNo se encontró ningún usuario con el código {id_buscado}.")