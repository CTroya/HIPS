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
2. Creamos un super usuario y ejecutamos el manage.py:
```
python3 manage.py createsuperuser
python3 manage.py runserver
```
3. Escribimos en el buscador de nuestro navegador:  
```
127.0.0.1:8000/login
``` 
Vermos una pagina asi:
![image](https://user-images.githubusercontent.com/70340830/182080342-ff20d760-1e3a-47a2-ae23-a7ec44a62395.png)

Ahora nos loguemos con las credenciales del super usuario que creamos en el paso 2. Y veremos una pagina asi:
![image](https://user-images.githubusercontent.com/70340830/182080632-567d0ffc-de72-4e87-bdea-603459ecbdec.png)

### Manual de uso
Una vez que estamos en la url /login/home/bruh tendremos un cuadro de texto para enviar comandos al HIPS.
IMPORTANTE: Antes de ejecutar cualquiere comando en el hips, poner en el cuadro de texto:
```
11
```
Esto hara que se ejecute un script de configuracion y acondicionamiento inicial en el sistema.
Este debe ser el primer comando ejecutado por el hips.
Deberiamos tener una respuesta tal que:
![image](https://user-images.githubusercontent.com/70340830/182080927-6659fa0c-9927-4dff-99e2-9014ab7332fd.png)

Entonces una vez hecha la configuracion inicial. Escribir en el cuadro de texto:
```
12 
```
Lo cual hara que se muestre en pantalla todos los comandos disponibles.
Tal que:
![image](https://user-images.githubusercontent.com/70340830/182080971-22571d38-5c07-4d7c-a0d6-76551b2c56b4.png)
