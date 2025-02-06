from datetime import datetime
from datos import cargar_datos, guardar_datos

def registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
    libros = cargar_datos('libros.json')
    nuevo_libro = {
        "id_libro": len(libros) + 1,
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "anio_publicacion": anio_publicacion,
        "genero": genero,
        "cantidad_disponible": cantidad_disponible
    }
    libros.append(nuevo_libro)
    guardar_datos('libros.json', libros)

def eliminar_libro(id_libro):
    libros = cargar_datos('libros.json')
    libros = [libro for libro in libros if libro["id_libro"] != id_libro]
    guardar_datos('libros.json', libros)

def buscar_libros(criterio, valor):
    libros = cargar_datos('libros.json')
    return [libro for libro in libros if libro[criterio].lower() == valor.lower()]

def registrar_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
    socios = cargar_datos('socios.json')
    nuevo_socio = {
        "id_socio": len(socios) + 1,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": direccion,
        "correo_electronico": correo_electronico,
        "telefono": telefono
    }
    socios.append(nuevo_socio)
    guardar_datos('socios.json', socios)

def eliminar_socio(id_socio):
    socios = cargar_datos('socios.json')
    socios = [socio for socio in socios if socio["id_socio"] != id_socio]
    guardar_datos('socios.json', socios)

def buscar_socios(criterio, valor):
    socios = cargar_datos('socios.json')
    return [socio for socio in socios if socio[criterio].lower() == valor.lower()]

def registrar_prestamo(id_socio, id_libro, costo):
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

    libro_disponible = None
    for libro in libros:
        if libro["id_libro"] == id_libro and libro["cantidad_disponible"] > 0:
            libro_disponible = libro
            break

    if not libro_disponible:
        raise ValueError("El libro no está disponible.")

    nuevo_prestamo = {
        "id_prestamo": len(prestamos) + 1,
        "id_socio": id_socio,
        "id_libro": id_libro,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d"),
        "costo": costo,
        "fecha_devolucion": None,
        "estado_prestamo": "En Curso"
    }
    prestamos.append(nuevo_prestamo)
    libro_disponible["cantidad_disponible"] -= 1

    guardar_datos('prestamos.json', prestamos)
    guardar_datos('libros.json', libros)

def eliminar_prestamo(id_prestamo):
    prestamos = cargar_datos('prestamos.json')
    prestamos = [prestamo for prestamo in prestamos if prestamo["id_prestamo"] != id_prestamo]
    guardar_datos('prestamos.json', prestamos)

def buscar_prestamos(criterio, valor):
    prestamos = cargar_datos('prestamos.json')
    return [prestamo for prestamo in prestamos if str(prestamo[criterio]).lower() == valor.lower()]

def registrar_devolucion(id_prestamo):
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

    for prestamo in prestamos:
        if prestamo["id_prestamo"] == id_prestamo:
            prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")
            prestamo["estado_prestamo"] = "Devuelto"
            for libro in libros:
                if libro["id_libro"] == prestamo["id_libro"]:
                    libro["cantidad_disponible"] += 1
                    break
            break

    guardar_datos('prestamos.json', prestamos)
    guardar_datos('libros.json', libros)

def generar_reporte_libros():
    libros = cargar_datos('libros.json')
    reporte = "Reporte de Libros:\n\n"
    for libro in libros:
        reporte += f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['anio_publicacion']}, Género: {libro['genero']}, Cantidad Disponible: {libro['cantidad_disponible']}\n"
    return reporte

def generar_reporte_socios():
    socios = cargar_datos('socios.json')
    reporte = "Reporte de Socios:\n\n"
    for socio in socios:
        reporte += f"ID: {socio['id_socio']}, Nombre: {socio['nombre']} {socio['apellido']}, Fecha de Nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Correo: {socio['correo_electronico']}, Teléfono: {socio['telefono']}\n"
    return reporte

def generar_reporte_prestamos():
    prestamos = cargar_datos('prestamos.json')
    reporte = "Reporte de Préstamos:\n\n"
    for prestamo in prestamos:
        reporte += f"ID: {prestamo['id_prestamo']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Costo: {prestamo['costo']}, Fecha de Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado_prestamo']}\n"
    return reporte
