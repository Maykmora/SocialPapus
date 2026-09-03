import struct
import os

FILE_PATH = "result/usuario.bin"

def leer_y_mostrar_registros():
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo aún no existe. Registra algo de información primero!")
        return

    with open(FILE_PATH, "rb") as f:
        print("\n--- MOSTRANDO TODOS LOS REGISTROS ---")
        num = 1
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            
            print()
            print(f"REGISTRO {num} ({tam_registro} Bytes)".center(50,'-'))
            tam_usuario = struct.unpack("<i", f.read(4))[0]
            codigo = f.read(5).decode("utf-8").strip('\x00')
            
            long_nombres = struct.unpack("<i", f.read(4))[0]
            nombre = f.read(long_nombres).decode("utf-8")
            fecha_nacimiento = f.read(10).decode("utf-8").strip('\x00')
            seguidores, seguidos, long_bios = struct.unpack("<iii", f.read(12))
            bio = f.read(long_bios).decode("utf-8")
            
            c_publicacions = struct.unpack("<i", f.read(4))[0]
            
            print(f"ID User: {codigo} | Nombre: {nombre}")
            print(f"Fecha Nacimiento: [{fecha_nacimiento}] | Seguidores: {seguidores} | Seguidos: {seguidos}")
            print(f"Bio: {bio}")
            print(f"Cantidad de publicacones: {c_publicacions}")
            
            for _ in range(c_publicacions):
                tam_pub = struct.unpack("<i", f.read(4))[0]
                codigo_pub = f.read(5).decode("utf-8").strip('\x00')
                
                len_content_pub = struct.unpack("<i", f.read(4))[0]
                content_pub = f.read(len_content_pub).decode("utf-8")
                
                fecha_pub = f.read(10).decode("utf-8")
                reacciones_pub, compartidos, cant_comentarios = struct.unpack("<iii", f.read(12))

                print("\t","".center(50,'-'))
                print(f"\t[Publicacion {_+1}/{c_publicacions}] ID PUB: {codigo_pub}")
                print(f"\t{content_pub}")
                print(f"\tFecha: [{fecha_pub}] | Reacciones: {reacciones_pub} | Compartidos: {compartidos}")
                print(f"\tComentarios registrados: {cant_comentarios}")

                #COMENTARIOS
                for __ in range(cant_comentarios):
                    tam_comentario = struct.unpack("<i", f.read(4))[0]
                    codigo_com = f.read(5).decode("utf-8").strip('\x00')
                    fecha_com = f.read(10).decode("utf-8")
                    
                    len_texto_com = struct.unpack("<i", f.read(4))[0]
                    texto_com = f.read(len_texto_com).decode("utf-8")
                    
                    reacciones_com = struct.unpack("<i", f.read(4))[0]

                    print(f"\t\t* (Comentario {__+1}) ID: {codigo_com} [{fecha_com}] (Reacciones: {reacciones_com}):")
                    print(f"\t\t  {texto_com}")

            num += 1
            
            #bytes_leidos_seccion = 4 + 5 + 4 + long_nombres + 10 + 12 + long_bios
            #bytes_restantes = tam_registro - bytes_leidos_seccion - 4 
            #if bytes_restantes > 0:
            #    f.seek(bytes_restantes, 1)

def recuperados():
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo aún no existe. Registra algo de información primero!")
        return

    with open(FILE_PATH, "rb") as f:
        print("\n REGISTROS RECUPERADOS CORRECTAMENTE!")
        num = 1
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                print("EXISTE UN REGISTRO CORRUPTO!")
                break
            
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            
            print()
            print(f"REGISTRO {num} ({tam_registro} Bytes)".center(50,'-'))
            tam_usuario = struct.unpack("<i", f.read(4))[0]
            codigo = f.read(5).decode("utf-8").strip('\x00')
            
            long_nombres = struct.unpack("<i", f.read(4))[0]
            nombre = f.read(long_nombres).decode("utf-8")
            fecha_nacimiento = f.read(10).decode("utf-8").strip('\x00')
            seguidores, seguidos, long_bios = struct.unpack("<iii", f.read(12))
            bio = f.read(long_bios).decode("utf-8")
            
            c_publicacions = struct.unpack("<i", f.read(4))[0]
            

            for _ in range(c_publicacions):
                tam_pub = struct.unpack("<i", f.read(4))[0]
                codigo_pub = f.read(5).decode("utf-8").strip('\x00')
                
                len_content_pub = struct.unpack("<i", f.read(4))[0]
                content_pub = f.read(len_content_pub).decode("utf-8")
                
                fecha_pub = f.read(10).decode("utf-8")
                reacciones_pub, compartidos, cant_comentarios = struct.unpack("<iii", f.read(12))

                for __ in range(cant_comentarios):
                    tam_comentario = struct.unpack("<i", f.read(4))[0]
                    codigo_com = f.read(5).decode("utf-8").strip('\x00')
                    fecha_com = f.read(10).decode("utf-8")
                    
                    len_texto_com = struct.unpack("<i", f.read(4))[0]
                    texto_com = f.read(len_texto_com).decode("utf-8")
                    
                    reacciones_com = struct.unpack("<i", f.read(4))[0]

                    print(f"\t\t* (Comentario {__+1}) ID: {codigo_com} [{fecha_com}] (Reacciones: {reacciones_com}):")
                    print(f"\t\t  {texto_com}")

            print(" - El registro {", f"ID User: {codigo} | Nombre: {nombre}", "} Fue recuperado correctamente")
            num += 1
            

