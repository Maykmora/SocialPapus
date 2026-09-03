import leer # <- Esto es nuevo e importante para conectar los archivos

FILE_PATH = "result/usuario.bin"

while True:
    print("SOCIAL PAPU".center(100, '='))
    print("""1) Registrar Informacion
2) Leer registros
3) Mostrar datos recuperados correctamente
4) Buscar registro por ID
5) Mostrar posicion incial de cada registro
6) Mostrar cantidad de bytes por registro
7) Mostrar tamaño del archivo
8) Salir
""")
    
    op = input("> Ingresa la opción: ")
    match op:
        # Añadimos tus opciones aquí
        case '2' | '3':
            leer.leer_y_mostrar_registros()
            
        case '4':
            id_a_buscar = input("Ingresa el ID del usuario a buscar (Ej. US000): ")
            leer.buscar_por_id(id_a_buscar)
            
        case '8': 
            break