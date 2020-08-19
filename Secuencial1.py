
#Ejercisio Arrays Python3

list1= ["Jabon", "Hawai", "Helecho", "Copia", "Moto"]
list2= ["Carbon", "Hawai", "Felicidad", "Moto"]
list3= [list1,list2]
print (list3)
conjunto= list (set(list1) - set(list2))
print (conjunto)
conjunto= list (set(list2) - set(list1))
print (conjunto)
print (list3)