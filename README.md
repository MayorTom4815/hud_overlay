# 🕹️ Arcade HUD Overlay

Visualizador gráfico de entradas tipo arcade para joystick o teclado, diseñado como overlay para emuladores.
Perfecto para tutoriales de juegos de pelea, demostraciones de habilidad o como herramienta de entrenamiento.

## Características

* Soporta joystick y teclado.
* Detecta 4 o 6 botones.
* Asignación personalizada para cada botón.
* Las configuraciones se guardan en "~/binginds.db".

### Requisitos 

* Python >= 3.13
* Pygame >= 2.6.1
* uv >= 0.7

## Uso
Aun no hay una version compilada, asi que toca ejecutar en terminal.

 ```bash
#Clonar el repositorio
git clone https://github.com/tu_usuario/hud_overlay.git

#Cambiar a la carpeta del proyecto
cd hud_overlay

#activar el entorno virtual en linux
source .venv/bin/activate

#activar el entorno virtual en windows
.venv/bin/activate.ps1

#Descargar las librerias con uv
uv sync

#Descargar las librerias con pip
pip install requirements.txt

#Iniciar el programa
make run 
```
## Estado actual del proyecto (version 0.2.1)
* Se ha removido la libreria evdev, puesto que pygame tiene su soporte para joysicks.
* Aun no hay un transparente al completo solo emulado por pygame, por ende no hay trasparencia. :[

* Refactor del proyecto completo ahora es mas modable.


### Por Hacer
1. Hacer una interfaz mas comoda (Agregar botones en vez de teclas para seleccionar las opciones, una mejor fuente, etc...).

2. hacer que el programa detecte al 100% sin estar enfocado.

## 👾 Créditos
Este proyecto fue desarrollado con amor al figthing y *mucha paciencia por leer el codigo de un novato.*

**@Cat-not-furry** (creador del proyecto)
