# 🕹️ Arcade HUD Overlay
Visualizador gráfico de entradas tipo arcade para joystick o teclado, diseñado como overlay para emuladores.
Perfecto para tutoriales de juegos de pelea, demostraciones de habilidad o como herramienta de entrenamiento.

## Características
* Soporta joystick y teclado.
* Configuración de botones en "~/.HUDOverlay.toml" (porfavor consulte la [api de RAYLIB](https://www.raylib.com/cheatsheet/cheatsheet.html) para saber el codigo de los botones) 

### Requisitos 
* python >= 3.14
* raylib >= 5.5.0
* uv >= 0.10

## Uso
 ```bash
#Clonar el repositorio
git clone https://github.com/MayorTom4815/hud_overlay.git

#Cambiar a la carpeta del proyecto
cd hud_overlay

#Crear el entorno virtual
uv venv

#Descargar las librerias con uv
uv sync

#Activar el entorno virtual en linux
source .venv/bin/activate

#Activar el entorno virtual en windows
.venv/bin/activate.ps1

#Iniciar el programa
uv run main.py
```
## Estado actual del proyecto (Versión 1)
* Se a refactorizado el programa utilizando raylib en vez de Pygame para una mejor compatibilidad
* Ya hay transparencia, pero aun falla en Linux.
* Se ha optado por usar toml en vez de sqlite para las configuraciones
* Puedes intercalar entre el jostick y teclado pulsando "la flecha Izquierda"

### Por Hacer
1. Hacer que el programa detecte el teclado sin estar enfocado.
2. Tratar de corregir la transparencia en Linux
3. Implementar el mapeo de botones mientras corre el programa

## 👾 Créditos
Este proyecto fue desarrollado con amor al figthing y *mucha paciencia por leer el codigo de un novato.*
**@Cat-not-furry** (creador del proyecto)
