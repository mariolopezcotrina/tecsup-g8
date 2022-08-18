# Introduccion a flask

## Creamos entorno virtual con python 

- Para crear el entorno virual se usa el comando: 
```bash
    python -m venv venv
```
- Para activar el entorno virtual se usa el comando ("bin" en MAC y "Scripts" en Windows):
```bash
    source venv/bin/activate
```
```bash
    source venv/Scripts/activate
```
- Para desactivar el entorno virtual se usa el comando:
```bash
    deactivate
```

## Instalamos flask
- Para instalar flask se usa el comando:
```bash
    pip install flask
```
- Para ver las librerias instaladas se usa el comando:
```bash
    pip freeze
```
```bash
    pip list
```

## Levantamos el servidor
- Para levantar el servidor se usa el comando:
```bash
    flask run
```
- Para levantar el servidor en modo debug se usa el comando:
```bash
    flask run --debugger
```