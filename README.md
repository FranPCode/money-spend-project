# Money Spend Project

MIT LICENSE

Money Spend Project es una API para registrar gastos en distintas divisas, con seguimiento por fechas, categoría y moneda. El backend está implementado con Django y Django REST framework. 

## Instalación

### Requisitos Previos
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configurar Variables de entorno.
    Crear un archivo .env en la raiz del proyecto.
    ejemplo:
        DB_HOST=db
        DB_NAME=nombre_de_tu_base_de_datos
        DB_USER=tu_usuario
        DB_PASS=tu_contraseña
        DJANGO_SECRET_KEY=tu_clave_secreta

## Ejecucion del proyecto.

    docker compose up --build

## Documentacion.

    La pagina principal es la documentacions hecha con swagger.

### Clonar el Repositorio
```sh
git clone https://github.com/HEAVYSHOCK/money-spend-project.git
cd money-spend-project
