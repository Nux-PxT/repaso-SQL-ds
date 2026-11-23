# Practica 1
# Definimos las variables con los tipos de datos
producto = "Teclado" # string
precio = 13.5 # float
cantidad = 2 # int 
Descuento = True # bool 

# Mostramos esa informacion en una breve frase mediante la funcion print
print(f"Vendo {producto} al precio de {precio}, me quedan {cantidad} en stock y posee descuento.\n")


# Practica 2

precios = [10, 15, 115, 245, 100]

for numero in precios: # itera sobre la lista usando la variable numero
    if numero > 100: # ¿numero es mayor a 100?
        print("Caro") # Respuesta si es True 
    else:
        print("Economico") # Respuesta si es False
print("")

# Practica 3 
# Creaccion del diccionario (almacen)
almacen = {
    "Teclado": 1,
    "Mouse": 2,
    "Silla": 1,
    "Parlante": 3,
    "Gabinete": 2
}

almacen["SSD"] = 1 # agregamos un nuevo producto con su cantidad

print(f"Stock del Teclado: {almacen['Teclado']}\n") # mostramos el diccionario completo para corroborar que se agrego 

# Practica 4
# Definimos la funcion y su parametro 
def resumen_estadistico(numeros): # En este caso numeros recibe una lista
    cantidad = len(numeros) # usamos len para contar cuantos elementos tiene esa lista 
    suma = 0 # definoms una variable local en 0 para sacar el total 
    for x in numeros: # iteramos en la lista y guardamos un valor a la vez en x 
        suma += x
    promedio = suma / cantidad # sacamos el promedio 
    
    return { # retornamos un diccionario usando los valores obtenido 
        "suma": suma,
        "cantidad": cantidad,
        "promedio": promedio
    }
    
diccionario = resumen_estadistico(precios) # guardamos los resultados en una nueva variable 
print(diccionario) # mostramos el resultado 