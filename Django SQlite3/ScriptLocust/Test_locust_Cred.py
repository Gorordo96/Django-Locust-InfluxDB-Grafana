from locust import HttpUser, task, between, TaskSet, User, constant, constant_pacing,events
import random
import json
import datetime
import pytz
from influxdb import InfluxDBClient
import socket





def obt_cred(nombre_archivo,cant_user):
    print("*************************************************")
    print(".............Procesando Credenciales.............")
    print("*************************************************")
    indice = list(range(0, 2 * cant_user - 1, 2))
    f = open(nombre_archivo, "r")
    List_prep = f.readline().replace("[", "").replace("'", "").replace("(", "").replace(")", "").replace("]","").split(",")
    Credenciales = []
    for j in indice:
        Credenciales.append(((List_prep[j], List_prep[j + 1])))
    return Credenciales

namefile="/mnt/locust/usuarios.txt"
cantidad_usuarios=10

hostname = socket.gethostname()
client = InfluxDBClient(host="172.20.0.4", port="8086",username="admin",password="admin",database="influx")

@events.request_success.add_listener
def individual_success_handle(request_type, name, response_time, response_length, **kwargs):
    SUCCESS_TEMPLATE = '[{"measurement": "%s","tags": {"hostname":"%s","requestName": "%s","requestType": "%s","status":"%s"},"time":"%s","fields": {"responseTime": "%s","responseLength":"%s"}}]'
    json_string = SUCCESS_TEMPLATE % ("ResponseTable", hostname, name, request_type, "success", datetime.datetime.now(tz=pytz.UTC), response_time, response_length)
    client.write_points(json.loads(json_string), time_precision='ms')

@events.request_failure.add_listener
def individual_fail_handle(request_type, name, response_time, response_length, exception, **kwargs):
    FAIL_TEMPLATE = '[{"measurement": "%s","tags": {"hostname":"%s","requestName": "%s","requestType": "%s","exception":"%s","status":"%s"},"time":"%s","fields": {"responseTime": "%s","responseLength":"%s"}}]'
    json_string = FAIL_TEMPLATE % ("ResponseTable", hostname, name, request_type, exception, "fail", datetime.datetime.now(tz=pytz.UTC), response_time, response_length)
    client.write_points(json.loads(json_string), time_precision='ms')

Credenciales=obt_cred(namefile,cantidad_usuarios)

class UserSensor(HttpUser):
    wait_time = constant_pacing (3)
    weight = 1

    @task
    def login_register_logout(self):
        usuario,contraseña,estado=self.login(Credenciales)
        if estado ==1:
            self.register_date()
            self.logout(usuario,contraseña)

    def login(self,Credenciales):
        if len(Credenciales) > 0:
            user,password=Credenciales.pop()
            respuesta = self.client.get("/accounts/login/")
            csrftoken = respuesta.cookies['csrftoken']
            self.client.post("/accounts/login/", {'username': user, 'password': password},headers={'X-CSRFToken': csrftoken})
            status=1
        else:
            status=0
            user=""
            password=""
        return user,password,status



    def register_date(self):
        ubc_var = ['RC', 'SAM', 'GD']
        ubc_selec = random.randint(0, 2)
        dat_var_num = [random.randint(-10, 50-1), random.randint(880, 1080-1), random.randint(0, 100-1)]
        csftoken=self.client.get("/registro/ingresar").cookies['csrftoken']
        self.client.post("/registro/privado", {'ubicacion':ubc_var[ubc_selec],'temperatura':dat_var_num[0],'presion':dat_var_num[1],'humedad':dat_var_num[2]},headers={'X-CSRFToken': csftoken})

    def logout(self,user,password):
        self.client.get("/accounts/logout/")
        Credenciales.append((user,password))

class UserCons(HttpUser):
    wait_time = between(120,360)
    weight = 3

    @task
    def consultaindex(self):
        self.client.get("/")

    @task
    def consultabasedatos(self):
        ubc_var = ['RC', 'SAM', 'GD']
        list_ubic=[]
        ubc_cant=random.randint(1,3)
        ubc = random.randint(0, 2)
        if ubc_cant == 1:
            list_ubic.append(ubc_var[ubc])
        elif ubc_cant == 2:
            list_ubic.append(ubc_var[ubc])
            ubc1=random.randint(0,2)
            while (ubc1 == ubc ):
                ubc1=random.randint(0, 2)
            list_ubic.append(ubc_var[ubc1])
        else:
            list_ubic=ubc_var

        dat_var = ['TEMP', 'PRE', 'HUM']
        list_dato=[]
        dat_cant=random.randint(1,3)
        dat = random.randint(0, 2)
        if dat_cant == 1:
            list_dato.append(dat_var[dat])
        elif dat_cant == 2:
            list_dato.append(dat_var[dat])
            dat1=random.randint(0,2)
            while (dat1 == dat ):
                dat1=random.randint(0, 2)
            list_dato.append(dat_var[dat1])
        else:
            list_dato=dat_var
        cookies=self.client.get("/registro/procUser").cookies['csrftoken']
        self.client.post("/registro/procUser",{'SelecUbic':list_ubic,'SelecDato':list_dato},headers={'X-CSRFToken':cookies})

