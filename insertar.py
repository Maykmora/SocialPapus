import struct
from Modulos.Publicaciones import empaquetar_publicacion
from Modulos.comentarios import empaquetar_comentario
from Modulos.users import empaquetar_usuario

def insertar_comentario():
    code_pub = input(" > Ingresa codigo del comentario (Formato: CM000): ")
    date = input(" > Ingresa la fecha de tu comentario (Formato: YYYY/MM/DD): ")
    reactions = int(input(" > Ingresa la cantidad de reacciones del comentario: "))
    info = input(" > Ingresa lo que quieres comentar: ")
    
    return empaquetar_comentario(code_pub, date, info, reactions)
    
def insertar_publicacion():
    pub_com, coms = False, []
    
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
    
    amount_com = 0
    if pub_com:
        print(f"\n*** Comentarios de la publicacion: {code_pub}")
        amount_com =  int(input(" > Ingresa la cantidad de comentarios: "))
        for _ in range(amount_com):
            print(f"\n* Comentario {_+1}")
            coms.append(insertar_comentario())

    
    return empaquetar_publicacion(code_pub, bio,reactions, date, compartidos, amount_com), coms

def insertar(file_path:str):
    pub_con, pubs = False, []
    
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
    
    amount_pub = 0
    if pub_con:
        print("PUBLICACIONES".center(50, '-'))
        amount_pub =  int(input(" > Ingresa la cantidad de publicaciones: "))
        
        for _ in range(amount_pub):
            print(f"\n***** Publicacion {_+1}")
            pubs.append(insertar_publicacion())
    
    user = empaquetar_usuario(code_user, name, date, followers, follow, bio, amount_pub) 
    
    formato_user = "" + user[0].replace("<", '')
    data_user = user[1]
    #print("USUARIO: ", user[0])
    for registro in pubs:
        formato_data_user = ""
        codigo = registro[0][0].replace("<", "")
        formato_data_user += codigo
        data_user += registro[0][1]
        #print("PUBLICACION: ", codigo)
        if registro[1]:
            for comentario in registro[1]:
                formato_data_user += comentario[0].replace("<", "")
                data_user += comentario[1]
                #print("COMENTARIO: ",comentario[0])
        formato_user += formato_data_user

    total_size_register = struct.calcsize("<"+formato_user) +4 #4 porque aun no le he agregado el mismo total_size
    
    print("F: ",formato_user)
    print(data_user)
    print("size total: ", total_size_register)

    with open(file_path, 'ab') as file:
        file.write(
            struct.pack("<i", total_size_register) + (data_user)
        )
        
    print("\n Datos insertados!")

#insertar('')