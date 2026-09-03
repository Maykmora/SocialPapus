"""
Moshe Pelaez - 1556425
Angelo Garcia - 1554725
Maynor Morales - 1553025
Cristian Chávez - 1666325
Rodrigo Pinto - 1507325
"""

import leer
import insertar

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
        case '1': 
            insertar.insertar(FILE_PATH)
        case '2':
            leer.leer_y_mostrar_registros()
        case '3': leer.recuperados()
        case '4':
            id_a_buscar = input("Ingresa el ID del usuario a buscar (Ej. US000): ")
            leer.buscar_por_id(id_a_buscar)
        case '5': leer.mostrar_inicial()
        case '6': leer.bytes_por_reg()
        case '7': leer.size_total()
        case '8': 
            break