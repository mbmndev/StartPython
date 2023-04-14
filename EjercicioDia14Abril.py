## Enunciado

#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase. La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}


#Se pide:

#1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

total_sesiones = len(asistencias["Ana"]) + len(asistencias["Luis"])

print("Total de sesiones a las que asistieron Ana y Luis en conjunto:", total_sesiones)

#2. Mostrar las sesiones a las que asistieron ambos alumnos.
asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

ambos_asistieron = set(asistencias["Ana"]).intersection(asistencias["Luis"])

print("Sesiones a las que asistieron ambos alumnos:", ambos_asistieron)

#3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

uno_pero_no_ambos = set(asistencias["Ana"]).symmetric_difference(asistencias["Luis"])

print("Sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos:", uno_pero_no_ambos)

#4. Mostrar las sesiones a las que asistió Ana pero no Luis.

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

solo_ana = set(asistencias["Ana"]).difference(asistencias["Luis"])

print("Sesiones a las que asistió Ana pero no Luis:", solo_ana)

#5. Mostrar las sesiones a las que asistió Luis pero no Ana.

# Diccionario de asistencias
asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

# Paso 1: Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto
total_asistencias = len(set(asistencias["Ana"]) | set(asistencias["Luis"]))
print("Cantidad total de sesiones a las que asistieron Ana y Luis:", total_asistencias)

# Paso 2: Mostrar las sesiones a las que asistieron ambos alumnos
ambos_asistieron = set(asistencias["Ana"]) & set(asistencias["Luis"])
print("Sesiones a las que asistieron ambos alumnos:", ambos_asistieron)

# Paso 3: Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos
uno_no_ambos = (set(asistencias["Ana"]) | set(asistencias["Luis"])) - (set(asistencias["Ana"]) & set(asistencias["Luis"]))
print("Sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos:", uno_no_ambos)

# Paso 4: Mostrar las sesiones a las que asistió Ana pero no Luis
ana_no_luis = set(asistencias["Ana"]) - set(asistencias["Luis"])
print("Sesiones a las que asistió Ana pero no Luis:", ana_no_luis)

# Paso 5: Mostrar las sesiones a las que asistió Luis pero no Ana
luis_no_ana = set(asistencias["Luis"]) - set(asistencias["Ana"])
print("Sesiones a las que asistió Luis pero no Ana:", luis_no_ana)

