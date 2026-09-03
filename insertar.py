import os
import struct


def insertar_comentario():
    code_pub = input(" > Ingresa codigo del comentario (Formato: CM000): ")
    reactions = int(input(" > Ingresa la cantidad de reacciones del comentario: "))
    info = input(" > Ingresa lo que quieres comentar: ")
    
def insertar_publicacion():
    pub_com = False
    
    code_pub = input(" > Ingresa codigo de publicación (Formato: PB000): ")
    date = input(" > Ingresa la fecha de tu publicación (Formato: YYYY/MM/DD): ")
    reactions = int(input(" > Ingresa la cantidad de reacciones: "))
    compartidos = int(input(" > Ingresa la cantidad de compartidos: "))
    
    bio = input(" > Ingresa lo que quieres publicar: ")
    
    while True:
        op_com = input(" > Quieres agregar comentarios (Y/n): ")
        
        if op_com == 'Y': 
            pub_com = True
            break
        elif op_com == 'n': break
        else: print(" / la opción no fue valida, vuelve a intentarlo\n")
    
    if pub_com:
        print(f"*** Comentarios de la publicacion: {code_pub}")
        amount_com =  int(input(" > Ingresa la cantidad de comentarios: "))

        for _ in range(amount_com):
            print(f"* Comentario {_+1}")
            insertar_comentario()


def insertar(file_path:str):
    pub_con = False
    
    code_user = input(" > Ingresa codigo de usuario (Formato: US000): ")
    name = input(" > Ingresa nombre del usuario: ")
    date = input(" > Ingresa tu fecha de nacimiento (Formato: YYYY/MM/DD): ")
    followers = int(input(" > Ingresa tu cantidad de seguidores: "))
    follow = int(input(" > Ingresa la catnidad de cuentas que sigues: "))
    bio = input(" > Ingresa tu biografia: ")

    # --- INICIO DEL PARCHE PARA PROBAR CÓDIGO ---
    codigo_bytes = code_user.encode("utf-8").ljust(5, b'\x00')
    nombre_bytes = name.encode("utf-8")
    long_nombres = len(nombre_bytes)
    fecha_bytes = date.encode("utf-8").ljust(10, b'\x00')
    bio_bytes = bio.encode("utf-8")
    long_bios = len(bio_bytes)
    
    formato = f"<5si{long_nombres}s10siii{long_bios}s"
    bytes_usuario = struct.pack(formato, codigo_bytes, long_nombres, nombre_bytes, fecha_bytes, followers, follow, long_bios, bio_bytes)
    
    tam_usuario = len(bytes_usuario)
    tam_registro = tam_usuario + 4 
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "ab") as f:
        f.write(struct.pack("<i", tam_registro))
        f.write(struct.pack("<i", tam_usuario))
        f.write(bytes_usuario)
    print("\n[!] Usuario guardado temporalmente en el .bin para pruebas.")
    # --- FIN DEL PARCHE ---
    
    while True:
        op_pub = input(" > Quieres agregar publicaciones (Y/n): ")
        
        if op_pub == 'Y': 
            pub_con = True
            break
        elif op_pub == 'n': break
        else: print(" / la opción no fue valida, vuelve a intentarlo\n")
    
    if pub_con:
        print("PUBLICACIONES".center(50, '-'))
        amount_pub =  int(input(" > Ingresa la cantidad de publicaciones: "))
        
        for _ in range(amount_pub):
            print(f"***** Publicacion {_+1}")
            insertar_publicacion()
            

if __name__ == "__main__":
    insertar("result/usuario.bin")