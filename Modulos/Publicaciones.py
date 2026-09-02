import struct

def empaquetar_publicacion(codigo_pub: str, info: str, likes: int, fecha: str, compartidos: int, tam_comen: int):
    bytes_codigo = codigo_pub.encode('utf-8')[:5].ljust(5, b'\x00')
    bytes_info = info.encode('utf-8')
    len_info = len(bytes_info)
    bytes_fecha = fecha.encode('utf-8')[:10].ljust(10, b'\x00')
    tam_pub = 31 + len_info

    #formato
    formato = f"<i5si{len_info}si10sii"

    bytes_empaquetados = struct.pack(
        formato,
        tam_pub,
        bytes_codigo,
        len_info,
        bytes_info,
        likes,
        bytes_fecha,
        compartidos,
        tam_comen
    )
    return (formato, bytes_empaquetados)
