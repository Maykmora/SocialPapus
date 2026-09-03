import struct

def empaquetar_usuario(codigo,nombre,fecha_nacimiento, seguidores,seguidos, bio, pubs):
    codigo_bytes=codigo.encode("utf-8")[:5].ljust(5, b'\x00')
    nombre_bytes=nombre.encode("utf-8")
    long_nombre=len(nombre_bytes)
    fecha_nacimiento_bytes= fecha_nacimiento.encode("utf-8").ljust(5, b'\x00')
    bio_bytes=bio.encode("utf-8")
    long_bio=len(bio_bytes)

    formato = f"5si{long_nombre}s10siii{long_bio}si"
    tam = struct.calcsize("<i" + formato)
    formato = f"<i{formato}"
    bytes_empaquetados = struct.pack(formato, 
        tam, 
        codigo_bytes, 
        long_nombre, nombre_bytes, 
        fecha_nacimiento_bytes, 
        seguidores, 
        seguidos, 
        long_bio, bio_bytes,
        pubs
    )
    return (formato, bytes_empaquetados)


#solicitar('PB001','12345','2026/04/11',15,10,"12345678")