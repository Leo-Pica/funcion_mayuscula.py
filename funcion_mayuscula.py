def mayuscula_primera(cadena):#definimos una función para poner mayúsculas al inico de la palabra.
    return cadena.title() #esto es para que retorne una copia de la cadena ingresada.

# Ejemplo de uso:
texto = "estas palabras deberían comenzar con mayúsculas"
resultado = mayuscula_primera(texto) #asignamos "mayuscula_primera" a la variable "resulatdo"
print(resultado)  #mostramos el resultado que debería ser:"Estas Palabras Deberían Comenzar Con Mayúsculas"
