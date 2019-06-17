# Backend test

Esta es una implementación de un API que cuenta con seis endpoints principales:

1. Consulta de la cantidad de viajes totales.
2. Consulta de la cantidad de viajes totales por ciudad.
3. Consultar la cantidad de viajes totales por país.
4. Crear un viaje.
5. Actualizar un viaje.
6. Consultar los viajes actuales

Esta api fue realizada con el framework Django de Python y se encuentra dentro de la carprta [backend_test](backend_test).

Para su despliegue es necesario tener instalado python3 y mongodb en el sistema. En el caso de Ubuntu(linux) basta con ejecutar los siguientes comandos para su instalación:

```
sudo apt-get install python3.6
sudo apt install -y mongodb 
```

Para la implementación se utilizo el gestor de paquetes de python PIP3 para instalar los paquetes necesarios en el proyecto.

```
sudo apt install python3-pip
```

## Ejecución

Para la ejecución de la aplicación basta con realizar la instalción de los paquetes utilizados en el proyecto con el siguiente comando

```
pip install -r requirements.txt
```

Posteriormente se debe ejecutar el servidor utilizando el siguiente comando

```
python3 manage.py runserver
```

El servidor de desarrollo sera lazado en `http://127.0.0.1:8000/`

## Consumo API

Aunque el servidor fue lanzado en `http://127.0.0.1:8000/`. La dirección inicial del api se encuentra en `http://127.0.0.1:8000/api/v1/`

Como se enuncia al inicio el api cuenta con seis endpoints los cuales encuentran en las siguientes direcciones:

1. Consulta de la cantidad de viajes totales: `http://127.0.0.1:8001/api/v1/trips/count`
2. Consulta de la cantidad de viajes totales por ciudad: `http://127.0.0.1:8001/api/v1/trips/count/?city=name_city`
3. Consultar la cantidad de viajes totales por país: `http://127.0.0.1:8001/api/v1/trips/count/?country=name_country`
4. Crear un viaje. `http://127.0.0.1:8000/api/v1/trips/`
5. Actualizar un viaje. `http://127.0.0.1:8000/api/v1/trips/id_trip/`
6. Consultar los viajes actuales `http://127.0.0.1:8001/api/v1/trips/?status=started`

Los metodos HTTP usados para cada petición son:
1. Consulta de la cantidad de viajes totales. [GET]
2. Consulta de la cantidad de viajes totales por ciudad. [GET]
3. Consultar la cantidad de viajes totales por país. [GET]
4. Crear un viaje. [POST]
5. Actualizar un viaje. [PUT]
6. Consultar los viajes actuales. [GET]

La documentación completa se puede encontrar en el archivo [sawgger.yaml](sawgger.yaml). Para ver la documentación basta con importar el archivo en [http://editor.swagger.io/](http://editor.swagger.io/).

## Consideraciones

El flujo de trabajo implementado fue Git flow. Cada caracteristica del desarrollo se realizo en una rama individual, la cual tenia como padre la rama develop. Al final todas las ramas fueron unidas con su rama padre utilizando rebase.

### Arquitectura
![Arquitectura API](Arquitecture.png)

## Retos

Los retos se pueden encontrar en la carpeta [challenges](challenges)
