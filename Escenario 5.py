# =====================================================
# SISTEMA DE GESTIÓN DE PROYECTOS
# JUNTA DE DESARROLLO LOCAL DE BETANIA
#Escenario 5 - Jhonathan Rodriguez 
# =====================================================

class Usuario:

    def __init__(self, id_usuario, nombre, cargo):
        self.id = id_usuario
        self.nombre = nombre
        self.cargo = cargo

    def mostrar(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")


class Tarea:

    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.responsable = None
        self.estado = "Pendiente"
        self.avance = 0

    def asignar_responsable(self, usuario):
        self.responsable = usuario

    def registrar_avance(self, porcentaje):

        if porcentaje < 0:
            porcentaje = 0

        if porcentaje > 100:
            porcentaje = 100

        self.avance = porcentaje

        if porcentaje == 0:
            self.estado = "Pendiente"

        elif porcentaje == 100:
            self.estado = "Finalizada"

        else:
            self.estado = "En Proceso"

    def mostrar(self):

        if self.responsable:
            responsable = self.responsable.nombre
        else:
            responsable = "Sin asignar"

        print("------------------------------------")
        print("Código:", self.codigo)
        print("Descripción:", self.descripcion)
        print("Responsable:", responsable)
        print("Estado:", self.estado)
        print("Avance:", str(self.avance) + "%")


class Proyecto:

    def __init__(self, codigo, nombre, descripcion,
                 objetivo, presupuesto, cronograma):

        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivo = objetivo
        self.presupuesto = presupuesto
        self.cronograma = cronograma
        self.estado = "Activo"

        self.tareas = {}

    def agregar_tarea(self, tarea):
        self.tareas[tarea.codigo] = tarea

    def calcular_avance(self):

        if len(self.tareas) == 0:
            return 0

        suma = 0

        for tarea in self.tareas.values():
            suma += tarea.avance

        return suma / len(self.tareas)

    def mostrar(self):

        print("\n====================================")
        print("Código:", self.codigo)
        print("Proyecto:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Objetivo:", self.objetivo)
        print("Presupuesto: B/.", self.presupuesto)
        print("Cronograma:", self.cronograma)
        print("Estado:", self.estado)
        print("Avance General:",
              round(self.calcular_avance(), 2), "%")

        print("\nTAREAS")

        if len(self.tareas) == 0:
            print("No hay tareas registradas.")

        else:

            for tarea in self.tareas.values():
                tarea.mostrar()
                
class Sistema:
                    
                
    def __init__(self):

        self.usuarios = {}
        self.proyectos = {}
        self.tareas = {}

    # ==========================
    # REGISTRAR USUARIO
    # ==========================

    def registrar_usuario(self):

        print("\n--- REGISTRAR USUARIO ---")

        id_usuario = input("ID del usuario: ")

        if id_usuario in self.usuarios:
            print("Ese usuario ya existe.")
            return

        nombre = input("Nombre: ")
        cargo = input("Cargo: ")

        usuario = Usuario(id_usuario, nombre, cargo)

        self.usuarios[id_usuario] = usuario

        print("Usuario registrado correctamente.")

    # ==========================
    # CREAR PROYECTO
    # ==========================

    def crear_proyecto(self):

        print("\n--- CREAR PROYECTO ---")

        codigo = input("Código del proyecto: ")

        if codigo in self.proyectos:
            print("Ese proyecto ya existe.")
            return

        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripción: ")
        objetivo = input("Objetivo: ")

        presupuesto = float(input("Presupuesto: "))

        cronograma = input("Cronograma: ")

        proyecto = Proyecto(
            codigo,
            nombre,
            descripcion,
            objetivo,
            presupuesto,
            cronograma
        )

        self.proyectos[codigo] = proyecto

        print("Proyecto creado correctamente.")

    # ==========================
    # CREAR TAREA
    # ==========================

    def crear_tarea(self):

        print("\n--- CREAR TAREA ---")

        codigo_proyecto = input("Código del proyecto: ")

        if codigo_proyecto not in self.proyectos:
            print("Ese proyecto no existe.")
            return

        codigo = input("Código de la tarea: ")

        if codigo in self.tareas:
            print("Ese código ya existe.")
            return

        descripcion = input("Descripción: ")

        tarea = Tarea(codigo, descripcion)

        self.tareas[codigo] = tarea

        self.proyectos[codigo_proyecto].agregar_tarea(tarea)

        print("Tarea registrada correctamente.")

    # ==========================
    # ASIGNAR RESPONSABLE
    # ==========================

    def asignar_responsable(self):

        print("\n--- ASIGNAR RESPONSABLE ---")

        codigo_tarea = input("Código de la tarea: ")

        if codigo_tarea not in self.tareas:
            print("La tarea no existe.")
            return

        id_usuario = input("ID del usuario: ")

        if id_usuario not in self.usuarios:
            print("Ese usuario no existe.")
            return

        self.tareas[codigo_tarea].asignar_responsable(
            self.usuarios[id_usuario]
        )

        print("Responsable asignado correctamente.")

    # ==========================
    # REGISTRAR AVANCE
    # ==========================

    def registrar_avance(self):

        print("\n--- REGISTRAR AVANCE ---")

        codigo = input("Código de la tarea: ")

        if codigo not in self.tareas:
            print("La tarea no existe.")
            return

        avance = int(input("Porcentaje de avance (0-100): "))

        self.tareas[codigo].registrar_avance(avance)

        print("Avance actualizado correctamente.")

    # ==========================
    # VER INFORMES
    # ==========================

    def ver_informes(self):

        if len(self.proyectos) == 0:
            print("\nNo hay proyectos registrados.")
            return

        for proyecto in self.proyectos.values():
            proyecto.mostrar()

    # ==========================
    # PUBLICAR PROYECTOS
    # ==========================

    def publicar_proyectos(self):

        print("\n========= PUBLICACIÓN =========")

        if len(self.proyectos) == 0:
            print("No existen proyectos.")
            return

        for proyecto in self.proyectos.values():

            print("\n----------------------------")
            print("Proyecto:", proyecto.nombre)
            print("Objetivo:", proyecto.objetivo)
            print("Estado:", proyecto.estado)
            print("Avance:",
                  round(proyecto.calcular_avance(), 2), "%")
            
            # ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def menu():

    sistema = Sistema()

    while True:

        print("\n" + "=" * 45)
        print(" SISTEMA DE GESTIÓN DE PROYECTOS JDL ")
        print("=" * 45)
        print("1. Registrar usuario")
        print("2. Crear proyecto")
        print("3. Crear tarea")
        print("4. Asignar responsable")
        print("5. Registrar avance")
        print("6. Ver informes")
        print("7. Publicar proyectos")
        print("8. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_usuario()

        elif opcion == "2":
            sistema.crear_proyecto()

        elif opcion == "3":
            sistema.crear_tarea()

        elif opcion == "4":
            sistema.asignar_responsable()

        elif opcion == "5":
            sistema.registrar_avance()

        elif opcion == "6":
            sistema.ver_informes()

        elif opcion == "7":
            sistema.publicar_proyectos()

        elif opcion == "8":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
