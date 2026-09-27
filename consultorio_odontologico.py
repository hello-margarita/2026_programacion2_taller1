# Universidad de Manizales
# Materia: Programación II
# Taller No. 1: Estructuras de datos - Arreglos y Listas
# Profesor: Ing. Jose Ubaldo Carvajal
# Elaborado por: Margarita María Arango Vélez
# Fecha: 26/09/2026


from datetime import date

#Clase Cliente que representa a un cliente del consultorio odontológico, con sus datos básicos de registro.
class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.valor_total = 0  # El valor total por cliente se calcula más adelante con la función de precios.

    def __repr__(self):
        return (
            f"Cliente(cedula={self.cedula}, nombre={self.nombre}, "
            f"telefono={self.telefono}, tipo_cliente={self.tipo_cliente}, "
            f"tipo_atencion={self.tipo_atencion}, cantidad={self.cantidad}, "
            f"prioridad={self.prioridad}, fecha_cita={self.fecha_cita}, "
            f"valor_total={self.valor_total})"
        )
    
# El programa le pide al usuario ingresar la cédula por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
def validar_cedula():
    while True:
        cedula = input("Ingrese la cédula del cliente (solo números, sin puntos): ")

        if cedula.isdigit() and cedula[0] != "0" and 7 <= len(cedula) <= 10:
            return cedula

        print()
        print("Dato inválido. La cédula debe contener solo números, tener entre 7 y 10 dígitos, y no puede empezar en 0. Por favor ingrese nuevamente el número de cédula del cliente.")

# Se pide ingresar el nombre del cliente por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre completo del cliente (nombres y apellidos): ")
        nombre_sin_espacios = nombre.replace(" ", "")

        if nombre_sin_espacios != "" and nombre_sin_espacios.isalpha():
            return nombre

        print()
        print("Dato inválido. El nombre debe contener solo letras y espacios, sin números ni símbolos. Por favor ingrese nuevamente el nombre del cliente.")

# Se pide ingresar el número telefónico de contacto por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
# Este dato se guarda como texto para no perder un posible 0 inicial en prefijos internacionales o por si cambian los indicativos locales.
def validar_telefono():
    while True:
        telefono = input("Ingrese el teléfono de contacto del cliente: ")

        if telefono.isdigit() and 7 <= len(telefono) <= 15:
            return telefono

        print()
        print("Dato inválido. El teléfono debe contener solo números, entre 7 y 15 dígitos. Por favor ingrese nuevamente el teléfono de contacto del cliente.")

# Muestra un menú para que el usuario seleccione el tipo de cliente y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_tipo_cliente():
    while True:
        print("Seleccione el tipo de cliente:")
        print("1. Particular")
        print("2. EPS")
        print("3. Prepagada")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2" or opcion == "3":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 3.")

# Muestra el menú con los tipos de atención disponibles y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_tipo_atencion():
    while True:
        print("Seleccione el tipo de atención:")
        print("1. Limpieza")
        print("2. Calzas")
        print("3. Extracción")
        print("4. Diagnóstico")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 4.")

# Se pide ingresar la cantidad del tipo de servicio ingresado por teclado, aplicando las reglas indicadas para cada tipo de atención.
def validar_cantidad(tipo_atencion):
    while True:
        if tipo_atencion == "1":
            cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Limpieza es 1): ")
        else:
            if tipo_atencion == "4":
                cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Diagnóstico es 1): ")
            else:
                cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Calzas y Extracción es 32): ") # Se limita la cantidad a un máximo de 32 ya que es el número máximo de dientes que puede tener un cliente.

        if cantidad_texto.isdigit() and cantidad_texto[0] != "0":
            cantidad = int(cantidad_texto)

            if tipo_atencion == "1" or tipo_atencion == "4":
                if cantidad == 1:
                    return cantidad

            if tipo_atencion == "2" or tipo_atencion == "3":
                if cantidad >= 1 and cantidad <= 32:
                    return cantidad

        print()
        print("El dato ingresado no es válido. Verifique la cantidad según el tipo de atención seleccionado. Por favor ingrese nuevamente la cantidad.")

# Muestra un menú para asignar el nivel de prioridad del cliente y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_prioridad():
    while True:
        print("Seleccione la prioridad de atención para el cliente ingresado:")
        print("1. Normal")
        print("2. Urgente")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 2.")

