import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
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
        self.state("zoomed")
        self.configure(background="#f0f0f0")

        # Cambiar el tema de ttk para permitir personalizaciones
        self.style = ttk.Style(self)
        self.style.theme_use("clam")  # Usar el tema "clam" que permite personalizaciones

        # Configurar el estilo de los botones
        self.style.configure("TButton", 
                            foreground="white",  # Color del texto
                            background="black",  # Color de fondo del botón (verde)
                            font=("Arial", 10), 
                            padding=10,
                            borderwidth=0,  # Sin borde
                            focusthickness=3,  # Grosor del foco
                            focuscolor="#4CAF50"  # Color del foco
                            )
        self.style.map("TButton",
                       background=[("active", "#45a049")],  # Color cuando el botón está activo (verde más oscuro)
                       relief=[("pressed", "sunken"), ("!pressed", "raised")]  # Efecto de relieve
                       )

        # Cargar imágenes (asegúrate de que las imágenes tengan fondo transparente)
        self.imagen_libro = self.cargar_imagen("Archivos Python/imagen_libro.png", (32, 32))
        self.imagen_socio = self.cargar_imagen("Archivos Python/imagen_socio.png", (32, 32))
        self.imagen_prestamo = self.cargar_imagen("Archivos Python/imagen_prestamo.png", (32, 32))

        # Configurar el sistema de grid para centrar los botones
        self.grid_columnconfigure(0, weight=1)  # Columna 0 se expande
        self.grid_columnconfigure(1, weight=1)  # Columna 1 se expande
        self.grid_columnconfigure(2, weight=1)  # Columna 2 se expande
        self.grid_rowconfigure(0, weight=1)     # Fila 0 se expande
        self.grid_rowconfigure(1, weight=1)     # Fila 1 se expande
        self.grid_rowconfigure(2, weight=1)     # Fila 2 se expande
        self.grid_rowconfigure(3, weight=1)     # Fila 3 se expande

        # Botones organizados en una cuadrícula con imágenes
        ttk.Button(self, text="Agregar Libro", image=self.imagen_libro, compound=tk.LEFT, command=self.agregar_libro_ui).grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Agregar Socio", image=self.imagen_socio, compound=tk.LEFT, command=self.agregar_socio_ui).grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Agregar Préstamo", image=self.imagen_prestamo, compound=tk.LEFT, command=self.agregar_prestamo_ui).grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Registrar Devolución", command=self.registrar_devolucion_ui).grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Eliminar Libro", command=self.eliminar_libro_ui).grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Eliminar Socio", command=self.eliminar_socio_ui).grid(row=1, column=2, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Buscar Libro", command=self.buscar_libro_ui).grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Buscar Socio", command=self.buscar_socio_ui).grid(row=2, column=1, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Buscar Préstamo", command=self.buscar_prestamo_ui).grid(row=2, column=2, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Generar Reporte de Libros", command=self.generar_reporte_libros_ui).grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Generar Reporte de Socios", command=self.generar_reporte_socios_ui).grid(row=3, column=1, padx=20, pady=20, sticky="nsew")
        ttk.Button(self, text="Generar Reporte de Préstamos", command=self.generar_reporte_prestamos_ui).grid(row=3, column=2, padx=20, pady=20, sticky="nsew")

    def cargar_imagen(self, ruta, tamaño):
        """Carga una imagen y la redimensiona."""
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(imagen)


    def crear_ventana(self, titulo, campos, callback):
        """Crea una ventana genérica para registro o búsqueda."""
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("400x300")
        ventana.grab_set()  # Hace la ventana modal

        entradas = {}
        for campo in campos:
            label = ttk.Label(ventana, text=campo)
            label.pack()
            entrada = ttk.Entry(ventana)
            entrada.pack()
            entradas[campo] = entrada

        ttk.Button(ventana, text="Guardar", command=lambda: callback(entradas)).pack()

    def agregar_libro_ui(self):
        self.crear_ventana("Registrar Libro", ["Título", "Autor", "Editorial", "Año de Publicación", "Género", "Cantidad Disponible"], self.registrar_libro_callback)

    def agregar_socio_ui(self):
        self.crear_ventana("Registrar Socio", ["Nombre", "Apellido", "Fecha de Nacimiento", "Dirección", "Correo Electrónico", "Teléfono"], self.registrar_socio_callback)

    def agregar_prestamo_ui(self):
        self.crear_ventana("Registrar Préstamo", ["ID del Socio", "ID del Libro", "Costo"], self.registrar_prestamo_callback)

    def registrar_devolucion_ui(self):
        self.crear_ventana("Registrar Devolución", ["ID del Préstamo"], self.registrar_devolucion_callback)

    def eliminar_libro_ui(self):
        self.crear_ventana_eliminacion("Eliminar Libro", self.eliminar_libro_callback)

    def eliminar_socio_ui(self):
        self.crear_ventana_eliminacion("Eliminar Socio", self.eliminar_socio_callback)

    def eliminar_prestamo_ui(self):
        self.crear_ventana_eliminacion("Eliminar Préstamo", self.eliminar_prestamo_callback)

    def crear_ventana_eliminacion(self, titulo, callback):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("300x150")
        ventana.grab_set()

        label = ttk.Label(ventana, text="ID a Eliminar")
        label.pack()
        entrada = ttk.Entry(ventana)
        entrada.pack()

        ttk.Button(ventana, text="Eliminar", command=lambda: callback(entrada.get())).pack()

    def buscar_libro_ui(self):
        self.crear_ventana_busqueda("Buscar Libro", ["Título", "Autor", "Editorial", "Año de Publicación", "Género"], self.buscar_libro_callback)

    def buscar_socio_ui(self):
        self.crear_ventana_busqueda("Buscar Socio", ["Nombre", "Apellido", "Fecha de Nacimiento", "Dirección", "Correo Electrónico", "Teléfono"], self.buscar_socio_callback)

    def buscar_prestamo_ui(self):
        self.crear_ventana_busqueda("Buscar Préstamo", ["ID del Socio", "ID del Libro", "Fecha de Préstamo", "Estado del Préstamo"], self.buscar_prestamo_callback)

    def crear_ventana_busqueda(self, titulo, criterios, callback):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry("400x300")
        ventana.grab_set()

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
        try:
            cantidad = int(entradas["Cantidad Disponible"].get())
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            registrar_libro(
                entradas["Título"].get(),
                entradas["Autor"].get(),
                entradas["Editorial"].get(),
                entradas["Año de Publicación"].get(),
                entradas["Género"].get(),
                cantidad
            )
            messagebox.showinfo("Información", "Libro registrado con éxito")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el libro: {e}")

    def registrar_socio_callback(self, entradas):
        try:
            registrar_socio(
                entradas["Nombre"].get(),
                entradas["Apellido"].get(),
                entradas["Fecha de Nacimiento"].get(),
                entradas["Dirección"].get(),
                entradas["Correo Electrónico"].get(),
                entradas["Teléfono"].get()
            )
            messagebox.showinfo("Información", "Socio registrado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el socio: {e}")

    def registrar_prestamo_callback(self, entradas):
        try:
            registrar_prestamo(
                int(entradas["ID del Socio"].get()),
                int(entradas["ID del Libro"].get()),
                float(entradas["Costo"].get())
            )
            messagebox.showinfo("Información", "Préstamo registrado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el préstamo: {e}")

    def registrar_devolucion_callback(self, entradas):
        try:
            registrar_devolucion(int(entradas["ID del Préstamo"].get()))
            messagebox.showinfo("Información", "Devolución registrada con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la devolución: {e}")

    def eliminar_libro_callback(self, id_libro):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este libro?"):
            try:
                eliminar_libro(int(id_libro))
                messagebox.showinfo("Información", "Libro eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el libro: {e}")

    def eliminar_socio_callback(self, id_socio):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este socio?"):
            try:
                eliminar_socio(int(id_socio))
                messagebox.showinfo("Información", "Socio eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el socio: {e}")

    def eliminar_prestamo_callback(self, id_prestamo):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este préstamo?"):
            try:
                eliminar_prestamo(int(id_prestamo))
                messagebox.showinfo("Información", "Préstamo eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el préstamo: {e}")

    def buscar_libro_callback(self, criterio, valor):
        try:
            libros = buscar_libros(criterio, valor)
            reporte = "\n".join([f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['anio_publicacion']}, Género: {libro['genero']}, Cantidad Disponible: {libro['cantidad_disponible']}" for libro in libros])
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el libro: {e}")

    def buscar_socio_callback(self, criterio, valor):
        try:
            socios = buscar_socios(criterio, valor)
            reporte = "\n".join([f"ID: {socio['id_socio']}, Nombre: {socio['nombre']} {socio['apellido']}, Fecha de Nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Correo: {socio['correo_electronico']}, Teléfono: {socio['telefono']}" for socio in socios])
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el socio: {e}")

    def buscar_prestamo_callback(self, criterio, valor):
        try:
            prestamos = buscar_prestamos(criterio, valor)
            reporte = "\n".join([f"ID: {prestamo['id_prestamo']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Costo: {prestamo['costo']}, Fecha de Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado_prestamo']}" for prestamo in prestamos])
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el préstamo: {e}")

    def generar_reporte_libros_ui(self):
        try:
            reporte = generar_reporte_libros()
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte de libros: {e}")

    def generar_reporte_socios_ui(self):
        try:
            reporte = generar_reporte_socios()
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte de socios: {e}")

    def generar_reporte_prestamos_ui(self):
        try:
            reporte = generar_reporte_prestamos()
            self.mostrar_reporte(reporte)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte de préstamos: {e}")
