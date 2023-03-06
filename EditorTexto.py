import time
import tkinter as tk
from tkinter import ttk, Menu
from tkinter.filedialog import askopenfile, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RainelDev - Editor de Texto")
        #Tamaño mínimo de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo campo texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo para saber si ya se abrió un archivo anteriormente
        self.archivo_abierto = False

        # Crear componenetes
        self._crearComponentes()
        self._crearMenu()

        self.mainloop()

    def _abrirArchivo(self):
        self.archivo_abierto = askopenfile(mode="r+", filetypes=[('Archivos de Texto (.txt)', '*.txt'), ('Todos los Archivos', '*.*')])

        # Eliminamos el texto anterior
        self.campo_texto.delete(1.0, tk.END)

        # Revisamos si hay un archivo
        if not self.archivo_abierto:
            return

        # Abrimos el archivo en modo lectura/escritura
        with open(self.archivo_abierto.name, "r+") as self.archivo:
            # Leemos el contenido
            texto = self.archivo.read()
            if texto:
                # Insertar en el campo texto el contenido
                self.campo_texto.insert(1.0, texto)

            self.title(f'*Archivo - {self.archivo.name}')

    def _guardarArchivo(self):
        if self.archivo_abierto:
            # Salvamos el archivo (lo abrimos en modo escritura)
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                self.archivo.write(self.campo_texto.get(1.0, tk.END))

            self.title(f'Archivo guardado - {self.archivo.name}')
        else:
            self._guardarComoArchivo()

    def _guardarComoArchivo(self):
        self.archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de Texto (.txt)', '*.txt'), ('Todos los Archivos', '*.*')]
        )

        if not self.archivo:
            return

        print(self.archivo)

        # Abrimos el archivo en modo escritura (write)
        with open(self.archivo, 'w') as archivo:
            archivo.write(self.campo_texto.get('1.0', tk.END))

            # cambiamos el nombre del archivo
            self.title(f'Archivo guardado - {self.archivo}')

            self.archivo_abierto = archivo
            print(archivo)

    def _crearMenu(self):
        menu = Menu(self)
        self.config(menu=menu)
        submenu = Menu(menu, tearoff=False)
        submenu.add_command(label='Abrir', command=self._abrirArchivo)
        submenu.add_command(label='Guardar', command=self._guardarArchivo)
        submenu.add_command(label='Guardar como...', command=self._guardarComoArchivo)
        submenu.add_separator()
        submenu.add_command(label='Salir', command=lambda: quit())

        menu.add_cascade(menu=submenu, label='Archivo')

    def _crearComponentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = ttk.Button(frame_botones, text="Abrir", command=self._abrirArchivo)
        boton_guardar = ttk.Button(frame_botones, text="Guardar", command=self._guardarArchivo)
        boton_guardar_como = ttk.Button(frame_botones, text="Guardar como...", command=self._guardarComoArchivo)

        # Expandir botones con sticky
        boton_abrir.grid(row=0, column=0, sticky="we", padx=5, pady=5, ipady=5, ipadx=5)
        boton_guardar.grid(row=1, column=0, sticky="we", padx=5, pady=5, ipady=5, ipadx=5)
        boton_guardar_como.grid(row=2, column=0, sticky="we", padx=5, pady=5, ipady=5, ipadx=5)

        # Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')

        # Colocar el campo de texto
        self.campo_texto.grid(row=0, column=1, sticky='nswe', ipadx=10)

if __name__ == '__main__':
    editor = Editor()