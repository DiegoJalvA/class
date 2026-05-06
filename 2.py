# CLASE PADRE
class Persona:
    def __init__(self, nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, estado_civil):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.cedula = cedula
        self.celular = celular
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.estado_civil = estado_civil

#METODOS 
    def mostrar_datos_personales(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def mostrar_informacion_contacto(self):
        print(f"Cedula: {self.cedula}")
        print(f"Celular: {self.celular}")

    def mostrar_caracteristicas(self):
        print(f"Genero: {self.genero}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")
        print(f"Estado Civil: {self.estado_civil}")

#POLIMORFISMO

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")

#CLASE ESTUDIANTE

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, estado_civil,
                 correo_institucional, semestre, carrera, facultad, sede_universitaria):
        super().__init__(nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, estado_civil)  

        self.correo_institucional = correo_institucional
        self.semestre = semestre    
        self.carrera = carrera
        self.facultad = facultad    
        self.sede_universitaria = sede_universitaria

#METODOS

    def mostrar_informacion_estudiante(self):
        print(f"Correo: {self.correo_institucional}")
        print(f"Semestre: {self.semestre}")

    def mostrar_informacion_academica(self):
        print(f"Carrera: {self.carrera}")
        print(f"Facultad: {self.facultad}")
        print(f"Sede: {self.sede_universitaria}")

    def mostrar_ubicacion_estudiante(self):
        print(f"Ubicacion: {self.sede_universitaria}")
        print(f"Facultad: {self.facultad}") 

#POLIMORFISMO

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, tengo {self.edad} años y estudio {self.carrera}.")

#CLASE PROFESOR 

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, estado_civil,
                 titulo, años_experiencia, materia_academica, jornada, departamento):
        super().__init__(nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, estado_civil)

        self.titulo = titulo
        self.años_experiencia = años_experiencia
        self.materia_academica = materia_academica
        self.jornada = jornada   
        self.departamento = departamento

#   METODOS 

    def mostrar_datos_profesor(self):
        print(f"Titulo: {self.titulo}")
        print(f"Experiencia: {self.años_experiencia} años")

    def mostrar_informacion_laboral(self):
        print(f"Materia: {self.materia_academica}")
        print(f"Jornada: {self.jornada}")
        print(f"Departamento: {self.departamento}") 

    def mostrar_experiencia_profesional(self):
        print(f"Docente de: {self.materia_academica}")
        print(f"Años experiencia: {self.años_experiencia}")

#POLIMORFISMO        

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, tengo {self.edad} años y soy profesor de {self.materia_academica}.")


#FUNCIONES PARA MOSTRAR INFORMACION

def mostrar_informacion_est(est):
    print("ESTUDIANTE:")
    est.mostrar_datos_personales()
    est.mostrar_informacion_contacto()
    est.mostrar_caracteristicas()
    est.mostrar_informacion_estudiante()    
    est.mostrar_informacion_academica()
    est.mostrar_ubicacion_estudiante()
    print()

def mostrar_informacion_pro(prof):
    print("PROFESOR:")
    prof.mostrar_datos_personales()
    prof.mostrar_informacion_contacto()
    prof.mostrar_caracteristicas()
    prof.mostrar_datos_profesor()    
    prof.mostrar_informacion_laboral()
    prof.mostrar_experiencia_profesional()
    print()

#POLIMORFISMO

def presentar_persona(persona):
    persona.presentarse()

#OBJETOS 

estudiante1 = Estudiante("Diego", "Alvarado", 20, "Ecuatoriano", "123456789", "3001234567", "Masculino", 1.75, 70, "Soltero",
                          "diego.alvarado@unemi.edu.com", "4 semestre", "Ingeniería en software", "Facultad de Ingeniería", "Milagro")                                              


profesor1 = Profesor("Juan", "Peres", 45, "Ecuatoriano", "987654321", "3007654321", "Masculino", 1.65, 60, "Casada", 
                     "PhD en Ciencias de la Computación", 20, "POO", "Tiempo completo", "Departamento de Informática")


mostrar_informacion_est(estudiante1)
mostrar_informacion_pro(profesor1)


#EJECUCION DE POLIMORFISMO

print("POLIMORFISMO:")
presentar_persona(estudiante1)
presentar_persona(profesor1)