### LISTAS ###

my_list = list()
my_other_list = []

print(len(my_list)) # Devuelve 0 porque no hemos adjuntado datos en la lista
print(len(my_other_list)) # Devuelve 0 porque no hemos adjuntado datos en la lista

my_list = [35, 30, 39, 40]
print(my_list) #Devuelve los valores que hemos metido en la lista
print(len(my_list)) # Nos indica el numero de datos que hemos metido 
print(type(my_list)) # El tipo de dato es de tipo lista como nos devuelve, si guardamos con []

my_other_list = ("Joni", "Galarza", 31, 1.70)
print(my_other_list) # Podemos usar varios tipos de datos en la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3]) # Mediante este comando podemos llamar a un elemento especifico de la lista

my_list = [1, 1, 2, 2, 3, 3, 2, 2]
print(my_list.count(2)) # Devuelve el numero de veces que se repite ese valor

my_other_list = ("Joni", "Galarza", 31, 1.70)
name, surname, age, height = my_other_list
print(name)
print(height) # Podemos realizar la llamada del valor realizando la llamada usando otro valor



