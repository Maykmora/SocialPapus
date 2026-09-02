import struct
def empaquetar_comentario(comentario, codigo, fecha, info, reacciones, tamanio_comentario):
    comentario_bytes = comentario.encode("utf-8")
    tam = len(comentario_bytes)
    codigo_bytes = codigo.encode("utf-8")
    tam_codigo = len(codigo_bytes)
    fecha_bytes = fecha.encode("utf-8")
    tam_fecha = len(fecha_bytes)
    info_bytes = info.encode("utf-8")
    tam_info = len(info_bytes)
    reacciones_bytes = reacciones.encode("utf-8")
    num_reacciones = len(reacciones_bytes)
    formato = f"<i5sis10siiis"
    bytes_empaquetados = struct.pack(tam, comentario_bytes, tam_codigo, codigo_bytes, tam_fecha,
        fecha_bytes,
        tam_info,
        info_bytes,
        num_reacciones,
        reacciones_bytes, tamanio_comentario) 

    return (formato, bytes_empaquetados)