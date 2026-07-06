from functions import *
import os

recorridos = {
    'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
    'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
    'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
    'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
    'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True],
}

venta = {
    'R001': [7990, 20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12],
}


acceso = True

while acceso:

    menu()
    opcion = leer_opcion()

    if opcion == 1:
        while True:
            origen = str(input("Ingrese ciudad de origen a consultar: ")).upper()
            if validacion_str(origen):
                break
        asientos_origen(recorridos,venta,origen)
    elif opcion == 2:
        acceso2 = True
        while acceso2:
            try:
                while True:
                    p_min = int(input("Ingrese precio mínimo: "))
                    if validacion_int_0(p_min):
                        break
                while True:
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_max > p_min:
                        break
                    print("El valor máximo debe ser mayor al mínimo.")
                busqueda_precio(recorridos, venta, p_min, p_max)
                acceso2 = False
            except:
                print("Debe ingresar valores enteros")
    elif opcion == 3:
        codigo_busqueda = str(input("Ingrese código del recorrido: ")).upper()
        while True:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if validacion_int(nuevo_precio):
                break
        if actualizar_precio(venta,codigo_busqueda,nuevo_precio):
            print("Precio actualizado.")
    elif opcion ==  4:
        nuevo_codigo = str(input("Ingrese código del recorrido: ")).upper() #buscarvodigo
        nuevo_origen = str(input("Ingrese origen: ")) #validacion_str
        nuevo_destino = str(input("Ingrese destino: ")) #validacion_str
        try:
            nueva_distancia = int(input("Ingrese distancia (km):")) #validacion_int
        except:
            print("Datos no validos, intente de nuevo.")
        nuevo_tipo_bus = str(input("Ingrese tipo de bus (normal/semi-cama/cama): ")) #validacionTIPOBUS
        nuevo_dia_noche = str(input("Ingrese servicio (dia/noche): "))
        nuevo_WIFI = ""
        while nuevo_WIFI not in ("S" ,"N"):
            nuevo_WIFI = str(input("¿Tiene WiFi? (s/n): ")).upper()
        try:
            nuevo_precio2 = int(input("Ingrese precio: ")) #validacion int
            nuevo_asiento = int(input("Ingrese asientos: ")) #validacion int
        except:
            print("Datos no validos, intente de nuevo.")
        
        if validacion_codigo(venta,nuevo_codigo):
            if validacion_str(nuevo_origen):
                if validacion_str(nuevo_destino):
                    if validacion_int(nueva_distancia):
                        if validacion_tipo_bus(nuevo_tipo_bus):
                            if validacion_dia_noche(nuevo_dia_noche):
                                if validacion_int(nuevo_precio2):
                                    if validacion_int_0(nuevo_asiento):
                                        agregar_recorrido(recorridos,venta,nuevo_codigo, nuevo_origen, nuevo_destino, nueva_distancia, nuevo_tipo_bus, nuevo_dia_noche, nuevo_WIFI, nuevo_precio2, nuevo_asiento)
                                    else:
                                        print("nuevos asientos invalidos.")
                                else:
                                    print("nuevo precio invalido.")
                            else:
                                print("validacion dia/noche invalida.")
                        else:
                            print("tipo de bus invalido.")
                    else:
                        print("distancia invalida.")
                else:
                    print("destino invalido.")
            else:
                print("origen invalido.")
        else:
            print("codigo invalido.")

    elif opcion == 5:
        while True:
            codigo = str(input("Ingrese el codigo a eliminar: ")).upper()
            if validacion_str(codigo):
                break
        if eliminar_recorrido(recorridos,venta,codigo):
            print("Recorrido eliminado")
        else:
            print("El codigo no existe.")
    else:
        print("Programa finalizado.")
        acceso = False
