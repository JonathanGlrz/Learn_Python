### Strings  ###

my_string = "Mi string"
my_other_string = "Mi otro string"
print(len(my_string))
print(len(my_other_string))

my_newline_string = "Este es un String\n con salto de linea"
print(my_newline_string) #Valor (\n) sirve para realizar un salto de linea

my_new_line_string = "\t Este es un String con tabulacion"
print(my_new_line_string) #Valor (\t ) sirve para realizar una tabulacion en el texto

my_scape_string = "\t Este es un string \n escapado"
print(my_scape_string)  #De esta forma realiza ambas operacion en la fresa (\t y \n)

### Formateo ###
name, surname, age = "Jonathan", "Galarza", 31
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  #Usando el .FORMAT usar siempre por defecto {} 
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))  #Usnado el %s, indicar variables despues del String con %(Variable)

### Desempaquetado de caracteres ###
language = "Python"
a, b, c, d ,e ,f = language
print(a)
print(c)

### Division ###
language_slice = language[1:3]
print(language_slice) #El valor asignado en el [] vuelca solo la letra

language_slice = language[1:]
print(language_slice) #Como no asignamos un valor final, vuelca todo lo siguiente

language_slice = language[-2]
print(language_slice) #El valor adopta un conteo inverso y vuelca la "O"

### Reverse ###
reversed_language = language[::-1]
print(reversed_language) #Vuelca de manera inversa la palabra indicada

### Funciones ###
print(language.capitalize()) #La funcion capitalize modifica la primera letra y la poner en mayuscula
print(language.upper()) #La funcion upper modifica a mayusculas toda la palabra
print(language.count("t")) #La funcion count, cuenta todas las letras del valor indicado y las imprime
print(language.isnumeric()) #La funcion is numerica, nos indica si la cadena indicada es numerica
print(language.lower()) #La funcion upper modifica a minusculas toda la palabra
print(language.upper().isupper()) #Concatenacion de funciones dentro de las opcionees
print(language.startswith("py")) #Esta funcion examina si la palabra coincide con el valor que le asignamos en la busqueda






