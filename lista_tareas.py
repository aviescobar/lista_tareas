class Tarea:
   def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"
def lista_tareas():
   
      
  