# Para validar la fecha ingresada para la cita, debemos determinar si el año ingresado es bisiesto (determinar si febrero tiene 28 o 29 días).
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Devuelve la cantidad de días que tiene un mes específico, considerando el año (para febrero).
def dias_en_mes(mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28

    return 0

# Se le pide al usuario que ingrese la fecha asignada para la cita por teclado y el ciclo se repite hasta que la fecha ingresada sea válida.
def validar_fecha():
    while True:
        fecha_texto = input("Ingrese la fecha asignada para la cita (formato DD/MM/AAAA): ")
        partes = fecha_texto.split("/")

        if len(partes) == 3:
            dia_texto = partes[0]
            mes_texto = partes[1]
            anio_texto = partes[2]

            if dia_texto.isdigit() and mes_texto.isdigit() and anio_texto.isdigit():
                dia = int(dia_texto)
                mes = int(mes_texto)
                anio = int(anio_texto)

                if mes >= 1 and mes <= 12:
                    if dia >= 1 and dia <= dias_en_mes(mes, anio):
                        fecha_ingresada = date(anio, mes, dia)
                        fecha_hoy = date.today()

                        # Para este punto tuve que buscar documentación en línea. Encontré que Python permite comparar fechas directamente con >= para saber si es hoy o una fecha futura. Esto con el fin de evitar que el usuario ingrese una fecha anterior a la fecha actual.
                        # Nota: Soy consciente de que esta validación permite fechas muy lejanas en el futuro (por ejemplo, años 2500 en adelante).
                        # Decidí no agregar un límite superior porque implicaría incluir una funcionalidad adicional no solicitada en el enunciado del taller.

                        if fecha_ingresada >= fecha_hoy:
                            return fecha_texto

        print()
        print("La fecha ingresada no es válida. Debe tener el formato DD/MM/AAAA, ser una fecha real, y no puede ser anterior al día de hoy. Por favor ingrese nuevamente la fecha asignada para la cita.")

# se crea la función que calcula el valor total a pagar por el cliente según el tipo de cliente, tipo de atención y cantidad.
def calcular_valor_total(tipo_cliente, tipo_atencion, cantidad):
    if tipo_cliente == "1":  # Particular
        valor_cita = 80000

        if tipo_atencion == "1":  # Limpieza
            valor_atencion = 60000
        else:
            if tipo_atencion == "2":  # Calzas
                valor_atencion = 80000
            else:
                if tipo_atencion == "3":  # Extracción
                    valor_atencion = 100000
                else:
                    valor_atencion = 50000  # Diagnóstico

    else:
        if tipo_cliente == "2":  # EPS
            valor_cita = 5000

            if tipo_atencion == "1":  # Limpieza
                valor_atencion = 0
            else:
                if tipo_atencion == "2":  # Calzas
                    valor_atencion = 40000
                else:
                    if tipo_atencion == "3":  # Extracción
                        valor_atencion = 40000
                    else:
                        valor_atencion = 0  # Diagnóstico

        else:  # Prepagada
            valor_cita = 30000

            if tipo_atencion == "1":  # Limpieza
                valor_atencion = 0
            else:
                if tipo_atencion == "2":  # Calzas
                    valor_atencion = 10000
                else:
                    if tipo_atencion == "3":  # Extracción
                        valor_atencion = 10000
                    else:
                        valor_atencion = 0  # Diagnóstico

    valor_total = valor_cita + (valor_atencion * cantidad)
    return valor_total

# Función que cuenta cuántos clientes en total hay en la lista.
def total_clientes(lista_clientes):
    return len(lista_clientes)

# Función que suma el valor total por pagar de todos los clientes registrados en la lista.
def ingresos_totales(lista_clientes):
    suma = 0

    for cliente in lista_clientes:
        suma = suma + cliente.valor_total

    return suma

# Función que cuenta cuántos clientes tienen como tipo de atención la "Extracción" de dientes.
def clientes_extraccion(lista_clientes):
    contador = 0

    for cliente in lista_clientes:
        if cliente.tipo_atencion == "3":
            contador = contador + 1

    return contador

# Investigué en internet cómo ordenar una lista de objetos según un atributo específico.
# El método sort() de Python permite usar el parámetro "key" para indicarle con qué valor comparar cada elemento; en este caso, se compara por el valor_total de cada cliente.
def obtener_valor_total(cliente):
    return cliente.valor_total

# Traduce el numero de tipo de cliente a su nombre correspondiente.
def texto_tipo_cliente(tipo_cliente):
    if tipo_cliente == "1":
        return "Particular"
    else:
        if tipo_cliente == "2":
            return "EPS"
        else:
            return "Prepagada"

# Traduce el numero de tipo de atención a su nombre correspondiente.
def texto_tipo_atencion(tipo_atencion):
    if tipo_atencion == "1":
        return "Limpieza"
    else:
        if tipo_atencion == "2":
            return "Calzas"
        else:
            if tipo_atencion == "3":
                return "Extracción"
            else:
                return "Diagnóstico"

# Traduce el número de prioridad a su nombre correspondiente.
def texto_prioridad(prioridad):
    if prioridad == "1":
        return "Normal"
    else:
        return "Urgente"

# Búsqueda de un cliente por el número de cédula registrado en la lista, recorriendola de forma lineal.
# Nota: el programa no impide registrar la misma cédula varias veces, ya que una persona puede tener agendadas varias citas (con diferente tipo de atención o fecha). 
# Por esta razón, si una cédula tiene más de un registro, la búsqueda muestra únicamente el primero que encuentra en la lista.
def buscar_cliente_por_cedula(lista_clientes, cedula_buscada):
    comparaciones = 0

    for cliente in lista_clientes:
        comparaciones = comparaciones + 1

        if cliente.cedula == cedula_buscada:
            return cliente, comparaciones

    return None, comparaciones

# Programa principal: registra los datos de cada cliente hasta que el usuario decida terminar el registro. Luego muestra la lista de clientes registrados.
if __name__ == "__main__":
    clientes = []
    contador = 1
    seguir = True

    while seguir:
        print()
        print(f"--- Registro del cliente {contador} ---")

        cedula = validar_cedula()
        nombre = validar_nombre()
        telefono = validar_telefono()
        tipo_cliente = validar_tipo_cliente()
        tipo_atencion = validar_tipo_atencion()
        cantidad = validar_cantidad(tipo_atencion)
        prioridad = validar_prioridad()
        fecha_cita = validar_fecha()

        cliente_nuevo = Cliente(cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha_cita)
        cliente_nuevo.valor_total = calcular_valor_total(tipo_cliente, tipo_atencion, cantidad)

        clientes.append(cliente_nuevo)
        contador = contador + 1

        respuesta_valida = False
        while respuesta_valida == False:
            print()
            respuesta = input("¿Desea ingresar otro cliente? (S/N): ")

            if respuesta == "S" or respuesta == "s":
                respuesta_valida = True
                continuar = "S"
            else:
                if respuesta == "N" or respuesta == "n":
                    respuesta_valida = True
                    continuar = "N"
                else:
                    print("Respuesta inválida. Por favor responda S (sí) o N (no).")

        if continuar == "N":
            seguir = False

    print()
    print("--- Registro finalizado. ---")
    print()
    print("No. total de clientes registrados:", total_clientes(clientes))
    print(f"Ingresos totales recibidos: ${ingresos_totales(clientes):,.0f} pesos mcte.")
    print("No. total de clientes agendados para extracción dental:", clientes_extraccion(clientes))

    print()
    print("--- Clientes ordenados por el valor total de la atención de mayor a menor: ---")
    print()
    clientes.sort(key=obtener_valor_total, reverse=True)

    numero = 1
    for cliente in clientes:
        print(f"{numero}. {cliente.nombre} - ${cliente.valor_total:,.0f} pesos mcte.")
        numero = numero + 1

        print()

    buscar_otro = True
    while buscar_otro:
        print()
        cedula_buscar = input("Ingrese la cédula del cliente que desea buscar: ")
        cliente_encontrado, comparaciones = buscar_cliente_por_cedula(clientes, cedula_buscar)

        if cliente_encontrado != None:
            print()
            print("--- Cliente encontrado ---")
            print()
            print(f"Cédula: {cliente_encontrado.cedula}")
            print(f"Nombre: {cliente_encontrado.nombre}")
            print(f"Teléfono: {cliente_encontrado.telefono}")
            print(f"Tipo de cliente: {texto_tipo_cliente(cliente_encontrado.tipo_cliente)}")
            print(f"Tipo de atención: {texto_tipo_atencion(cliente_encontrado.tipo_atencion)}")
            print(f"Cantidad: {cliente_encontrado.cantidad}")
            print(f"Prioridad: {texto_prioridad(cliente_encontrado.prioridad)}")
            print(f"Fecha de la cita: {cliente_encontrado.fecha_cita}")
            print(f"Valor total de la atención: ${cliente_encontrado.valor_total:,.0f} pesos mcte.")
            print(f"(Comparaciones realizadas: {comparaciones})")
        else:
            print()
            print(f"No se encontró ningún cliente con la cédula {cedula_buscar}.")
            print(f"(Comparaciones realizadas: {comparaciones})")

        respuesta_busqueda_valida = False
        while respuesta_busqueda_valida == False:
            print()
            respuesta_busqueda = input("¿Desea consultar otra cédula? (S/N): ")

            if respuesta_busqueda == "S" or respuesta_busqueda == "s":
                respuesta_busqueda_valida = True
                continuar_busqueda = "S"
            else:
                if respuesta_busqueda == "N" or respuesta_busqueda == "n":
                    respuesta_busqueda_valida = True
                    continuar_busqueda = "N"
                else:
                    print("Respuesta inválida. Por favor responda S (sí) o N (no).")

        if continuar_busqueda == "N":
            buscar_otro = False