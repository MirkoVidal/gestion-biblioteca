import tkinter as tk
from tkinter import messagebox, ttk
from operaciones import (
    registrar_libro, eliminar_libro, buscar_libros,
    registrar_socio, eliminar_socio, buscar_socios,
    registrar_prestamo, eliminar_prestamo, buscar_prestamos, registrar_devolucion,
    generar_reporte_libros, generar_reporte_socios, generar_reporte_prestamos
)

class BibliotecaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Biblioteca")
        self.geometry("400x400")
        self.configure(background="black")

        ttk.Button(self, text="Agregar Libro", command=self.agregar_libro_ui).pack()
        ttk.Button(self, text="Agregar Socio", command=self.agregar_socio_ui).pack()
        ttk.Button(self, text="Agregar Préstamo", command=self.agregar_prestamo_ui).pack()
        ttk.Button(self, text="Registrar Devolución", command=self.registrar_devolucion_ui).pack()
        ttk.Button(self, text="Eliminar Libro", command=self.eliminar_libro_ui).pack()
        ttk.Button(self, text="Eliminar Socio", command=self.eliminar_socio_ui).pack()
        ttk.Button(self, text="Eliminar Préstamo", command=self.eliminar_prestamo_ui).pack()
        ttk.Button(self, text="Buscar Libro", command=self.buscar_libro_ui).pack()
        ttk.Button(self, text="Buscar Socio", command=self.buscar_socio_ui).pack()
        ttk.Button(self, text="Buscar Préstamo", command=self.buscar_prestamo_ui).pack()
        ttk.Button(self, text="Generar Reporte de Libros", command=self.generar_reporte_libros_ui).pack()
        ttk.Button(self, text="Generar Reporte de Socios", command=self.generar_reporte_socios_ui).pack()
        ttk.Button(self, text="Generar Reporte de Préstamos", command=self.generar_reporte_prestamos_ui).pack()

    def agregar_libro_ui(self):
        self.crear_ventana_registro("Registrar Libro", self.registrar_libro_callback)

    def agregar_socio_ui(self):
        self.crear_ventana_registro("Registrar Socio", self.registrar_socio_callback)

    def agregar_prestamo_ui(self):
        self.crear_ventana_registro("Registrar Préstamo", self.registrar_prestamo_callback)

    def registrar_devolucion_ui(self):
        self.crear_ventana_registro("Registrar Devolución", self.registrar_devolucion_callback)

    def eliminar_libro_ui(self):
        self.crear_ventana_eliminacion("Eliminar Libro", self.eliminar_libro_callback)

    def eliminar_socio_ui(self):
        self.crear_ventana_eliminacion("Eliminar Socio", self.eliminar_socio_callback)

    def eliminar_prestamo_ui(self):
        self.crear_ventana_eliminacion("Eliminar Préstamo", self.eliminar_prestamo_callback)

    def buscar_libro_ui(self):
        self.crear_ventana_busqueda("Buscar Libro", ["titulo", "autor", "editorial", "anio_publicacion", "genero"], self.buscar_libro_callback)

    def buscar_socio_ui(self):
        self.crear_ventana_busqueda("Buscar Socio", ["nombre", "apellido", "fecha_nacimiento", "direccion", "correo_electronico", "telefono"], self.buscar_socio_callback)

    def buscar_prestamo_ui(self):
        self.crear_ventana_busqueda("Buscar Préstamo", ["id_socio", "id_libro", "fecha_prestamo", "estado_prestamo"], self.buscar_prestamo_callback)

    def generar_reporte_libros_ui(self):
        reporte = generar_reporte_libros()
        self.mostrar_reporte(reporte)

    def generar_reporte_socios_ui(self):
        reporte = generar_reporte_socios()
        self.mostrar_reporte(reporte)

    def generar_reporte_prestamos_ui(self):
        reporte = generar_reporte_prestamos()
        self.mostrar_reporte(reporte)

    def crear_ventana_registro(self, titulo, callback):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("400x400")

        if titulo == "Registrar Libro":
            campos = ["Título", "Autor", "Editorial", "Año de Publicación", "Género", "Cantidad Disponible"]
        elif titulo == "Registrar Socio":
            campos = ["Nombre", "Apellido", "Fecha de Nacimiento", "Dirección", "Correo Electrónico", "Teléfono"]
        elif titulo == "Registrar Préstamo":
            campos = ["ID del Socio", "ID del Libro", "Costo"]
        elif titulo == "Registrar Devolución":
            campos = ["ID del Préstamo"]

        entradas = {}
        for campo in campos:
            label = ttk.Label(ventana, text=campo)
            label.pack()
            entrada = ttk.Entry(ventana)
            entrada.pack()
            entradas[campo] = entrada

        ttk.Button(ventana, text="Guardar", command=lambda: callback(entradas)).pack()

    def crear_ventana_eliminacion(self, titulo, callback):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("300x200")

        label = ttk.Label(ventana, text="ID a Eliminar")
        label.pack()
        entrada = ttk.Entry(ventana)
        entrada.pack()

        ttk.Button(ventana, text="Eliminar", command=lambda: callback(entrada.get())).pack()

    def crear_ventana_busqueda(self, titulo, criterios, callback):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("400x400")

        label_criterio = ttk.Label(ventana, text="Criterio")
        label_criterio.pack()
        combo_criterio = ttk.Combobox(ventana, values=criterios)
        combo_criterio.pack()

        label_valor = ttk.Label(ventana, text="Valor")
        label_valor.pack()
        entrada_valor = ttk.Entry(ventana)
        entrada_valor.pack()

        ttk.Button(ventana, text="Buscar", command=lambda: callback(combo_criterio.get(), entrada_valor.get())).pack()

    def mostrar_reporte(self, reporte):
        ventana = tk.Toplevel(self)
        ventana.title("Reporte")
        ventana.geometry("500x500")

        texto_reporte = tk.Text(ventana, wrap="word")
        texto_reporte.insert("1.0", reporte)
        texto_reporte.pack(expand=True, fill="both")

    def registrar_libro_callback(self, entradas):
        registrar_libro(
            entradas["Título"].get(),
            entradas["Autor"].get(),
            entradas["Editorial"].get(),
            entradas["Año de Publicación"].get(),
            entradas["Género"].get(),
            int(entradas["Cantidad Disponible"].get())
        )
        messagebox.showinfo("Información", "Libro registrado con éxito")

    def registrar_socio_callback(self, entradas):
        registrar_socio(
            entradas["Nombre"].get(),
            entradas["Apellido"].get(),
            entradas["Fecha de Nacimiento"].get(),
            entradas["Dirección"].get(),
            entradas["Correo Electrónico"].get(),
            entradas["Teléfono"].get()
        )
        messagebox.showinfo("Información", "Socio registrado con éxito")

    def registrar_prestamo_callback(self, entradas):
        registrar_prestamo(
            int(entradas["ID del Socio"].get()),
            int(entradas["ID del Libro"].get()),
            float(entradas["Costo"].get())
        )
        messagebox.showinfo("Información", "Préstamo registrado con éxito")

    def registrar_devolucion_callback(self, entradas):
        registrar_devolucion(int(entradas["ID del Préstamo"].get()))
        messagebox.showinfo("Información", "Devolución registrada con éxito")

    def eliminar_libro_callback(self, id_libro):
        eliminar_libro(int(id_libro))
        messagebox.showinfo("Información", "Libro eliminado con éxito")

    def eliminar_socio_callback(self, id_socio):
        eliminar_socio(int(id_socio))
        messagebox.showinfo("Información", "Socio eliminado con éxito")

    def eliminar_prestamo_callback(self, id_prestamo):
        eliminar_prestamo(int(id_prestamo))
        messagebox.showinfo("Información", "Préstamo eliminado con éxito")

    def buscar_libro_callback(self, criterio, valor):
        libros = buscar_libros(criterio, valor)
        reporte = "\n".join([f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['anio_publicacion']}, Género: {libro['genero']}, Cantidad Disponible: {libro['cantidad_disponible']}" for libro in libros])
        self.mostrar_reporte(reporte)

    def buscar_socio_callback(self, criterio, valor):
        socios = buscar_socios(criterio, valor)
        reporte = "\n".join([f"ID: {socio['id_socio']}, Nombre: {socio['nombre']} {socio['apellido']}, Fecha de Nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Correo: {socio['correo_electronico']}, Teléfono: {socio['telefono']}" for socio in socios])
        self.mostrar_reporte(reporte)

    def buscar_prestamo_callback(self, criterio, valor):
        prestamos = buscar_prestamos(criterio, valor)
        reporte = "\n".join([f"ID: {prestamo['id_prestamo']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Costo: {prestamo['costo']}, Fecha de Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado_prestamo']}" for prestamo in prestamos])
        self.mostrar_reporte(reporte)
