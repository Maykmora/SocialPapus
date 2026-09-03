import struct
def empaquetar_comentario(codigo, fecha, info, reacciones):
    codigo_bytes = codigo.encode("utf-8")[:5].ljust(5, b'\x00') #4
    fecha_bytes = fecha.encode("utf-8")[:10].ljust(10, b'\x00') #10
    info_bytes = info.encode("utf-8") # N
    tam_info = len(info_bytes) # 4
    formato = f"5s10si{tam_info}si"
    size = struct.calcsize("<i" + formato)
    formato = "<i" + formato
    
    bytes_empaquetados = struct.pack(formato,
        size,
        codigo_bytes,
        fecha_bytes,
        tam_info, info_bytes,
        reacciones
    ) 
    
    return (formato, bytes_empaquetados)

#empaquetar_comentario("CM001", "2026/04/20", '123456', 15)