def buscar_por_id(id_buscado):
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo no existe.")
        return

    encontrado = False
    with open(FILE_PATH, "rb") as f:
        while True:
            bytes_tam_registro = f.read(4)
            if encontrado: break
            if not bytes_tam_registro:
                print("EXISTE UN REGISTRO CORRUPTO!")
                break
            
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]

            tam_usuario = struct.unpack("<i", f.read(4))[0]
            codigo = f.read(5).decode("utf-8").strip('\x00')
            
            long_nombres = struct.unpack("<i", f.read(4))[0]
            nombre = f.read(long_nombres).decode("utf-8")
            fecha_nacimiento = f.read(10).decode("utf-8").strip('\x00')
            seguidores, seguidos, long_bios = struct.unpack("<iii", f.read(12))
            bio = f.read(long_bios).decode("utf-8")
            
            c_publicacions = struct.unpack("<i", f.read(4))[0]
            
            if codigo == id_buscado:
                encontrado = True
                print("".center(50,'-'))
                print(f"ID User: {codigo} | Nombre: {nombre}")
                print(f"Fecha Nacimiento: [{fecha_nacimiento}] | Seguidores: {seguidores} | Seguidos: {seguidos}")
                print(f"Bio: {bio}")
                print(f"Cantidad de publicacones: {c_publicacions}")

            for _ in range(c_publicacions):
                tam_pub = struct.unpack("<i", f.read(4))[0]
                codigo_pub = f.read(5).decode("utf-8").strip('\x00')
                
                len_content_pub = struct.unpack("<i", f.read(4))[0]
                content_pub = f.read(len_content_pub).decode("utf-8")
                
                fecha_pub = f.read(10).decode("utf-8")
                reacciones_pub, compartidos, cant_comentarios = struct.unpack("<iii", f.read(12))

                if encontrado: 
                    print("\t","".center(50,'-'))
                    print(f"\t[Publicacion {_+1}/{c_publicacions}] ID PUB: {codigo_pub}")
                    print(f"\t{content_pub}")
                    print(f"\tFecha: [{fecha_pub}] | Reacciones: {reacciones_pub} | Compartidos: {compartidos}")
                    print(f"\tComentarios registrados: {cant_comentarios}")

                for __ in range(cant_comentarios):
                    tam_comentario = struct.unpack("<i", f.read(4))[0]
                    codigo_com = f.read(5).decode("utf-8").strip('\x00')
                    fecha_com = f.read(10).decode("utf-8")
                    
                    len_texto_com = struct.unpack("<i", f.read(4))[0]
                    texto_com = f.read(len_texto_com).decode("utf-8")
                    
                    reacciones_com = struct.unpack("<i", f.read(4))[0]

                    if encontrado:
                        print(f"\t\t* (Comentario {__+1}) ID: {codigo_com} [{fecha_com}] (Reacciones: {reacciones_com}):")
                        print(f"\t\t  {texto_com}")


    if not encontrado:
        print(f"\nNo se encontró ningún usuario con el código {id_buscado}.")
        
        
def mostrar_inicial():
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo aún no existe. Registra algo de información primero!")
        return
    
    with open(FILE_PATH, "rb") as f:
        num = 1
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            print(f" - REGISTRO {num} inicia en: {f.tell()} Byte")
                        
            f.seek(tam_registro-4, 1)
            num+=1

def bytes_por_reg():
    if not os.path.exists(FILE_PATH):
        print("\nEl archivo aún no existe. Registra algo de información primero!")
        return
    
    with open(FILE_PATH, "rb") as f:
        num = 1
        while True:
            pos = f.tell()
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            tam_registro = struct.unpack("<i", bytes_tam_registro)[0]
            print(f" - REGISTRO {num} ({tam_registro} Bytes) inicia en: {pos} Byte")
                        
            f.seek(tam_registro-4, 1)
            num+=1


def size_total():
    if not os.path.exists(FILE_PATH):
            print("\nEl archivo aún no existe. Registra algo de información primero!")
            return
        
    with open(FILE_PATH, "rb") as f:
        size_total = 0
        while True:
            bytes_tam_registro = f.read(4)
            if not bytes_tam_registro:
                break
            size_total += len(bytes_tam_registro)
        print(f"\nTamaño de todo el archivo: {size_total} Bytes")