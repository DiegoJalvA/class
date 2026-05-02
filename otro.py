# ==========================================================
# CLASE PADRE: PERSONA
# Esta clase contiene los datos generales que puede tener
# cualquier persona, ya sea estudiante o profesor.
# ==========================================================

class Persona:

    # Constructor de la clase Persona
    # Aquí se reciben los 10 atributos mínimos solicitados.
    def __init__(self, nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, etnia):
        
        # Atributos generales de una persona
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.cedula = cedula
        self.celular = celular
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.etnia = etnia

    # Método 1 de Persona
    # Muestra los datos personales básicos.
    def mostrar_datos_personales(self):
        print("===== DATOS PERSONALES =====")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Nacionalidad: {self.nacionalidad}")

    # Método 2 de Persona
    # Muestra la información de contacto.
    def mostrar_informacion_contacto(self):
        print("===== INFORMACIÓN DE CONTACTO =====")
        print(f"Cédula: {self.cedula}")
        print(f"Celular: {self.celular}")

    # Método 3 de Persona
    # Muestra características personales y físicas.
    def mostrar_caracteristicas(self):
        print("===== CARACTERÍSTICAS PERSONALES =====")
        print(f"Género: {self.genero}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")
        print(f"Etnia: {self.etnia}")

    # Método general para aplicar polimorfismo.
    # Este método será sobrescrito en Estudiante y Profesor.
    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")


# ==========================================================
# CLASE HIJA: ESTUDIANTE
# Hereda de la clase Persona.
# Además de los atributos de Persona, agrega 5 atributos propios.
# ==========================================================

class Estudiante(Persona):

    # Constructor de Estudiante
    def __init__(
        self,
        nombre,
        apellido,
        edad,
        nacionalidad,
        cedula,
        celular,
        genero,
        altura,
        peso,
        etnia,
        correo_institucional,
        semestre,
        carrera,
        facultad,
        sede_universitaria
    ):

        # super() llama al constructor de la clase padre Persona.
        # Así reutilizamos los 10 atributos generales.
        super().__init__(nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, etnia)

        # Atributos propios de la clase Estudiante.
        self.correo_institucional = correo_institucional
        self.semestre = semestre
        self.carrera = carrera
        self.facultad = facultad
        self.sede_universitaria = sede_universitaria

    # Método propio 1 de Estudiante
    # Muestra información básica del estudiante.
    def mostrar_informacion_estudiante(self):
        print("===== DATOS DEL ESTUDIANTE =====")
        print(f"Estudiante: {self.nombre} {self.apellido}")
        print(f"Correo institucional: {self.correo_institucional}")
        print(f"Semestre: {self.semestre}")

    # Método propio 2 de Estudiante
    # Muestra información académica.
    def mostrar_informacion_academica(self):
        print("===== INFORMACIÓN ACADÉMICA =====")
        print(f"Carrera: {self.carrera}")
        print(f"Facultad: {self.facultad}")
        print(f"Sede universitaria: {self.sede_universitaria}")

    # Método propio 3 de Estudiante
    # Muestra la ubicación universitaria del estudiante.
    def mostrar_ubicacion_estudiante(self):
        print("===== UBICACIÓN DEL ESTUDIANTE =====")
        print(f"Sede universitaria: {self.sede_universitaria}")
        print(f"Facultad: {self.facultad}")
        print(f"El estudiante {self.nombre} {self.apellido} pertenece a la sede {self.sede_universitaria}.")

    # Polimorfismo:
    # Este método tiene el mismo nombre que en Persona,
    # pero su comportamiento es diferente porque presenta a un estudiante.
    def presentarse(self):
        print(
            f"Hola, soy {self.nombre} {self.apellido}, tengo {self.edad} años "
            f"y soy estudiante de {self.carrera} en el {self.semestre}."
        )


# ==========================================================
# CLASE HIJA: PROFESOR
# Hereda de la clase Persona.
# Además de los atributos de Persona, agrega 5 atributos propios.
# ==========================================================

