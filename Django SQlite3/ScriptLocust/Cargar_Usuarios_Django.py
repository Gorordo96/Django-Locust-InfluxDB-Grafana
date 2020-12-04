import requests
from string import ascii_letters
import random

#----------------------------------------------------------------------------------------------
#Creacion de lista de usuarios
string_base="sensor_"
cant_user=1000
longitud_contr=8
#-----------------------------------------------------------------------------------------------
letras=list(ascii_letters)
numeros=list(range(0,10))
user=[]
contras=[]
string_aux=list(range(1,cant_user+1))
for i in string_aux:
    conter=0
    contra = ""
    #---------------------------------------------
    #Generando usuario
    print(string_base+ str(i))
    user.append(string_base+ str(i))
    #---------------------------------------------
    #Generando contraseña
    while (conter<longitud_contr):
        conter=conter+1
        letra_or_number = random.randint(0, 1)
        if letra_or_number ==1:
            letra=random.choice(letras)
            contra=contra+letra
        else:
            numero=str(random.choice(numeros))
            contra=contra+numero
    print(contra)
    contras.append(contra)

#-----------------------------------------------------

print(user)
print(len(user))
print(contras)
print(len(contras))

#------------------------------------------------------
indice=list(range(0,len(user)))
diccionario=[]
for j in indice:
    URL = "http://172.20.0.2:8010/registro/nuevo"
    cliente=requests.session()
    cliente.get(URL)  # sets cookie
    if 'csrftoken' in cliente.cookies:
        # Django 1.6 and up
        csrftoken = cliente.cookies['csrftoken']
    else:
        # older versions
        csrftoken = cliente.cookies['csrf']

    register_data = dict(username=user[j], password1=contras[j],password2=contras[j], csrfmiddlewaretoken=csrftoken, next='/')
    print("realizando registro")
    r = cliente.post(URL, data=register_data, headers=dict(Referer=URL))
    diccionario.append((user[j], contras[j]))
print(diccionario)
f=open("usuarios.txt","w")
f.write(str(diccionario))
f.close()

#-------------------------------------------------------------------------------------------------
indice=list(range(0,2*len(user)-1,2))
print(indice)
f=open("usuarios.txt","r")
List_prep=f.readline().replace("[","").replace("'","").replace("(","").replace(")","").split(",")
dict_Locust=[]
for j in indice:
    dict_Locust.append(((List_prep[j],List_prep[j+1])))
print(dict_Locust)
#--------------------------------------------------------------------------------------------------
