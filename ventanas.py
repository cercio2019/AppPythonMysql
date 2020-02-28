from tkinter import ttk
from tkinter import *

from conexion import Conexion

class Ventana:
    
    conex = Conexion()
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Registro personal de la empresas')
        
        frame = LabelFrame(self.wind, text='Registrar a un nuevo empleado')
        frame.grid(row=0, column=0, columnspan=50, pady=20)

        self.ID = Label(frame, text='')
        self.ID.grid(row= 1, column=0)
        Label(frame, text = 'Nombre completo').grid(row= 2, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 2, column = 1)

        Label(frame, text = 'Correo electronico').grid(row= 3, column = 0)
        self.email = Entry(frame)
        self.email.focus()
        self.email.grid(row = 3, column = 1)

        Label(frame, text = 'Telefono').grid(row= 4, column = 0)
        self.telefono = Entry(frame)
        self.telefono.focus()
        self.telefono.grid(row = 4, column = 1)

        self.btn_funcion = ttk.Button(frame, text='Registrar', state=NORMAL, command=self.registrar)
        self.btn_funcion.grid(row = 5, columnspan=2, sticky= W +E)

        self.btn_editar = ttk.Button(frame, text='Editar Persona', state=DISABLED, command=self.editar)
        self.btn_editar.grid(row=6, columnspan=2, sticky= W+E)

        self.btn_limpiar = ttk.Button(frame, text='Limpiar', command=self.limpiar_formulario)
        self.btn_limpiar.grid(row=7, columnspan=2, sticky= W+E)

        self.message= Label(text = '', fg='green')
        self.message.grid(row= 2, column = 0, columnspan = 2, sticky = W + E)

        self.tabla = ttk.Treeview(height=10, column = 3)
        self.tabla.grid(row=3, column= 0, columnspan= 3)
        self.tabla.heading('#0', text='Nombre' )
        self.tabla.heading('#1', text='Email' )
        #self.tabla.heading('#2', text='Telefono')

        ttk.Button(text='Buscar', command=self.buscarEmpleado).grid(row=4, column=0, sticky= W+E)
        ttk.Button(text='Eliminar', command=self.eliminar).grid(row=4, column=2, sticky= W+E)

        self.Empleados()

    def Empleados(self):
        records = self.tabla.get_children()
        for elements in records:
            self.tabla.delete(elements)
        empleados = self.conex.All_user()
        for i in empleados:
            self.tabla.insert('', 0, text=i[1], values=i[2])

    def validacion(self):
        return len(self.name.get()) !=0 and len(self.email.get()) != 0 and len(self.telefono.get()) !=0

    def limpiar_formulario(self):
        self.ID['text'] = ''
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.telefono.delete(0, END)
        self.btn_funcion.config(state=ACTIVE)
        self.btn_editar.config(state=DISABLED)

    def registrar(self):
        if self.validacion():
            user = []
            user.append(self.name.get())
            user.append(self.email.get())
            user.append(self.telefono.get())
            result = self.conex.regis_User(user)
            if result == True:
                self.message.config(fg='green')
                self.message['text'] = self.name.get()+' se ha registrado en la base de datos exitosamente'
            self.Empleados()
            self.limpiar_formulario()
        else:
            self.message.config(fg='red')
            self.message['text'] = 'Porfavor llenar todo los campos del formulario'

    def eliminar(self):
        self.message['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.message.config(fg='red')
            self.message['text'] = 'Seleccionar el empleado que desea eliminar'
            return
        self.message['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        result = self.conex.delete_user(nombre)
        if result == True:
            self.message.config(fg='green')
            self.message['text']= nombre+' ha sido borrado del sistema'
        self.Empleados()

    def buscarEmpleado(self):
        self.message['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.message.config(fg='red')
            self.message['text'] = 'Seleccionar el empleado que desea editar'
            return
        self.message['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        result = self.conex.mostrarRegistro(nombre)
        num:str = str(result[0])
        self.name['textvariable'] = StringVar(value= result[1])
        self.email['textvariable'] = StringVar(value= result[2])
        self.telefono['textvariable'] = StringVar(value= result[3])
        self.ID['text'] = num
        self.btn_funcion.config(state=DISABLED)
        self.btn_editar.config(state=ACTIVE)

    def editar(self):
        if self.validacion():
            edit_user= []
            numId:int = int(self.ID['text'])           
            edit_user.append(numId)
            edit_user.append(self.name.get())
            edit_user.append(self.email.get())
            edit_user.append(self.telefono.get())
            result = self.conex.update_user(edit_user)
            if result == True:
                self.message.config(fg='green')
                self.message['text']= 'Se han actualizado los datos del empleado'
            self.Empleados()
            self.limpiar_formulario()
            self.btn_funcion.config(state=ACTIVE)
            self.btn_editar.config(state=DISABLED)
        else:
            self.message.config(fg='red')
            self.message['text']='porfavor llenar todo los campos'

    
if __name__ == '__main__':
    window = Tk()
    application = Ventana(window)
    window = mainloop()