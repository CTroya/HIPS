# HIPS
Repositorio para el trabajo practico del HIPS de Sistemas operativos 2

### Integrantes:
- Carlos Troya
- Alain Vega

### Manual de instalacion
Para que el HIPS funcione necesitamos de las siguientes herramientas:
1. git
2. Python
3. Django
4. SQLAlchemy
5. sympy
Para lo cual, la forma de instalarlo en el sistema centos es la siguiente:
```
sudo dnf install git
yum install python39
sudo dnf install python3-pip
pip3 install django
sudo pip3.9 install SQLAlchemy
sudo pip3.9 install sympy
```
Una vez que ya tenemos las herramientas instaladas:
1. Clonamos el repositori:
```
git clone https://github.com/CTroya/HIPS.git
```
2. Agregamos nuestra direccion ip al archivo settings.py:
```
cd hips
vi settings.py
>>>   ALLOWED_HOSTS = [ 'tu_ip' ]
```
3. Creamos un super usuario y ejecutamos el manage.py:
```
python3 manage.py createsuperuser
python3 manage.py runserver
```
4. Escribimos en el navegador: tu_ip:80/login para ingresar con el super usuario que creamos:

### Manual de uso
Una vez que estamos en la url /login/home/bruh tendremos un cuadro de texto para enviar comandos al HIPS.
IMPORTANTE: Antes de ejecutar cualquiere comando en el hips, poner en el cuadro de texto:
```
11
```
Esto hara que se ejecute un script de configuracion y acondicionamiento inicial en el sistema.
Este debe ser el primer comando ejecutado por el hips.

Entonces una vez hecha la configuracion inicial. Escribir en el cuadro de texto:
```
12 
```
Lo cual hara que se muestre en pantalla todos los comandos disponibles.
