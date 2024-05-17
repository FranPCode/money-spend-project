Proyecto de gestion de gastos con seguimiento por fechas, categoria y moneda.

Backend con Django y Django REST
Frontend con React (no implementado por ahora)

Uso:
Hasta ahora solo se tiene implementado la API y su documentacion en swagger.

Aqui estan las urls disponibles:
-http://127.0.0.1:8000/api/spends/all
-http://127.0.0.1:8000/api/spends/{pk}
-http://127.0.0.1:8000/api/categories/all
-http://127.0.0.1:8000/api/categories/{pk}
-http://127.0.0.1:8000/api/currencies/all
-http://127.0.0.1:8000/api/currencies/{pk}
-http://127.0.0.1:8000/api/users/all
-http://127.0.0.1:8000/api/users/{pk}

Como instalar:
Para el entorno virtual uso "pipenv".
$ pip install pipenv

Se activa el entorno virtual
$ pipenv shell

Se instalan los paquetes de pipfile.lock
$ pipenv install --ignore-pipfile


Se necesita cambiar el interprete al interprete del entorno virtual.

Para iniciar el proyecto:
$ manage.py runserver



