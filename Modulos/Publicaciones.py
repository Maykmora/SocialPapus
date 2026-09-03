import struct

def empaquetar_publicacion(codigo_pub: str, info: str, likes: int, fecha: str, compartidos: int, tam_comen: int):
    bytes_codigo = codigo_pub.encode('utf-8')[:5].ljust(5, b'\x00')
    bytes_info = info.encode('utf-8')
    len_info = len(bytes_info)
    bytes_fecha = fecha.encode('utf-8')[:10].ljust(10, b'\x00')
    
    formato = f"5si{len_info}s10siii"
    tam_pub = struct.calcsize("<i" + formato)
    formato = f"<i{formato}"
    
    #formato
    bytes_empaquetados = struct.pack(
        formato,
        tam_pub,
        bytes_codigo,
        len_info,
        bytes_info,
        bytes_fecha,
        likes,
        compartidos,
        tam_comen
    )
    
    return (formato, bytes_empaquetados)

#empaquetar_publicacion('PB001', '12345678', 15, '2026/05/08', 20, 0)