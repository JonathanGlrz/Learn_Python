### Variables ###

my_str_variable = "My String variable"
print(my_str_variable) # Variable STR

my_int_variable = 5
print(my_int_variable) # Variable INT

my_bool_variable = False
print(my_bool_variable) # Variable BOOL

# Concatenacion de todas las variables
print(my_str_variable, my_int_variable, my_bool_variable)

# Transformacion de un tipo de variable a otra
my_int_to_variable = str(my_int_variable) # Declaramos una nueva variable e indicamos el cambio a realizar de variable STR
print(my_int_to_variable) 
print(type(my_int_to_variable)) # Al usar el TYPE observamos que la variable ya no es INT sino STR
    #Al reailzar este cambio de tipo, ya no nos permite poder usar ese valor como un numero para realizar calculos

#Funcion del valor len
print(len(my_str_variable)) # LEN, cuenta todos los caracteres del texto

# Variables en una sola linea
name, surname, age, alias = "Jonatha", "Galarza", 33, "Joni"
print("Me llamo ", name, surname, "tengo ", age, " años", " y me llaman ", alias)

#INPUTS - Sirben para introducir datos por consola al usuario
name = input("¿Cual es tu nombre? ")
edad = input("¿Cual es tu edad? ")
print(name)
print(edad)
