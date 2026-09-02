
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
            

insertar('')