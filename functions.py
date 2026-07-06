import os,time

def _pausa(x):
    time.sleep(x)

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    opcion = 0
    while opcion not in [1,2,3,4,5,6]:
        try:
            opcion =int(input("Ingrese opcion: "))
            if opcion not in [1,2,3,4,5,6]:
                print("Debe seleccionar una opción válida")
                _pausa(2)
        except:
            print("Datos no validos, intente denuevo")
            _pausa(2)
    return opcion

def validacion_str(palabra):
    if "" in palabra.strip():
        return True
    return False

def asientos_origen(recorridos,venta,origen):
    total = 0
    for codigo in recorridos:
        if recorridos[codigo][0].upper() == origen.upper():
            total += venta[codigo][1]
    print(f"El total de asientos disponibles es: {total}")
    _pausa(2)

def validacion_int_0(numero):
    if numero >= 0:
        return True
    print("El numero debe ser mayor o igual a 0.")
    return False

def validacion_int(numero):
    if numero > 0:
        return True
    print("El numero debe ser mayor a 0.")
    return False

def busqueda_precio(recorridos,venta,p_min, p_max):
    lista = []
    for codigo in venta:
        if venta[codigo][0] >= p_min and venta[codigo][0] <= p_max:
            if venta[codigo][1] >0:
                lista.append(recorridos[codigo][0] + "-" + recorridos[codigo][1] + "--" + codigo)
    lista.sort()
    print(f"Los recorridos encontrados son: {lista}")
    _pausa(3)

def _buscar_codigo(venta,codigo_busqueda):
    for codigo in venta:
        if codigo.upper() == codigo_busqueda.upper():
            return True
    return False

def actualizar_precio(venta,codigo_busqueda,nuevo_precio):
    if _buscar_codigo(venta,codigo_busqueda):
        for codigo in venta:
            if codigo.upper() == codigo_busqueda.upper():
                venta[codigo][0] = nuevo_precio
                return True
    else:
        print("El código no existe") #NO SE COMO RETORNAR FALSE Y LUEGO PREGUNAR
        while True:
            siono = str(input("¿Desea actualizar otro precio (s/n)?: ")).upper()
            if validacion_si_no(siono):
                break
        if siono == "S":
            codigo_busqueda = str(input("Ingrese código del recorrido: ")).upper()
            while True:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if validacion_int(nuevo_precio):
                    break
            actualizar_precio(venta,codigo_busqueda,nuevo_precio)

def validacion_codigo(venta, nuevo_codigo):
    if nuevo_codigo.strip() == "":
        return False
    else:
        for codigo in venta:
            if codigo.upper() == nuevo_codigo.upper():
                return False
        return True

def validacion_si_no(siono):
    while siono.upper() not in ("S", "N"):
        siono = input("¿S/N? ").upper()
    _pausa(2)
    return True

def validacion_tipo_bus(tipo):
    if tipo.lower() in ("normal","semi-cama","cama"):
        return True
    return False

def validacion_dia_noche(dianoche):
    if dianoche.lower() in ("dia","noche"):
        return True
    return False

def agregar_recorrido(recorridos,venta,nuevo_codigo, nuevo_origen, nuevo_destino, nueva_distancia, nuevo_tipo_bus, nuevo_dia_noche, nuevo_WIFI, nuevo_precio2, nuevo_asiento):
    recorridos.update({
        nuevo_codigo : [nuevo_origen,nuevo_destino,nueva_distancia,nuevo_tipo_bus,nuevo_dia_noche,nuevo_WIFI]
    })
    venta.update({
        nuevo_codigo : [nuevo_precio2,nuevo_asiento]
    })

def eliminar_recorrido(recorridos, venta, codigo):
    if _buscar_codigo(venta,codigo):
        recorridos.pop(codigo)
        venta.pop(codigo)
        return True
    else:
        return False