class Profesor(Persona):

    # Constructor de Profesor
    def __init__(
        self,
        nombre,
        apellido,
        edad,
        nacionalidad,
        cedula,
        celular,
        genero,
        altura,
        peso,
        etnia,
        titulo,
        anios_experiencia,
        materia_academica,
        jornada,
        departamento
    ):

        # super() llama al constructor de la clase Persona.
        # Así Profesor hereda los 10 atributos generales.
        super().__init__(nombre, apellido, edad, nacionalidad, cedula, celular, genero, altura, peso, etnia)

        # Atributos propios de la clase Profesor.
        self.titulo = titulo
        self.anios_experiencia = anios_experiencia
        self.materia_academica = materia_academica
        self.jornada = jornada
        self.departamento = departamento

    # Método propio 1 de Profesor
    # Muestra los datos principales del profesor.
    def mostrar_datos_profesor(self):
        print("===== DATOS DEL PROFESOR =====")
        print(f"Profesor: {self.nombre} {self.apellido}")
        print(f"Título profesional: {self.titulo}")
        print(f"Años de experiencia: {self.anios_experiencia}")

    # Método propio 2 de Profesor
    # Muestra información relacionada con su trabajo.
    def mostrar_informacion_laboral(self):
        print("===== INFORMACIÓN LABORAL =====")
        print(f"Materia académica: {self.materia_academica}")
        print(f"Jornada: {self.jornada}")
        print(f"Departamento: {self.departamento}")

    # Método propio 3 de Profesor
    # Muestra información sobre su experiencia profesional.
    def mostrar_experiencia_profesional(self):
        print("===== EXPERIENCIA PROFESIONAL =====")
        print(f"Profesor: {self.nombre} {self.apellido}")
        print(f"Años de experiencia: {self.anios_experiencia}")
        print(f"Materia que imparte: {self.materia_academica}")

    # Polimorfismo:
    # Este método tiene el mismo nombre que en Persona y Estudiante,
    # pero se comporta diferente porque presenta a un profesor.
    def presentarse(self):
        print(
            f"Hola, soy el profesor {self.nombre} {self.apellido}, tengo {self.edad} años, "
            f"soy {self.titulo} y dicto la materia de {self.materia_academica}."
        )


# ==========================================================
# FUNCIÓN PARA APLICAR POLIMORFISMO
# Esta función recibe cualquier objeto.
# Si recibe un Estudiante, se ejecuta el presentarse() de Estudiante.
# Si recibe un Profesor, se ejecuta el presentarse() de Profesor.
# ==========================================================

def presentarse(persona):
    persona.presentarse()


# ==========================================================
# CREACIÓN DE OBJETOS
# Aquí se crean los objetos estudiante1 y profesor1.
# Cada objeto recibe los datos necesarios según su clase.
# ==========================================================

estudiante1 = Estudiante(
    "Diego",
    "Alvarado",
    20,
    "Ecuatoriano",
    "0929961340",
    "0988075126",
    "Masculino",
    1.70,
    65,
    "Mestizo",
    "dalavaradoa12@unemi.edu.ec",
    "Cuarto Semestre",
    "Ingeniería en Software",
    "Facultad de Ingeniería",
    "Milagro"
)


profesor1 = Profesor(
    "Carlos",
    "Mendoza",
    40,
    "Ecuatoriano",
    "0912345678",
    "0998765432",
    "Masculino",
    1.75,
    78,
    "Mestizo",
    "Ingeniero en Sistemas",
    10,
    "Programación Orientada a Objetos",
    "Matutina",
    "Departamento de Tecnología"
)


# ==========================================================
# EJECUCIÓN DE MÉTODOS DEL ESTUDIANTE
# Aquí se llama a los métodos heredados de Persona
# y también a los métodos propios de Estudiante.
# ==========================================================

print("========== INFORMACIÓN DEL ESTUDIANTE ==========")

estudiante1.mostrar_datos_personales()
print()

estudiante1.mostrar_informacion_contacto()
print()

estudiante1.mostrar_caracteristicas()
print()

estudiante1.mostrar_informacion_estudiante()
print()

estudiante1.mostrar_informacion_academica()
print()

estudiante1.mostrar_ubicacion_estudiante()
print()


# ==========================================================
# EJECUCIÓN DE MÉTODOS DEL PROFESOR
# Aquí se llama a los métodos heredados de Persona
# y también a los métodos propios de Profesor.
# ==========================================================

print("========== INFORMACIÓN DEL PROFESOR ==========")

profesor1.mostrar_datos_personales()
print()

profesor1.mostrar_informacion_contacto()
print()

profesor1.mostrar_caracteristicas()
print()

profesor1.mostrar_datos_profesor()
print()

profesor1.mostrar_informacion_laboral()
print()

profesor1.mostrar_experiencia_profesional()
print()


# ==========================================================
# APLICACIÓN DEL POLIMORFISMO
# Se usa la misma función presentarse(),
# pero el resultado cambia según el objeto recibido.
# ==========================================================

print("========== POLIMORFISMO ==========")

presentarse(estudiante1)
presentarse(profesor1)