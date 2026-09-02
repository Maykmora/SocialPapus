import struct

def solicitar(codigo,nombre,fecha_nacimiento, seguidores,seguidos, bio):
    codigo_bytes=codigo.encode("utf-8")
    nombre_bytes=nombre.encode("utf-8")
    long_nombres=len(nombre_bytes)
    fecha_nacimiento_bytes=fecha_nacimiento.encode("utf-8")
    bio_bytes=bio.encode("utf-8")
    long_bios=len(bio_bytes)

    return struct.pack("<5sis10siiis", codigo_bytes,
                       long_nombres, nombre_bytes,
                       fecha_nacimiento_bytes,
                       seguidores,
                       seguidos,
                       long_bios,
                       bio_bytes)